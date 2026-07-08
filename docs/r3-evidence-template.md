# R3 environment and command-template evidence template

R3 means environment information and reviewed command templates are available.

R3 does not mean the tool has run successfully. It only means an agent can inspect requirements and prepare a reviewed execution plan without inventing shell commands.

## Evidence file location

For a plugin example, place the evidence file next to the manifest:

```text
examples/<plugin-name>/r3-env-command-evidence.md
```

## Required evidence

```yaml
plugin_name:
manifest_version:
readiness_before: R2
readiness_after: R3
checked_at:
reviewer:

environment_spec:
  conda:
  conda_lock:
  dockerfile:
  apptainer_def:
  system_packages:
  hpc_modules:
  notes:

command_templates:
  local:
  slurm:
  reviewed_wrapper:
  allowed_placeholders:

metadata_checks:
  inputs_declared:
  outputs_declared:
  license_declared:
  citation_declared:
  model_weights_declared:
  limitations_declared:

limitations:
  - "R3 does not prove the tool can run."
  - "R3 does not reduce execution trial-and-error cost by itself."
```

## Review checks

Before marking a manifest or capsule as R3:

- Environment requirements must be explicit enough to attempt a smoke test.
- Reviewed command templates or reviewed wrapper metadata must exist.
- Command placeholders must reference declared fields.
- Known missing values such as `to-be-filled` must remain visible.
- Required license, citation, model-weight, safety, and limitation metadata must be present.

## Next levels

- R4 requires a smoke test that passed in one recorded environment.
- R5 requires an example run and run record.
- R6 requires multi-environment pass/fail evidence.
- R7 requires external reproduction evidence.
