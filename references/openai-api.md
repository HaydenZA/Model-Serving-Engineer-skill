# OpenAI-compatible API contract

Implement only routes that can be tested. Prefer:
- `GET /health` and `GET /ready` with no sensitive internals.
- `GET /v1/models`.
- `POST /v1/chat/completions`.
- `POST /v1/completions` when raw completion is supported.
- `POST /v1/embeddings` only for embedding-capable models.
- `POST /v1/responses` when implemented completely.

Requirements:
- JSON schema validation with bounded body, string, array and token limits.
- Bearer authentication for non-loopback binds; keys supplied by file/secret/environment, never argv or logs.
- Stable OpenAI-style error envelope and meaningful HTTP statuses.
- SSE streaming with `data:` frames, terminal `[DONE]`, disconnect cancellation and backpressure.
- Request IDs; optional client IDs must not replace server IDs.
- Correct `prompt_tokens`, `completion_tokens` and `total_tokens` from the runtime tokenizer.
- Model alias resolution without leaking filesystem paths.
- Idempotent cancellation and graceful shutdown with bounded drain time.
- Explicit policy for unsupported parameters; reject rather than silently ignore compatibility-sensitive fields.
- Tests for tools/function calling, JSON/structured output and multimodal input only when those capabilities are claimed.

Publish a compatibility statement listing tested SDK/client versions, endpoints, fields, streaming semantics and deviations.
