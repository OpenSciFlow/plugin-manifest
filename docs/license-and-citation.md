# License and citation policy

Plugin manifests do not override upstream software, model, weight, or data licenses.

## Required license fields

Each manifest should declare:

- software license;
- model weight license, if applicable;
- example data license, if applicable.

If any license is unclear, the plugin status should be `metadata-incomplete`, not `ready`.

## Citation propagation

Generated OpenSciFlow reports should include citations from every plugin used in the run.

At minimum, a plugin should provide:

- preferred citation text;
- DOI when available;
- URL to upstream citation instructions or paper.

## Sensitive use cases

For hospital, pharma, or commercial use, non-commercial model weights or unclear licenses should be blocked or surfaced as strong warnings before execution.

