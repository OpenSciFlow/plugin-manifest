from __future__ import annotations

import json
import re
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "opensciflow-plugin.schema.json"
EXAMPLES_DIR = ROOT / "examples"
COMMAND_FIXTURES_PATH = ROOT / "tests" / "command-rendering-fixtures.json"
PLACEHOLDER_RE = re.compile(r"{([^{}]+)}")
DANGEROUS_SHELL_FRAGMENTS = ("&&", "||", ";", "`", "$(", "\n", "\r")


def declared_names(items: object) -> set[str]:
    if not isinstance(items, list):
        return set()
    names: set[str] = set()
    for item in items:
        if isinstance(item, dict) and isinstance(item.get("name"), str):
            names.add(item["name"])
    return names


def command_templates(data: dict) -> list[tuple[str, str]]:
    execution = data.get("execution", {})
    if not isinstance(execution, dict):
        return []

    templates: list[tuple[str, str]] = []
    for section_name, section in execution.items():
        if not isinstance(section, dict):
            continue
        for key, value in section.items():
            if "command" in key and isinstance(value, str):
                templates.append((f"execution.{section_name}.{key}", value))
    return templates


def validate_command_templates(data: dict) -> list[str]:
    errors: list[str] = []
    inputs = declared_names(data.get("inputs"))
    outputs = declared_names(data.get("outputs"))
    parameters = declared_names(data.get("parameters"))
    allowed_literals = {"outputs_dir", "run_directory"}

    templates = command_templates(data)
    local_templates = [path for path, _ in templates if path.startswith("execution.local.")]
    if not local_templates:
        errors.append("execution.local must define at least one reviewed command template")

    for location, command in templates:
        for fragment in DANGEROUS_SHELL_FRAGMENTS:
            if fragment in command:
                errors.append(f"{location}: command contains disallowed shell fragment {fragment!r}")

        for placeholder in PLACEHOLDER_RE.findall(command):
            if placeholder in allowed_literals:
                continue
            if "." not in placeholder:
                errors.append(f"{location}: unknown placeholder {{{placeholder}}}")
                continue

            section, name = placeholder.split(".", 1)
            if section == "inputs":
                if name not in inputs:
                    errors.append(f"{location}: placeholder {{{placeholder}}} is not declared in inputs")
            elif section == "outputs":
                if name not in outputs:
                    errors.append(f"{location}: placeholder {{{placeholder}}} is not declared in outputs")
            elif section == "parameters":
                if name not in parameters:
                    errors.append(f"{location}: placeholder {{{placeholder}}} is not declared in parameters")
            else:
                errors.append(f"{location}: unsupported placeholder namespace {{{placeholder}}}")

    return errors


def render_command_template(template: str, values: dict[str, str]) -> str:
    missing: list[str] = []
    invalid: list[str] = []

    def replace(match: re.Match[str]) -> str:
        placeholder = match.group(1)
        value = values.get(placeholder)
        if value is None:
            missing.append(placeholder)
            return match.group(0)
        if not isinstance(value, str) or not value:
            invalid.append(placeholder)
            return match.group(0)
        return value

    rendered = PLACEHOLDER_RE.sub(replace, template)

    if missing:
        raise ValueError(f"missing values for placeholders: {', '.join(sorted(set(missing)))}")
    if invalid:
        raise ValueError(f"invalid values for placeholders: {', '.join(sorted(set(invalid)))}")

    return rendered


def validate_command_rendering_fixtures() -> list[str]:
    errors: list[str] = []

    if not COMMAND_FIXTURES_PATH.exists():
        return errors

    fixtures = json.loads(COMMAND_FIXTURES_PATH.read_text(encoding="utf-8"))
    if not isinstance(fixtures, list):
        return ["tests/command-rendering-fixtures.json must contain a list"]

    for index, fixture in enumerate(fixtures):
        if not isinstance(fixture, dict):
            errors.append(f"command fixture {index} must be an object")
            continue

        name = fixture.get("name", f"fixture[{index}]")
        template = fixture.get("template")
        values = fixture.get("values")
        expected = fixture.get("expected")

        if not isinstance(template, str) or not template:
            errors.append(f"{name}: template must be a non-empty string")
            continue
        if not isinstance(values, dict):
            errors.append(f"{name}: values must be an object")
            continue
        if not isinstance(expected, str) or not expected:
            errors.append(f"{name}: expected must be a non-empty string")
            continue

        try:
            rendered = render_command_template(template, values)
        except ValueError as exc:
            errors.append(f"{name}: {exc}")
            continue

        if rendered != expected:
            errors.append(f"{name}: rendered command does not match expected output")

        for fragment in DANGEROUS_SHELL_FRAGMENTS:
            if fragment in rendered:
                errors.append(f"{name}: rendered command contains disallowed shell fragment {fragment!r}")

    return errors


def main() -> None:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    files = sorted(EXAMPLES_DIR.glob("*/opensciflow.yaml"))
    if not files:
        raise SystemExit("No plugin examples found")

    errors: list[str] = []
    for path in files:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            jsonschema.validate(data, schema)
            for error in validate_command_templates(data):
                errors.append(f"{path.relative_to(ROOT)}: {error}")
        except Exception as exc:  # noqa: BLE001 - report all validation failures clearly.
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    errors.extend(validate_command_rendering_fixtures())

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(files)} plugin manifests")


if __name__ == "__main__":
    main()
