FROM ghcr.io/astral-sh/uv:python3.14-alpine

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --locked

COPY . .

EXPOSE 3000

# TODO: Figure out why ruff and ty are being installed when running the container.

CMD ["uv", "run", "--no-dev", "fastapi", "run", "--port", "3000", "src/main.py"]
