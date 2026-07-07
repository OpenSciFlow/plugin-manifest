# Validation levels

Validation levels describe checks performed on a manifest or execution path.

They are related to readiness levels, but not identical:

- readiness levels summarize current evidence;
- validation levels describe the checks that generate that evidence.

## Levels

| Level | Name | Checks | Typical readiness impact |
|---|---|---|---|
| V0 | Listed only | Project is known, but no manifest exists. | R0 |
| V1 | Schema validation | YAML parses, required fields exist, JSON Schema passes. | R1 |
| V2 | Metadata validation | License, citation, inputs, outputs, environment, hardware, weights, safety notes, and limitations are present and reviewable. | R2 |
| V3 | Command-template validation | Reviewed command templates use declared placeholders and avoid disallowed shell fragments. | R2/R3 prerequisite |
| V4 | Dry-run validation | Declared non-destructive dry-run command exits with `0` in a documented environment. | R3 |
| V5 | Smoke-test validation | Tiny public input produces expected files. | R4 |
| V6 | Run-record validation | Execution produces a complete run record with commands, versions, hashes, artifacts, citations, licenses, limitations, and warnings. | R5 |
| V7 | Workflow validation | Manifest is used in a workflow template with DAG, artifact handoff, report, and run-record checks. | R6 |

## Fail-closed rule

If a check fails, the agent should stop at the last validated level and report missing requirements.

Do not skip from schema validation to execution because an upstream project is popular or widely cited.

## Minimum evidence by level

### V1 schema validation

- Manifest parses as YAML.
- JSON Schema validation passes.
- Required top-level fields exist.

### V2 metadata validation

- `license.software` exists.
- `license.data` exists.
- `citation.preferred` exists.
- Required model weights have source, license, and checksum fields.
- Limitations are domain-specific.

### V3 command-template validation

- Command placeholders reference declared inputs, outputs, parameters, or approved runner fields.
- Disallowed shell fragments are absent.
- Reviewed wrappers are declared when wrappers are needed.

### V4 dry-run validation

- Dry-run command is declared.
- It does not require private data or expensive compute.
- Environment is documented.
- Exit code is `0`.
- Output shows a version, help text, import success, or equivalent readiness signal.

### V5 smoke-test validation

- Tiny public input is available or generated.
- Expected files are listed.
- Output interpretation is limited to smoke-test success.

### V6 run-record validation

- Rendered command is recorded.
- Input hashes are recorded.
- Output artifacts and hashes are recorded where available.
- Tool versions and environment metadata are recorded.
- Citations, licenses, limitations, and warnings are preserved.

### V7 workflow validation

- Workflow template validates.
- DAG is acyclic.
- Step `consumes` and `produces` handoff is valid.
- Report includes citations and limitations.
- Run record validates.

## Current validator coverage

The current v0.1 validator covers:

- V1 schema validation;
- part of V2 license/citation/model-weight metadata validation;
- V3 command-template placeholder and shell-fragment checks;
- command rendering fixtures.

V4-V7 require committed evidence files, run records, or workflow-template validation.

