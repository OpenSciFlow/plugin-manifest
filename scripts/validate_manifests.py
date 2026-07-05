from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import yaml


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "schema" / "opensciflow-plugin.schema.json"
EXAMPLES_DIR = ROOT / "examples"


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
        except Exception as exc:  # noqa: BLE001 - report all validation failures clearly.
            errors.append(f"{path.relative_to(ROOT)}: {exc}")

    if errors:
        raise SystemExit("\n".join(errors))

    print(f"Validated {len(files)} plugin manifests")


if __name__ == "__main__":
    main()

