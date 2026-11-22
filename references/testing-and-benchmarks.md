# Testing and benchmarks

## Mandatory test layers
- Unit: tokenizer boundaries, config parsing, sampling, cache accounting, shape/dtype checks.
- Golden: fixed model revision, prompt, seed and expected tokens/logits or tolerance.
- API: validation, errors, authentication, streaming, disconnect, cancellation and usage.
- Integration: load, infer, unload/reload, concurrent requests and graceful shutdown.
- Resource: OOM handling, bounded queues, file descriptors, threads, GPU memory and cache eviction.
- Packaging: clean machine/container installation and startup.
- Security: secret leakage, path traversal, unsafe model metadata, oversized inputs and untrusted templates.

## Required model matrix
Use small test fixtures where possible, then at least one representative real model per claimed family/format. Cover dense and MoE if claimed, quantized and unquantized where supported, short and long context, batch 1 and concurrent load.

## Benchmark method
Record:
- commit and dirty state;
- model repository, exact revision, format, quantization and hashes;
- OS, kernel, architecture, CPU/RAM, accelerator(s), driver and runtime;
- compiler, flags and dependency lock;
- server flags, context, batch, parallelism and cache settings;
- prompt/completion token distributions;
- warm-up count, measured iterations, variance and failures.

Report at minimum:
- time to first token p50/p95/p99;
- inter-token latency p50/p95/p99;
- prompt processing tokens/s;
- generation tokens/s per request and aggregate;
- requests/s and goodput under a stated SLO;
- peak host and accelerator memory;
- model load and readiness time;
- queue time, cancellation latency and error rate.

Never compare projects using different models, revisions, tokenizers, quantizations, contexts or quality envelopes without highlighting the mismatch.
