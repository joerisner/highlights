FROM ghcr.io/astral-sh/uv:python3.13-alpine

WORKDIR /app

COPY pyproject.toml .

RUN uv sync

COPY . .

EXPOSE 3000

CMD ["uv", "run", "fastapi", "run", "--port", "3000", "src/main.py"]
