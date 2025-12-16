FROM python:3.11-slim AS base

COPY --from=ghcr.io/astral-sh/uv:0.8 /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen

FROM base AS final
COPY app ./app
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]