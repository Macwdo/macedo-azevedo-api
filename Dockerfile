FROM python:3.12.0-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY . /app

WORKDIR /app
RUN uv sync --frozen --no-cache
RUN chmod +x /app/scripts/command.sh

ENV PATH="/scripts:/venv/bin:$PATH"

CMD ["/app/scripts/command.sh"]
