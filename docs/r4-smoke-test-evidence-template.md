# R4 smoke-test evidence template

R4 means a capsule has passed a minimal smoke test in one documented environment.

R4 does not mean the full workflow has run. It only means a minimal version/import/help/tiny-input check passed in the recorded environment.

## Evidence file location

For a plugin example, place the evidence file next to the manifest:

```text
examples/<plugin-name>/r4-smoke-test-evidence.md
```

## Required evidence

```yaml
plugin_name:
manifest_version:
readiness_before: R3
readiness_after: R4
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
  declared_smoke_test_command:
  rendered_command:
  working_directory:
  exit_code:

output:
  stdout:
  stderr:
  log_path:

limitations:
  - "Smoke-test evidence does not validate scientific correctness."
  - "Smoke-test evidence does not prove the full workflow can run."
```

Use `null` for fields that do not apply, and add a short note explaining why.

## Review checks

Before marking a capsule as R4:

- The command must be declared in `validation.dry_run_command` or capsule smoke-test metadata.
- The command must not require private data, large model weights, or expensive compute.
- The output must show a version, help text, import success, or equivalent readiness signal.
- The exit code must be `0`.
- The environment must be specific enough for another contributor to reproduce the check.
- Known limitations and known failures must remain visible.

## What to avoid

- Do not mark a capsule as R4 because the upstream project is famous.
- Do not mark a capsule as R4 from documentation alone.
- Do not include private paths, tokens, API keys, or user-specific credentials.
- Do not treat `--help` success as proof that a scientific workflow is correct.

## Next levels

- R5 requires an example run and validated run record with hashes, commands, versions, citations, and limitations.
- R6 requires multi-environment pass/fail evidence.
- R7 requires external reproduction evidence.
