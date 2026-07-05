# OpenSciFlow Plugin Manifest

Draft standard for describing AI for Science tools, models, environments, execution commands, HPC support, validation tests, licenses, citations, safety notes, and known limitations.

Recommended manifest filename:

```text
opensciflow.yaml
```

## Design goals

- Human-readable.
- Lightweight v0.1 fields.
- Local/HPC execution aware.
- Explicit license and citation.
- Validation before execution.
- No arbitrary LLM-generated shell execution.

## Contents

- `schema/opensciflow-plugin.schema.json`
- `examples/gromacs-md-stability/opensciflow.yaml`
- `examples/proteinflux-dynamics/opensciflow.yaml`
- `examples/diffdock-docking/opensciflow.yaml`
- `docs/design-principles.md`
- `ISSUES.md`
- `MILESTONES.md`

