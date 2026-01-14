FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:0.8 /uv /uvx /bin/

WORKDIR /app


RUN useradd -m -u 10001 -s /bin/sh svcuser

ENV HOME=/home/svcuser
ENV UV_CACHE_DIR=/home/svcuser/.cache/uv
RUN mkdir -p /home/svcuser/.cache/uv && chown -R 10001:10001 /home/svcuser

COPY pyproject.toml uv.lock /app/

RUN chown -R 10001:10001 /app
USER 10001

RUN uv venv /app/.venv
RUN uv sync --frozen --no-dev

COPY --chown=10001:10001 app ./app

EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]