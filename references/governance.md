# Governance and safety

## Automatic, low-risk
- Read-only repository and environment inspection.
- Create local reports, tests and code in a new branch/worktree.
- Build and test in an isolated non-production environment.
- Run bounded benchmarks that cannot exhaust shared production resources.

## Explicit user enablement
- Provision or use OpenComputer.
- Download gated or large model weights.
- Use paid compute or cloud accelerators.
- Bind beyond loopback.
- Push a development branch when the user has authorized the target.

## External human approval required
- Merge or force-push.
- Publish tags, releases, packages, images or signed artifacts.
- Deploy to production or alter production traffic/configuration.
- Delete repositories, branches, weights, caches, releases, registries, deployments or persistent data.
- Execute migrations with irreversible state changes.
- Change licensing or redistribute restricted weights.

Approval must name the artifact/revision, target environment, action, rollback and approver. A prior general approval does not authorize a materially different release or production target.
