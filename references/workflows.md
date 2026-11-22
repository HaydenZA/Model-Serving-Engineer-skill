# Workflows

## Existing repository repair
1. Protect state: record commit, branch and dirty files; create a branch/worktree when allowed.
2. Inventory with `scripts/repo_inventory.py`.
3. Reproduce using the smallest documented build/test path.
4. Minimize the failure and identify the owning layer.
5. Add a failing regression test.
6. Implement the smallest architecture-consistent fix using full replacement files.
7. Run focused tests, then broader tests.
8. Run API/correctness/performance checks affected by the change.
9. Document commands, evidence, risk and rollback.
10. Stop at approval gates.

## Modernization
1. Freeze observable API, model output and benchmark baselines.
2. Identify seams and characterize current behavior with tests.
3. Refactor in reversible stages.
4. Compare outputs and performance after each stage.
5. Remove old paths only after parity is demonstrated.

## Backend or platform port
1. Build a capability matrix and define unsupported features explicitly.
2. Add compile-time and runtime feature detection.
3. Implement reference CPU behavior first when absent.
4. Add backend kernels behind a narrow interface.
5. Add numerical parity tests and backend-specific CI.
6. Test startup failure and fallback behavior on unsupported hardware.
7. Document toolchain, drivers, runtime libraries and minimum versions from measured evidence.

## Greenfield runtime
1. Write acceptance matrix and architecture decision record.
2. Scaffold API, configuration, health, logging and test harness.
3. Implement tokenizer/model inspection and a reference CPU execution path.
4. Add one model family and one format end to end.
5. Add streaming, cancellation, scheduling and bounded memory.
6. Add accelerator backends incrementally behind tested interfaces.
7. Add packaging, containers and orchestration.
8. Validate correctness before optimization.
9. Benchmark representative workloads.
10. Produce operations, security and rollback documentation.

## Optimization
1. Profile first with platform-native tools.
2. State a falsifiable bottleneck hypothesis.
3. Record baseline and variance.
4. Change one material factor at a time.
5. Verify correctness envelope.
6. Measure cold and warm behavior.
7. Keep only improvements that survive repeated runs and realistic workloads.
