#!/bin/sh
set -e


echo "✅ Postgres Database Started Successfully ($DB_HOST:$DB_PORT)"

echo "Collect static files"
uv run manage.py collectstatic --noinput

echo "Apply database migrations"
uv run manage.py migrate --noinput

echo "Starting server"
uv run gunicorn -c gunicorn.py core.wsgi:application
