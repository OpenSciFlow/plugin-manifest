# MDAnalysis trajectory-analysis readiness

Current OpenSciFlow readiness target:

```text
R2 metadata-reviewed -> R3 dry-run ready
```

This manifest should not be marked `R3` until a dry run has been executed in a documented environment and the evidence is recorded.

## Current status

As of 2026-07-06:

- Manifest schema validation passes.
- Command-template placeholder validation passes.
- License/citation fields are present but should still be checked against upstream guidance.
- Dry-run command is declared.
- No dry-run evidence has been committed yet.

## Dry-run command

Declared in `opensciflow.yaml`:

```bash
python -c "import MDAnalysis as mda; print(mda.__version__)"
```

## Evidence required for R3

Record:

| Field | Required evidence |
|---|---|
| Python version | `python --version` output |
| MDAnalysis version | dry-run command output |
| Installation route | Conda, pip, container, or existing environment |
| Platform | OS and architecture |
| Date | ISO date/time |
| Exit code | Must be `0` |
| Log | Full command and output |

## R3 evidence template

```text
checked_at:
platform:
python_version:
install_route:
command:
exit_code:
stdout:
stderr:
reviewer:
notes:
```

## Not required for R3

R3 does not require running a trajectory analysis or producing scientific artifacts.

Those belong to:

- `R4`: smoke test with tiny public input.
- `R5`: complete run record.
- `R6`: use inside a tested workflow template.

## Candidate R4/R5 sample data

Preferred candidate:

```text
MDAnalysisData adk_equilibrium
```

Do not treat this as finalized until license, citation, file sizes, and SHA256 hashes are recorded.
