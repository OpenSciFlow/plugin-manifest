# DiffDock manifest review notes

Target manifest:

```text
examples/diffdock-docking/opensciflow.yaml
```

Upstream repository:

```text
https://github.com/gcorso/DiffDock
```

Verification date:

```text
2026-07-05
```

## Facts captured from upstream README

- The repository contains DiffDock and now runs DiffDock-L by default.
- The upstream README gives Conda setup through `environment.yml`.
- A Dockerfile is provided and a pre-built Docker image is listed as `rbgcsail/diffdock`.
- Inference can use a single protein and ligand, or a batch CSV.
- Protein input can be a `.pdb` file or a sequence.
- Ligand input can be a SMILES string or an RDKit-readable file such as `.sdf` or `.mol2`.
- GPU is recommended; CPU can run some PDB-input cases but is slower.
- The README states that code and model weights are MIT licensed.
- DiffDock confidence scores are not binding affinity predictions.
- The model is intended for small-molecule docking to proteins, not broad biomolecular interaction prediction.

## Open questions for maintainers

1. Is the `diffdock-docking` plugin name and task classification accurate?
2. Should OpenSciFlow distinguish `diffdock-original` and `diffdock-l` as separate manifests?
3. What is the best way to represent model weight retrieval and checksums?
4. Which output files should a minimal wrapper treat as stable public artifacts?
5. Is the example smoke test based on `data/protein_ligand_example.csv` appropriate?
6. Are there additional license or citation notes that should be shown before execution?

## Safety boundary for OpenSciFlow

OpenSciFlow should describe this as a docking-pose prediction workflow. It must not claim binding affinity, drug efficacy, clinical usefulness, or validated biological function from the generated poses.
