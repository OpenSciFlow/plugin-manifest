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
- Are placeholder values such as `to-be-filled`, `to-be-reviewed`, or `to-be-confirmed` treated as review warnings rather than silent approval?

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
- If model weights are required, do all weight sources include license and checksum fields?
- Are license, citation, limitations, and safety notes expected to propagate into run records and reports?

## 8. Safety and limitations

- Are safety notes specific to the tool/model, not generic boilerplate?
- Are scientific limitations specific enough to prevent common misuse?
- For chemistry, biology, medicine, or clinical-adjacent workflows, does the manifest clearly forbid efficacy, toxicity, diagnostic, or clinical claims from computational output alone?

## 9. Readiness mapping

Map the manifest or capsule to the lowest valid readiness level:

- `R1` if it is only a draft manifest.
- `R2` if it passes schema validation.
- `R3` if environment specs and reviewed command templates are present.
- `R4` if a smoke test passes in one recorded environment.
- `R5` if an example run passes and writes a run record.
- `R6` if multiple environments have recorded pass/fail evidence.
- `R7` if an external user or machine reproduces it.

Do not advance a manifest because it is famous or useful. Advance it only when the evidence exists.

## 10. Required-field boundary

- Does the manifest include every field listed in `docs/required-vs-optional-fields.md`?
- Does each required field provide useful information, or explicitly say `not-applicable`, `user-provided`, `unknown`, or `to-be-filled`?
- Are optional fields used only when the manifest claims that capability?
- If Slurm support is claimed, does `execution.slurm` include enough scheduler metadata for review?
