FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS builder

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

FROM python:3.13-slim-bookworm AS runtime

WORKDIR /app

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PATH="/app/.venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y --no-install-recommends gosu && \
    addgroup --system --gid 1001 appgroup && \
    adduser --system --uid 1001 --gid 1001 appuser && \
    mkdir -p logs && \
    chown appuser:appgroup logs && \
    chmod 755 logs && \
    mkdir -p logs /app/migrations/versions && \
    chown -R appuser:appgroup /app/migrations/versions && \
    chmod 755 /app/migrations/versions && \
    rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
RUN sed -i 's/\r$//' /entrypoint.sh && \
    chmod +x /entrypoint.sh

COPY migrations /app/migrations
COPY alembic.ini /app/alembic.ini
COPY --from=builder /app/.venv /app/.venv
COPY locales/ ./locales
COPY bot/ ./bot

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "-m", "bot"]