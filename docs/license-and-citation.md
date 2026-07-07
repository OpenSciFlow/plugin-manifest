# License and citation policy

Plugin manifests do not override upstream software, model, weight, or data licenses.

## Required license fields

Each manifest should declare:

- software license;
- model weight license, if applicable;
- example data license, if applicable.

If any license is unclear, the plugin status should be `metadata-incomplete`, not `ready`.

The validator now checks the minimum propagation fields:

- `license.software`;
- `license.data`;
- `citation.preferred`;
- `license.model_weights` when model weights are required;
- `model_weights.sources[*].license` when model weights are required;
- `model_weights.sources[*].checksum` when model weights are required.

## Citation propagation

Generated OpenSciFlow reports should include citations from every plugin used in the run.

At minimum, a plugin should provide:

- preferred citation text;
- DOI when available;
- URL to upstream citation instructions or paper.

Run records and reports should not collapse citations into prose. Keep them as structured fields first, then render them into user-facing reports.

## Propagation rule

When a workflow uses a plugin, the local agent should carry these fields forward:

| Manifest field | Destination |
|---|---|
| `citation.preferred` | approval summary, run record, report |
| `citation.url` | run record, report references |
| `license.software` | approval summary, run record |
| `license.model_weights` | approval summary, run record |
| `license.data` | run record, report data note |
| `limitations` | approval summary, run record, report |
| `safety_notes` | approval summary and warnings |

If any required propagation field is missing, execution should be blocked or downgraded to review-only.

## Sensitive use cases

For hospital, pharma, or commercial use, non-commercial model weights or unclear licenses should be blocked or surfaced as strong warnings before execution.
