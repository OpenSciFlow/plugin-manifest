# HPC and Slurm metadata

OpenSciFlow v0.1 should describe HPC execution requirements without pretending to replace Slurm, environment modules, site policies, or workflow engines.

The goal is to make a local agent ask the right questions before submitting work to a cluster.

## Manifest fields to review

For a plugin that supports Slurm, the manifest should record:

```yaml
execution:
  slurm:
    supported: true
    submit_command: "sbatch {run_directory}/job.sbatch"
    reviewed_wrapper:
      path:
      review_status:
      reviewed_by:
      allowed_arguments:
        - run_directory
        - account
        - partition
        - time_limit
        - cpu_cores
        - memory_gb
        - gpu_resources
        - module
    recommended:
      partition:
      account:
      time_limit:
      nodes:
      tasks:
      cpu_cores:
      memory_gb:
      gpu_resources:
      constraint:
      modules:
        - 
      environment_variables:
        - name:
          value_policy:
      launcher:
      notes:
```

Use `null` or omit site-specific values when they cannot be portable. Do not hard-code a private cluster account, username, or filesystem path.

## Field naming convention

OpenSciFlow uses normalized resource names in manifests, workflow templates, skill execution requests, and run records:

| OpenSciFlow field | Slurm option usually rendered by wrapper |
|---|---|
| `account` | `#SBATCH --account` |
| `partition` | `#SBATCH --partition` |
| `time_limit` | `#SBATCH --time` |
| `cpu_cores` | `#SBATCH --cpus-per-task` for single-task jobs |
| `memory_gb` | `#SBATCH --mem` |
| `gpu_resources` | `#SBATCH --gres` or site-specific GPU option |
| `modules` / `module` | `module load ...` |

The reviewed wrapper is responsible for translating normalized fields into site-specific Slurm options.

## Required review questions

- Does the tool need MPI, OpenMP, CUDA, ROCm, oneAPI, or CPU-only execution?
- Does it require environment modules before Conda, Apptainer, or Docker?
- Is the recommended `time` based on a tiny smoke test, a typical run, or a large production run?
- Are GPU requirements expressed as optional, required, or unsupported?
- Does execution require shared filesystem paths?
- Are temporary directories and output directories safe for cluster policy?
- Are model weights or sample data expected to be staged before submission?
- Can the dry run be executed on a login node, or must it run as a Slurm job?
- Is the Slurm wrapper reviewed, and are its fillable arguments explicitly listed?

Detailed reviewed-wrapper field rules:

- `docs/reviewed-wrapper-fields.md`

## Safety boundaries

An OpenSciFlow-compatible agent should not:

- submit a job without showing the rendered Slurm options to the user;
- invent an account, partition, or module name;
- run a wrapper script that is not declared and reviewed in the manifest;
- submit jobs that download model weights without approval;
- write outside the approved work directory;
- treat Slurm submission success as scientific validation.

## Run-record expectations

When a workflow runs under Slurm, the run record should capture:

- Slurm job id;
- rendered `sbatch` options;
- submitted script path;
- stdout and stderr log paths;
- exit status;
- modules loaded;
- container image or Conda environment;
- node, GPU, CPU, memory, and walltime information when available.

## First review targets

Start with:

- `gromacs-md-stability`
- `mace-interatomic-potential`
- `diffdock-docking`

These cover CPU trajectory analysis, molecular simulation/HPC conventions, GPU inference, and model-weight staging.
