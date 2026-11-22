# Completion report

Use this structure:

## Outcome
State what was created, fixed or validated and the exact revision/artifact.

## Evidence
List build, test and benchmark commands with pass/fail results. Distinguish executed from recommended commands.

## Compatibility matrix
List each claimed OS, architecture, backend, framework, format and API route as Passed, Failed, Not run or Not applicable. Never convert Not run into Supported.

## Files
Provide complete created/changed files or a downloadable repository/archive. Do not provide only patches when full files were requested.

## Performance
Include reproducible workload and environment, central values and percentiles, variance and correctness envelope.

## Security and operations
State bind/auth defaults, secret handling, health/readiness, metrics, shutdown, deployment and rollback.

## Known limitations
List gaps and untested combinations directly.

## Approval checkpoint
State pending merge, release or production actions. Do not imply they were performed.
