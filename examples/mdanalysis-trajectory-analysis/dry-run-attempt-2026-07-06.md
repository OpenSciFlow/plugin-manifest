# MDAnalysis dry-run attempt, 2026-07-06

This is a failed dry-run attempt. It is useful readiness evidence, but it does not move the manifest to R3.

## Summary

```yaml
plugin_name: mdanalysis-trajectory-analysis
manifest_version: 0.1.0
readiness_before: R2
readiness_after: R2
checked_at: "2026-07-06T19:33:53.9521230+08:00"
reviewer: OpenSciFlow maintainers

environment:
  platform: "Windows-11-10.0.26200-SP0"
  architecture: "AMD64"
  python_version: "Python 3.13.5"
  python_executable: "C:\\Users\\lkn\\anaconda3\\python.exe"
  installation_route: "existing local Python environment"
  container_image: null
  conda_environment: "base environment path not recorded"

command:
  declared_dry_run_command: "python -c \"import MDAnalysis as mda; print(mda.__version__)\""
  rendered_command: "python -c \"import MDAnalysis as mda; print(mda.__version__)\""
  working_directory: "C:\\Users\\lkn\\Desktop\\OpenSciFlow"
  exit_code: 1

output:
  stdout: ""
  stderr: |
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
        import MDAnalysis as mda; print(mda.__version__)
        ^^^^^^^^^^^^^^^^^^^^^^^^
    ModuleNotFoundError: No module named 'MDAnalysis'
  log_path: null

limitations:
  - "This failed attempt only shows that MDAnalysis is missing from the current local environment."
  - "It does not test the Conda installation route."
  - "It does not test trajectory loading or scientific outputs."
```

## Next action

Create or select an environment that contains MDAnalysis, then repeat the dry-run command and record passing evidence with exit code `0`.
