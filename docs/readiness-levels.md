# Readiness levels

Readiness levels describe whether a manifest can be used by an OpenSciFlow-compatible local agent.

They do not certify scientific correctness.

## Levels

| Level | Name | Meaning |
|---|---|---|
| R0 | Listed | Project is listed in the landscape but has no manifest. |
| R1 | Draft manifest | Manifest exists and passes basic schema validation. |
| R2 | Metadata reviewed | License, citation, inputs, outputs, environment, hardware, weights, safety notes, and limitations have been reviewed. |
| R3 | Dry-run ready | Dry-run command succeeds in a documented environment. |
| R4 | Smoke-test ready | Tiny example input produces expected files. |
| R5 | Run-record ready | Execution produces a complete run record with input hashes, commands, versions, artifacts, citations, and limitations. |
| R6 | Workflow ready | Manifest is used inside a workflow template with tested report generation. |

## Allowed agent behavior

| Level | Agent may select? | Agent may execute? | Notes |
|---|---|---|---|
| R0 | No | No | Landscape only. |
| R1 | No by default | No | Review target only. |
| R2 | With warning | No by default | Metadata is reviewed but not executable. |
| R3 | Yes for readiness check | Dry-run only | No scientific output. |
| R4 | Yes for demo | Smoke test only unless user provides explicit inputs. |
| R5 | Yes | Yes with approval | Execution must write run record. |
| R6 | Yes | Yes with workflow approval | Preferred level for BioPilot workflows. |

## Required evidence by level

### R1

- Manifest parses.
- JSON Schema validation passes.
- Required top-level fields exist.

### R2

- License fields are reviewed.
- Citation fields are reviewed.
- Model-weight/data terms are explicit.
- Safety notes and limitations are domain-specific.
- Maintainer or curator review is linked.

### R3

- Dry-run command exists.
- Environment instructions are sufficient to run the dry run.
- Dry run records tool version where possible.

### R4

- Tiny input is available or generated.
- Smoke-test command exists.
- Expected files are listed.
- Smoke-test output does not require private data.

### R5

- Run record includes:
  - manifest name and version;
  - workflow name, if applicable;
  - input file hashes;
  - rendered command;
  - environment versions;
  - model-weight source and checksum, if applicable;
  - logs;
  - output artifacts and hashes;
  - citations;
  - limitations;
  - timestamps.
- The run record should validate against the current BioPilot run-record schema when used by the reference prototype.

### R6

- Workflow template references the manifest.
- Workflow validation passes.
- Report template renders.
- Scientific claim boundaries appear in the report.

## Status labels

Recommended issue labels:

- `readiness:R0-listed`
- `readiness:R1-draft`
- `readiness:R2-reviewed`
- `readiness:R3-dry-run`
- `readiness:R4-smoke-test`
- `readiness:R5-run-record`
- `readiness:R6-workflow`

## Rule for model manifests

A model manifest cannot exceed R2 unless it records:

- model-weight source;
- model-weight license;
- checksum or documented reason checksum is unavailable;
- exact model version or release;
- applicability-domain statement.
