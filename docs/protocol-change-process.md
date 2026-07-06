# Protocol change process

OpenSciFlow is still a draft protocol. Changes should be easy to propose, but they should not silently break existing manifests or encourage unsafe agent behavior.

## When to propose a protocol change

Open a protocol change issue when a reviewer finds that:

- a required field is missing from the schema;
- a field is too vague for safe local execution;
- a workflow needs metadata that does not fit the current manifest;
- license, citation, model-weight, remote-service, or limitation metadata cannot be represented cleanly;
- command rendering needs a stricter rule.

Small wording fixes and manifest-specific corrections do not need the protocol-change process.

## Required sections

A protocol change proposal should include:

1. Problem: the concrete review or execution problem.
2. Proposed field or rule: the exact addition or change.
3. Example: one minimal YAML snippet.
4. Agent impact: what a local agent must do differently.
5. Backward compatibility: whether existing manifests remain valid.
6. Risk: what could go wrong if the field or rule is misused.

## Decision rule for v0.1

Prefer fields that make assumptions visible over fields that automate behavior.

For example:

- Good: disclose remote service use.
- Good: require model-weight source and license.
- Risky: automatically download and execute a remote install script.
- Risky: let an LLM generate command-line flags that are not in the manifest.

## Versioning

Use patch-level manifest version changes for corrections to a single manifest.

Use schema version changes only when the JSON Schema or agent contract changes:

- `opensciflow.plugin/v0.1`: reviewable metadata.
- `opensciflow.plugin/v0.2`: executable command-template contract.
- `opensciflow.plugin/v0.3`: workflow/HPC interoperability.

## Review expectations

A protocol change should be reviewed by at least:

- one manifest reviewer;
- one workflow reviewer if the change affects workflow templates;
- one security-minded reviewer if the change affects command execution, downloads, remote services, or filesystem access.

If no reviewer is available, keep the proposal as a draft and do not change the schema.
