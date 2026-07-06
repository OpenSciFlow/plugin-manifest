# Model manifest backlog

This backlog prioritizes scientific models that may become OpenSciFlow plugin manifests.

Status:

```text
Planning document. Inclusion here does not mean the model is ready to run through OpenSciFlow.
```

## Priority A: manifest drafts already exist

| Model/tool | Existing draft | Main unresolved issues |
|---|---|---|
| DiffDock | `examples/diffdock-docking/opensciflow.yaml` | model-weight retrieval, stable output artifacts, DiffDock vs DiffDock-L split |
| Boltz | `examples/boltz-structure-prediction/opensciflow.yaml` | Boltz-1 vs Boltz-2 split, MSA server disclosure, affinity-output warnings |
| ProteinMPNN | `examples/proteinmpnn-sequence-design/opensciflow.yaml` | weight files/checksums, design vs score-only modes, experimental-validation limitations |
| MACE | `examples/mace-interatomic-potential/opensciflow.yaml` | per-foundation-model licenses, applicability domain, element coverage, level of theory |

## Priority B: strong next manifest candidates

| Model/tool | Why next | Notes before drafting |
|---|---|---|
| CHGNet | Atomistic model with clear model/version/applicability metadata needs | Confirm license and model-weight terms first |
| MatterSim | Active atomistic model across elements, temperatures, and pressures | Record model coverage, device assumptions, and precision warnings |
| REINVENT4 | Clear generative chemistry workflow | Strong limitations needed around synthesis, toxicity, and experimental validation |
| AiZynthFinder | Clear retrosynthesis planning task | Useful report-boundary example for route feasibility |
| Protenix | Active biomolecular structure model | Need upstream correction on canonical metadata and execution assumptions |
| Nucleotide Transformer | Genomics/transcriptomics foundation model | Need model-card/license/sequence-task boundaries |

## Priority C: landscape/reference first

| Model/tool | Reason |
|---|---|
| OmegaFold | Useful historical/alternative structure-model reference |
| Uni-Fold | Structure-prediction platform reference |
| RoseTTAFold-All-Atom | Important but license/input-output metadata need careful review |
| LigandMPNN | Related to ProteinMPNN, but should wait until ProteinMPNN manifest is corrected |
| GNINA | Docking comparison target; first finish DiffDock and classical docking manifests |
| EquiBind | Research-code docking reference |
| TorchDrug | Broad toolkit, likely multiple manifests rather than one |
| GT4SD | Broad generative-science toolkit |
| GuacaMol | Benchmark/evaluation reference rather than execution manifest |
| MolBART | Archived historical reference |
| Recursion GFlowNet | Generative library; needs task-specific scope before manifest |
| AI2BMD | Promising but scientifically heavier than current MVP |
| JMP | Archived historical atomistic model reference |
| Google DeepMind materials_discovery | Need clearer reusable workflow boundary |
| MatCalc | Downstream library/workflow target rather than standalone model |
| M3GNet | Archived/historical materials model reference |

## Required fields before a model can be marked ready

- exact model family and version;
- model-weight URL and checksum;
- model-weight license;
- code license;
- citation for code and selected weights;
- input schema and example input;
- expected output artifacts;
- runtime environment;
- hardware requirements;
- dry-run command;
- smoke-test command and tiny input;
- applicability-domain statement;
- explicit scientific limitations;
- remote-service disclosure, if any;
- cache/download location and cleanup policy.
