# Validation levels

Validation levels describe checks performed on a manifest or execution path.

They are related to readiness levels, but not identical:

- readiness levels summarize current evidence;
- validation levels describe the checks that generate that evidence.

## Levels

| Level | Name | Checks | Typical readiness impact |
|---|---|---|---|
| V0 | Listed only | Project is known, but no manifest exists. | R0 |
| V1 | Draft presence check | A manifest draft exists and required fields are visible. | R1 |
| V2 | Schema validation | YAML parses, required fields exist, JSON Schema passes. | R2 |
| V3 | Environment and command-template validation | Environment specs exist and reviewed command templates use declared placeholders and avoid disallowed shell fragments. | R3 |
| V4 | Smoke-test validation | A minimal version/import/help/tiny-input check exits with `0` in a documented environment. | R4 |
| V5 | Example-run validation | Tiny public or regenerable input produces expected files. | R5 when paired with a run record |
| V6 | Run-record validation | Execution produces a complete run record with commands, versions, hashes, artifacts, citations, licenses, limitations, warnings, and known failures. | R5 |
| V7 | Multi-environment or external validation | Evidence exists across multiple environments or from an external reproducer. | R6/R7 |

## Fail-closed rule

If a check fails, the agent should stop at the last validated level and report missing requirements.

Do not skip from schema validation to execution because an upstream project is popular or widely cited.

## Minimum evidence by level

### V1 draft presence check

- Manifest draft exists.
- Required fields are visible, even if incomplete.

### V2 schema validation

- Manifest parses as YAML.
- JSON Schema validation passes.
- Required top-level fields exist.

### V3 environment and command-template validation

- `license.software` exists.
- `license.data` exists.
- `citation.preferred` exists.
- Required model weights have source, license, and checksum fields.
- Limitations are domain-specific.
- Command placeholders reference declared inputs, outputs, parameters, or approved runner fields.
- Disallowed shell fragments are absent.
- Reviewed wrappers are declared when wrappers are needed.
- Environment specs are explicit enough to attempt a smoke test.

### V4 smoke-test validation

- Smoke-test command is declared.
- It does not require private data or expensive compute.
- Environment is documented.
- Exit code is `0`.
- Output shows a version, help text, import success, or equivalent readiness signal.

### V5 example-run validation

- Tiny public input is available or generated.
- Expected files are listed.
- Output interpretation is limited to smoke-test success.

### V6 run-record validation

- Rendered command is recorded.
- Input hashes are recorded.
- Output artifacts and hashes are recorded where available.
- Tool versions and environment metadata are recorded.
- Citations, licenses, limitations, and warnings are preserved.

### V7 multi-environment or external validation

- At least two heterogeneous environments have recorded pass/fail evidence, or an external user/machine has reproduced the capsule.
- Known failures are recorded rather than hidden.

## Current validator coverage

The current v0.1 validator covers:

- V1 draft presence checks;
- V2 schema validation;
- part of V2 license/citation/model-weight metadata validation;
- V3 command-template placeholder, reviewed-wrapper, and shell-fragment checks;
- command rendering fixtures.

V4-V7 require committed smoke-test evidence, example-run records, verified environment matrices, or external reproduction evidence.
