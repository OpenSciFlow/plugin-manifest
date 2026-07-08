# Readiness levels

Readiness levels describe evidence for an OpenSciFlow tool or capsule.

They do not certify scientific correctness. They do not guarantee that a tool runs across all environments.

For the checks that generate readiness evidence, see `docs/validation-levels.md`.

## Levels

| Level | Name | Meaning |
|---|---|---|
| R0 | Project indexed only | Only a project link and basic information exist. |
| R1 | Draft manifest | A manifest draft exists, but it has not been validated. |
| R2 | Schema-validated manifest | The manifest passes schema validation. |
| R3 | Environment spec and command templates available | Environment information and reviewed command templates exist. |
| R4 | Smoke test passed in one environment | A minimal smoke test passed in at least one recorded environment. |
| R5 | Example run passed with run record | A real example run passed in at least one environment and produced a run record. |
| R6 | Multi-environment verification | The capsule has passed or failed with records across two or more heterogeneous environments. |
| R7 | External reproduction | An external user or external machine reproduced the capsule successfully and recorded evidence. |

## Allowed agent behavior

| Level | Agent may inspect? | Agent may execute? | Notes |
|---|---|---|---|
| R0 | Yes | No | Landscape only. |
| R1 | Yes | No | Draft metadata only. |
| R2 | Yes | No by default | Schema-valid does not mean runnable. |
| R3 | Yes | Readiness checks only by default | Commands exist but no smoke-test evidence yet. |
| R4 | Yes | Smoke test with approval | Evidence applies only to the recorded environment. |
| R5 | Yes | Example run with approval | Execution must write a run record. |
| R6 | Yes | Yes with environment matching and approval | Multi-environment evidence exists but remains bounded. |
| R7 | Yes | Yes with environment matching and approval | External reproduction exists; scientific correctness is still not certified. |

## Interpretation rule

- R1/R2 may reduce documentation-understanding cost.
- R4/R5 may cautiously reduce trial-and-error cost in the verified environment.
- R6/R7 provide stronger evidence for cross-environment migration or external reproduction.

Do not claim a manifest reduces execution trial-and-error cost until at least R4 evidence exists.

Do not claim cross-environment reproducibility until R6 or R7 evidence exists.

## Required evidence by level

### R1

- Draft manifest exists.
- Required fields are visible, even if incomplete.

### R2

- Manifest parses.
- JSON Schema validation passes.
- Required top-level fields exist.

### R3

- Environment spec exists.
- Reviewed command templates or reviewed wrapper metadata exist.
- Required inputs, outputs, model weights, licenses, citations, safety notes, and limitations are declared.

### R4

- Smoke-test command exists.
- Smoke-test result is recorded.
- Environment information is recorded.
- Failure or success is explicit.

### R5

- Example input exists or is regenerable.
- Expected outputs are listed.
- Example run completed.
- Run record captures commands, versions, parameters, logs, return code, artifacts, hashes, citations, licenses, limitations, and warnings.

### R6

- Two or more environments are recorded.
- Differences between environments are explicit.
- Known failures are not hidden.

### R7

- Reproduction evidence comes from an external user, machine, lab, or CI environment.
- The reproduced run record is linked or included.

## Status labels

Recommended issue labels:

- `readiness:R0-indexed`
- `readiness:R1-draft-manifest`
- `readiness:R2-schema-validated`
- `readiness:R3-env-and-commands`
- `readiness:R4-smoke-test`
- `readiness:R5-example-run`
- `readiness:R6-multi-env`
- `readiness:R7-external-reproduction`
