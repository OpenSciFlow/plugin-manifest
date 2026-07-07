# Required vs optional fields

This page defines the v0.1 boundary between fields that every `opensciflow.yaml` manifest must expose and fields that can remain optional or tool-specific.

The purpose is not to make every scientific tool look identical. The purpose is to make a local agent able to inspect the tool, explain what is known, block unsafe execution, and produce a useful run record.

## Rule

If a field affects local execution, scientific interpretation, citation, licensing, reproducibility, or user approval, v0.1 treats it as required.

Required does not mean the information must always be favorable or complete. It means the manifest must say what is known, what is not applicable, or what is still unknown.

For example:

- A tool without model weights should still declare `model_weights.required: false`.
- A tool with unknown weight checksums should record `checksum: "to-be-filled"` until reviewed.
- A tool without Slurm support can set `execution.slurm.supported: false` or omit the Slurm block.
- A tool whose data is supplied by the user should still set `license.data: "user-provided"`.

## Required top-level fields

| Field | Why it is required |
|---|---|
| `schema_version` | Allows validators and agents to select the right schema. |
| `name` | Provides a stable manifest identifier. |
| `version` | Separates manifest versions from upstream tool versions. |
| `domain` | Helps route scientific review and user expectations. |
| `task_types` | States what the manifest is allowed to do. |
| `description` | Gives a human-readable summary before execution. |
| `authors` | Records manifest/tool ownership or maintainer context. |
| `license` | Carries software, model-weight, and data license context into reports. |
| `citation` | Prevents uncited workflow outputs. |
| `inputs` | Lets the agent validate user-provided artifacts before execution. |
| `outputs` | Lets the agent know what files should exist after execution. |
| `environment` | Allows install/readiness checks before commands run. |
| `hardware` | Prevents misleading CPU/GPU/HPC expectations. |
| `model_weights` | Forces explicit handling of weights, sources, checksums, and download policy. |
| `execution` | Lists reviewed command templates. |
| `expected_runtime` | Helps users decide whether a run is plausible. |
| `examples` | Gives reviewers and users at least one intended use case. |
| `validation` | Defines dry-run or smoke-test evidence. |
| `safety_notes` | Captures execution and scientific safety boundaries. |
| `limitations` | Prevents over-interpretation of outputs. |

## Optional or conditional fields

| Field | When to use |
|---|---|
| `execution.slurm` | Required only when a manifest claims HPC/Slurm support. |
| `environment.docker` | Use when a reviewed Docker image or build path exists. |
| `environment.apptainer` | Use when an Apptainer/Singularity image path exists. |
| `validation.smoke_test` | Use after a tiny public example can actually run. |
| `parameters` | Use for bounded runtime parameters referenced by command templates. |
| `citation.doi` | Use when a DOI is available. |
| `citation.notes` | Use for citation edge cases such as optional model variants. |
| `expected_runtime.typical` | Use when there is enough evidence for a normal-size estimate. |

## Local-agent interpretation

A local agent should treat missing required fields as a blocking manifest error.

It should treat placeholder values such as `to-be-filled`, `to-be-reviewed`, or `to-be-confirmed` as review warnings. These values are acceptable in draft manifests, but they should block automatic execution unless the user explicitly accepts the uncertainty.

## Schema status

The JSON Schema enforces the basic v0.1 required-field boundary. The Python validator adds additional protocol checks that are easier to express procedurally, including command-template placeholder validation and stricter license/citation propagation when model weights are required.
