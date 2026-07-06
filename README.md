# OpenSciFlow Plugin Manifest

Draft standard for describing AI for Science tools, models, environments, execution commands, HPC support, validation tests, licenses, citations, safety notes, and known limitations.

Recommended manifest filename:

```text
opensciflow.yaml
```

## Status

Draft v0.1. This repository is intended for public review and correction, not production deployment.

## Design goals

- Human-readable.
- Lightweight v0.1 fields.
- Local/HPC execution aware.
- Explicit license and citation.
- Validation before execution.
- No arbitrary LLM-generated shell execution.
- Compatible with Conda, Docker, Apptainer, Slurm, and existing model/tool ecosystems.

## Required fields

| Field | Purpose |
|---|---|
| `schema_version` | Manifest schema version, currently `opensciflow.plugin/v0.1` |
| `name` | Stable plugin identifier |
| `version` | Manifest version |
| `domain` | Scientific domain tags |
| `task_types` | Supported task types |
| `description` | Short human-readable summary |
| `authors` | Manifest/tool authors or maintainers |
| `license` | Software, model weight, and data license metadata |
| `citation` | Preferred citation, DOI, or URL |
| `inputs` | Required/optional inputs and formats |
| `outputs` | Expected outputs and formats |
| `environment` | Conda/Docker/Apptainer/system requirements |
| `hardware` | CPU, memory, GPU, and accelerator requirements |
| `model_weights` | Whether weights are required and where to obtain them |
| `execution` | Local and optional Slurm execution commands |
| `expected_runtime` | Small example and typical runtime estimates |
| `examples` | Example inputs and expected outputs |
| `validation` | Schema, dry-run, and smoke-test rules |
| `safety_notes` | Execution and scientific safety notes |
| `limitations` | Known scientific or technical limitations |

## Minimal example

```yaml
schema_version: "opensciflow.plugin/v0.1"
name: "example-tool"
version: "0.1.0"
domain: ["computational-biology"]
task_types: ["trajectory-analysis"]
description: "Example plugin manifest for an AI for Science command-line tool."
authors:
  - name: "Tool Maintainers"
license:
  software: "MIT"
  model_weights: "not-applicable"
  data: "CC-BY-4.0"
citation:
  preferred: "Tool Maintainers. Example Tool. 2026."
inputs:
  - name: "structure"
    type: "file"
    formats: ["pdb"]
    required: true
outputs:
  - name: "metrics"
    type: "file"
    formats: ["csv"]
environment:
  conda:
    channels: ["conda-forge"]
    packages: ["python>=3.10"]
hardware:
  cpu_cores_min: 2
  memory_gb_min: 4
  gpu: false
model_weights:
  required: false
  sources: []
execution:
  local:
    command: "example-tool analyze --structure {inputs.structure} --out {outputs_dir}"
expected_runtime:
  small_example: "1-5 min"
examples:
  - name: "small example"
validation:
  dry_run_command: "example-tool --help"
safety_notes:
  - "Review commands before execution."
limitations:
  - "Accuracy depends on input quality."
```

## Validation levels

1. Schema validation: YAML parses and matches the JSON Schema.
2. Metadata validation: license, citation, authors, and links exist.
3. Command validation: command template renders without missing variables.
4. Environment validation: Conda/Docker/Apptainer instructions are syntactically valid.
5. Dry run: `--help` or version command succeeds.
6. Smoke test: tiny example input produces expected files.
7. Reproducibility check: input hashes, command, environment, tool versions, and output hashes are recorded.

## Review process

Use `docs/manifest-review-checklist.md` before moving a manifest beyond schema validation.

The short rule is:

```text
Famous project is not enough. A manifest advances only when the required evidence exists.
```

For protocol-level changes, use `docs/protocol-change-process.md`.

## Installation policy

v0.1 should not auto-install arbitrary code without explicit user approval.

Recommended flow:

1. Read manifest.
2. Show dependencies, license, hardware, model weights, and command templates.
3. Let user choose Conda, Docker, Apptainer, or existing system install.
4. Run environment dry-run.
5. Mark status as `ready`, `missing`, `partial`, or `unsupported`.
6. Never download model weights without showing source, license, and checksum.

## Contents

- `schema/opensciflow-plugin.schema.json`
- `examples/mdanalysis-trajectory-analysis/opensciflow.yaml`
- `examples/gromacs-md-stability/opensciflow.yaml`
- `examples/proteinflux-dynamics/opensciflow.yaml`
- `examples/diffdock-docking/opensciflow.yaml`
- `examples/boltz-structure-prediction/opensciflow.yaml`
- `examples/proteinmpnn-sequence-design/opensciflow.yaml`
- `examples/mace-interatomic-potential/opensciflow.yaml`
- `docs/diffdock-review-notes.md`
- `docs/model-manifest-review-notes.md`
- `docs/model-manifest-backlog.md`
- `docs/manifest-review-checklist.md`
- `docs/protocol-change-process.md`
- `docs/protocol-roadmap.md`
- `docs/readiness-levels.md`
- `docs/agent-contract.md`
- `docs/design-principles.md`
- `docs/license-and-citation.md`
- `docs/security-model.md`
- `ISSUES.md`
- `MILESTONES.md`

## Non-goals

- Replacing upstream documentation.
- Replacing package managers such as Conda, Spack, or Bioconda.
- Replacing workflow engines such as Nextflow, Snakemake, CWL, AiiDA, or Parsl.
- Certifying scientific correctness of a model/tool.
