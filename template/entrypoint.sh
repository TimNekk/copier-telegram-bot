#!/bin/sh
set -e

if [ "$(id -u)" = "0" ]; then
    chown -R appuser:appgroup /app/logs
    exec gosu appuser:appgroup "$@"
else
    if [ ! -w "/app/logs" ]; then
        echo "ERROR: Logs directory not writable" >&2
        exit 1
    fi
    exec "$@"
fi