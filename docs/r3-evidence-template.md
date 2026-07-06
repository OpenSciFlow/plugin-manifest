# R3 dry-run evidence template

R3 means a manifest can run its declared dry-run command in a documented environment.

R3 does not mean the tool has produced scientific outputs. It only means the manifest is executable enough for a local agent to check readiness without running a full workflow.

## Evidence file location

For a plugin example, place the evidence file next to the manifest:

```text
examples/<plugin-name>/r3-dry-run-evidence.md
```

## Required evidence

```yaml
plugin_name:
manifest_version:
readiness_before: R2
readiness_after: R3
checked_at:
reviewer:

environment:
  platform:
  architecture:
  python_version:
  installation_route:
  container_image:
  conda_environment:

command:
  declared_dry_run_command:
  rendered_command:
  working_directory:
  exit_code:

output:
  stdout:
  stderr:
  log_path:

limitations:
  - "Dry-run evidence does not validate scientific correctness."
  - "Dry-run evidence does not prove the full workflow can run."
```

Use `null` for fields that do not apply, and add a short note explaining why.

## Review checks

Before marking a manifest as R3:

- The command must be declared in `validation.dry_run_command`.
- The command must not require private data, large model weights, or expensive compute.
- The output must show a version, help text, import success, or equivalent readiness signal.
- The exit code must be `0`.
- The environment must be specific enough for another contributor to reproduce the check.
- Known limitations must remain visible in the manifest and the evidence file.

## What to avoid

- Do not mark a manifest as R3 because the upstream project is famous.
- Do not mark a manifest as R3 from documentation alone.
- Do not include private paths, tokens, API keys, or user-specific credentials.
- Do not treat `--help` success as proof that a scientific workflow is correct.

## Next levels

After R3:

- R4 requires a tiny public smoke-test input and expected output files.
- R5 requires a validated run record with hashes, commands, versions, citations, and limitations.
- R6 requires use inside a tested workflow template and report generation.
