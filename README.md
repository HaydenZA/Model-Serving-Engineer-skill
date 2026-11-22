# Model Serving Engineer

## Purpose

The Model Serving Engineer skill creates, repairs, modernizes, ports, tests, benchmarks and secures AI inference and model-serving codebases. It supports both existing repositories and complete greenfield runtimes. The result must be able to run independently; external test providers are optional infrastructure rather than runtime dependencies.

## Use this skill for

- Diagnosing build, portability, correctness, API, memory or performance failures.
- Producing complete replacement files for an existing serving repository.
- Creating a new production-oriented inference server from requirements.
- Adding models, formats, quantization schemes, schedulers or accelerator backends.
- Implementing OpenAI-compatible APIs, streaming, cancellation and usage accounting.
- Building reproducible platform, correctness and performance test matrices.
- Preparing containers, Kubernetes manifests, packages, CI workflows and rollback documentation.

## Platforms and backends

- Linux, Windows and macOS.
- x86-64 and ARM64.
- Native builds, Docker, Podman and Kubernetes.
- CPU scalar and applicable AVX2, AVX-512, AMX, NEON and SVE paths.
- NVIDIA CUDA, cuBLAS, NCCL and TensorRT-LLM.
- AMD ROCm, HIP, rocBLAS and RCCL.
- Apple Metal and MLX.
- Vulkan and practical SYCL/oneAPI implementations.

## Frameworks and formats

The skill can work with llama.cpp and GGUF, Hugging Face Transformers, safetensors, PyTorch, ONNX Runtime, vLLM, SGLang, TensorRT-LLM, MLX, ONNX and custom C, C++, Rust, Go or Python engines. Projects such as OneKru, Strata, Basalt, Uzu and TensorFold are treated as architectural references only after the exact repository and revision are established.

## OpenAI-compatible API expectations

Supported implementations should use strict request validation, stable error envelopes, server-sent-event streaming, disconnect cancellation, bounded queues, backpressure, graceful shutdown, correct tokenizer-based usage accounting and explicit handling of unsupported parameters. Compatibility claims must identify exactly which endpoints and clients were tested.

## OpenComputer policy

OpenComputer is **disabled by default**. The user must explicitly enable it for the task. It may be used as an isolated Linux test provider when the model and required hardware fit the available environment. It cannot be used to claim Windows, macOS, Metal, ROCm or unavailable GPU compatibility. OpenComputer adapters belong in testing or infrastructure modules and must not become production runtime dependencies.

## Safety and approval

The skill may inspect repositories, generate local code, create tests and run bounded isolated builds automatically. Human approval is required before merging, force-pushing, tagging, releasing, publishing packages or images, signing artifacts, deploying to production, changing production traffic or deleting durable artifacts. Model and runtime licences must be evaluated separately.

## Typical workflow

1. Protect and inventory the repository or establish a greenfield acceptance matrix.
2. Reproduce the current failure or define a deterministic baseline.
3. Map the API, scheduler, tokenizer, loader, execution engine, cache and backend boundaries.
4. Add a regression or contract test before changing behavior.
5. Implement complete files using reproducible dependencies.
6. Validate correctness before measuring performance.
7. Test realistic prompt, batch, concurrency and context-length combinations.
8. Report tested and untested platform combinations separately.
9. Prepare build, run, deployment and rollback commands.
10. Stop at release and production approval gates.

## Example requests

- “Repair this MSVC build and return every changed file in full.”
- “Create an OpenAI-compatible GGUF server with CPU, CUDA and Metal backends.”
- “Add continuous batching and prove that token output remains within the defined correctness envelope.”
- “Benchmark time to first token, inter-token latency and aggregate throughput for this model revision.”
