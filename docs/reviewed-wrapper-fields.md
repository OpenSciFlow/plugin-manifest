# Reviewed wrapper fields

This page defines the minimum fields for a Slurm reviewed-wrapper declaration in a plugin manifest.

It applies when a manifest declares:

```yaml
execution:
  slurm:
    submit_command: "sbatch {run_directory}/job.sbatch"
    reviewed_wrapper:
      ...
```

Manifests may still include ordinary Slurm `recommended` metadata without claiming a reviewed wrapper. A manifest becomes reviewed-wrapper-ready only when both `submit_command` and `reviewed_wrapper` are present and valid.

## Required fields

```yaml
execution:
  slurm:
    supported: true
    submit_command: "sbatch {run_directory}/job.sbatch"
    reviewed_wrapper:
      path: "wrappers/tool-name.sbatch"
      review_status: "reviewed"
      reviewed_by: "OpenSciFlow maintainers"
      allowed_arguments:
        - run_directory
        - account
        - partition
        - time_limit
        - cpu_cores
        - memory_gb
        - module
    recommended:
      account: null
      partition: null
      time_limit: "01:00:00"
      cpu_cores: 4
      memory_gb: 16
      module: "tool/1.0"
```

## Validator checks

`scripts/validate_manifests.py` checks that:

- `submit_command` exists when `reviewed_wrapper` is declared;
- `reviewed_wrapper.path` is non-empty;
- `reviewed_wrapper.review_status` is exactly `reviewed`;
- `reviewed_wrapper.reviewed_by` is non-empty;
- `reviewed_wrapper.allowed_arguments` is a non-empty list;
- `allowed_arguments` contains `run_directory`;
- `allowed_arguments` has no duplicates;
- each non-`run_directory` argument is also declared under `execution.slurm.recommended`.

## Agent rule

A local agent may render or submit a Slurm wrapper only after the wrapper declaration passes these checks and the user approves the rendered command, resources, paths, logs, citations, limitations, and run directory.
