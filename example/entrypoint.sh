#!/bin/sh
set -e

if [ "$(id -u)" = "0" ]; then
    chown -R appuser:appgroup /app/logs /app/migrations/versions
    exec gosu appuser:appgroup "$@"
else
    if [ ! -w "/app/logs" ] || [ ! -w "/app/migrations/versions" ]; then
        echo "ERROR: Logs or migrations directory not writable" >&2
        exit 1
    fi
    exec "$@"
fi