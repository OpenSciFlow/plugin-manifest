# Manifest review checklist

Use this checklist when reviewing an `opensciflow.yaml` plugin manifest.

The goal is not to certify scientific correctness. The goal is to decide whether a local agent can inspect the tool/model, explain the risks to a user, and avoid executing unreviewed commands.

## Review outcome

Use one of these outcomes:

| Outcome | Meaning |
|---|---|
| `needs-scope` | The manifest describes too broad a task or the plugin boundary is unclear. |
| `needs-metadata` | Required metadata is missing or too vague. |
| `schema-ready` | The manifest passes schema validation but is not reviewed for execution. |
| `metadata-reviewed` | License, citation, inputs, outputs, environment, weights, and limitations have been reviewed. |
| `dry-run-ready` | A documented dry run can be executed without private data or model downloads. |
| `smoke-test-ready` | A tiny example can run and produce expected files. |

## 1. Scope

- Is this manifest for one tool/model/script, not a whole research project?
- Is the supported task narrow enough for a local agent to describe accurately?
- Are unsupported tasks explicitly out of scope?
- Does the description avoid claiming validation, discovery, efficacy, or clinical meaning?

## 2. Upstream evidence

- Is the canonical repository or documentation page clear?
- Are upstream installation instructions linked or summarized accurately?
- Are release/version assumptions visible?
- If the manifest was written by OpenSciFlow maintainers, is it marked as a draft?

## 3. Inputs and outputs

- Are required inputs listed with concrete formats?
- Are optional inputs clearly marked as optional?
- Are output files named by type and format, not just "results"?
- Are output interpretations bounded by the tool's actual purpose?

## 4. Environment and hardware

- Are Conda, Docker, Apptainer, or system dependencies described enough for review?
- Are CPU, memory, GPU, and accelerator requirements explicit?
- Is local execution separated from Slurm/HPC execution?
- Are remote services disclosed if the tool may call one?

## 5. Model weights and data

- Does the manifest say whether model weights are required?
- Are weight source, license, version, and checksum recorded where available?
- If checksums are unavailable, is the reason documented?
- Does the manifest avoid silent model/data download?

## 6. Command templates

- Does every executable command come from a reviewed template?
- Are placeholders limited to declared inputs, outputs, parameters, and output directories?
- Does the command avoid shell pipes, redirects, subshells, network calls, and arbitrary user-provided fragments unless explicitly reviewed?
- Is there a dry-run command such as `--help`, `--version`, or a non-destructive validation command?

## 7. License and citation

- Are software, model-weight, and data licenses separated?
- Is the preferred citation or DOI included?
- Are generated reports expected to carry citations forward?
- Are license conflicts or unknown terms called out rather than hidden?

## 8. Safety and limitations

- Are safety notes specific to the tool/model, not generic boilerplate?
- Are scientific limitations specific enough to prevent common misuse?
- For chemistry, biology, medicine, or clinical-adjacent workflows, does the manifest clearly forbid efficacy, toxicity, diagnostic, or clinical claims from computational output alone?

## 9. Readiness mapping

Map the manifest to the lowest valid readiness level:

- `R1` if it only passes schema validation.
- `R2` if metadata has been reviewed.
- `R3` if a dry run works in a documented environment.
- `R4` if a smoke test works with tiny public input.
- `R5` if execution writes a complete run record.
- `R6` if the manifest is used inside a tested workflow template.

Do not advance a manifest because it is famous or useful. Advance it only when the evidence exists.
