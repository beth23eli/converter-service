FROM python:3.11-slim

COPY --from=ghcr.io/astral-sh/uv:0.8 /uv /uvx /bin/

WORKDIR /app
COPY pyproject.toml uv.lock /app/
RUN uv sync --frozen

COPY app ./app
EXPOSE 8000

CMD ["uv", "run", "uvicorn", "app.main:create_app", "--host", "0.0.0.0", "--port", "8000"]