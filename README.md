# Qwen3.6-35B-A3B GB10 image mirror

This repository owns the signing workflow for the public container mirror used
by [Approaching-AI/qwen36-gb10-highspeed](https://github.com/Approaching-AI/qwen36-gb10-highspeed).

The mirror is byte-for-byte identical to the candidate measured on Test15:

```text
ghcr.io/rjckkkkk/qwen36-gb10@sha256:d4e9505469af37e7c65b83a8e9a6b3025173ab9836366443eacee2dbf0493ae7
```

Pull it anonymously:

```bash
docker pull ghcr.io/rjckkkkk/qwen36-gb10@sha256:d4e9505469af37e7c65b83a8e9a6b3025173ab9836366443eacee2dbf0493ae7
```

Verify the personal mirror signature:

```bash
cosign verify \
  --certificate-identity \
  "https://github.com/rjckkkkk/qwen36-gb10-mirror/.github/workflows/candidate.yml@refs/heads/main" \
  --certificate-oidc-issuer \
  "https://token.actions.githubusercontent.com" \
  ghcr.io/rjckkkkk/qwen36-gb10@sha256:d4e9505469af37e7c65b83a8e9a6b3025173ab9836366443eacee2dbf0493ae7
```

This repository does not contain or redistribute model weights. Reproduction
uses the model sources and pinned revisions documented by the canonical source
repository.
