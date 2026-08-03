FROM ghcr.io/astral-sh/uv:python3.14-alpine

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --locked

COPY . .

EXPOSE 3000

CMD ["uv", "run", "fastapi", "run", "--port", "3000", "src/main.py"]
