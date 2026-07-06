# Model manifest review notes

This note collects review questions for the first model-focused OpenSciFlow manifests.

Status:

```text
Drafts for correction, not stable execution profiles.
```

## Boltz

Manifest:

```text
examples/boltz-structure-prediction/opensciflow.yaml
```

Upstream:

```text
https://github.com/jwohlwend/boltz
```

Initial facts captured:

- `boltz predict <INPUT_PATH> [OPTIONS]` is the primary prediction command.
- YAML input is preferred; FASTA is supported but deprecated upstream.
- `--out_dir` controls output location.
- `--cache` defaults to `~/.boltz` and may use `BOLTZ_CACHE`.
- `--use_msa_server` can generate MSA remotely and may require authentication.
- Output includes predicted structures, confidence JSON, optional affinity JSON, PAE/PDE/pLDDT files, and processed inputs.
- Upstream README states that code and weights are MIT licensed.

Review questions:

1. Should Boltz-1 and Boltz-2 be separate OpenSciFlow manifests?
2. Which model identifier/version should a run record store by default?
3. Which output files should be considered stable artifacts?
4. How should MSA server use be disclosed before execution?
5. Which affinity-output warnings should appear in generated reports?

## ProteinMPNN

Manifest:

```text
examples/proteinmpnn-sequence-design/opensciflow.yaml
```

Upstream:

```text
https://github.com/dauparas/ProteinMPNN
```

Initial facts captured:

- `protein_mpnn_run.py` is the primary execution script.
- Main input can be a PDB backbone.
- The tool supports design, scoring, conditional probabilities, tied positions, fixed positions, and amino-acid biases.
- Output examples include FASTA-style designed sequences with score, global score, model name, git hash, seed, and sampling temperature.
- GitHub metadata reports MIT license for the repository.

Review questions:

1. Which model-weight files and versions should be recorded?
2. Which outputs are stable artifacts across common runs?
3. Should design and score-only modes be separate manifests?
4. Which validation boundaries should be shown before a user interprets a designed sequence?
5. What license statement should OpenSciFlow use for model weights?

## MACE

Manifest:

```text
examples/mace-interatomic-potential/opensciflow.yaml
```

Upstream:

```text
https://github.com/ACEsuit/mace
```

Initial facts captured:

- `mace_eval_configs --configs ... --model ... --output ...` is the basic evaluation command.
- `mace-torch` is the PyPI package name.
- MACE supports CPU, CUDA, and other device modes depending on environment.
- Upstream README says MACE code is MIT licensed.
- Foundation models can have different licenses and target domains.
- Model metadata may include elements covered, training dataset, level of theory, target system, model size, release source, and license.

Review questions:

1. Should each foundation model family get a separate OpenSciFlow manifest?
2. Which model metadata fields are required before marking a MACE model `ready`?
3. How should per-model license differences be represented?
4. Which applicability-domain warnings should be shown before execution?
5. Which citations should be attached to code vs selected model weights?
