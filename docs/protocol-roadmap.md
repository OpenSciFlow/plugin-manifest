# Protocol roadmap

OpenSciFlow should evolve from readable metadata into an executable contract for local-first AI for Science agents.

## Current status

`opensciflow.plugin/v0.1` is a draft schema for public review. It is useful for describing tools and models, but it is not yet strict enough to be treated as a fully executable protocol.

## Design target

The protocol should let a local agent answer five questions before running anything:

1. What tool or model is allowed to run?
2. What exact inputs, environment, weights, hardware, and licenses are required?
3. What command template may be rendered?
4. What files and metadata must be produced?
5. What scientific claims are explicitly out of scope?

## v0.1: Reviewable Metadata

Goal:

```text
Make tool/model assumptions visible and correctable.
```

Required capabilities:

- parse YAML;
- validate required fields;
- record inputs, outputs, environment, execution, citations, licenses, safety notes, and limitations;
- expose dry-run and smoke-test commands;
- keep examples small and reviewable.

Not required yet:

- automatic environment creation;
- full command-template type checking;
- real sample datasets for every manifest;
- runtime attestation;
- signed manifests.

## v0.2: Executable Contract

Goal:

```text
Let a local agent safely execute only reviewed command templates.
```

Required additions:

- typed input references;
- typed output references;
- command-template variable validation;
- explicit environment readiness states;
- model-weight retrieval policy;
- checksum requirements for sample inputs and model weights;
- clear local vs remote-service disclosure;
- required run-record fields;
- stricter validation levels.

Expected agent behavior:

- refuse unknown tasks;
- refuse missing required inputs;
- refuse unreviewed shell commands;
- show license, citation, model weights, remote services, hardware, and limitations before execution;
- write a run record after execution.

## v0.3: Interoperability Layer

Goal:

```text
Allow OpenSciFlow manifests to interoperate with workflow engines and HPC systems.
```

Candidate additions:

- export mapping to CWL / Nextflow / Snakemake where feasible;
- Slurm profile conventions;
- Apptainer image metadata;
- Conda lockfile support;
- structured provenance export;
- report-template metadata;
- manifest ownership and review status.

## v1.0: Stable Local-Agent Protocol

Goal:

```text
A stable protocol that local agents, workflow templates, and reviewed plugins can depend on.
```

Non-negotiable requirements:

- schema versioning and migration policy;
- required validation suite;
- stable run-record format;
- security review for command rendering;
- license/citation propagation;
- model-weight provenance;
- reproducibility record;
- explicit non-clinical / non-drug-efficacy claim boundary where relevant.

## Immediate priorities

1. Define readiness levels.
2. Define the agent execution contract.
3. Continue tightening JSON Schema for nested fields beyond input/output artifacts.
4. Review command-template validation against wrapper-script and workflow-engine cases.
5. Record reusable R3 dry-run evidence for at least one manifest.
6. Review Slurm/HPC metadata fields against real cluster workflows.
7. Align `R5` and `R6` readiness with the BioPilot run-record schema.
8. Convert the BioPilot MVP into a protocol compliance test.
