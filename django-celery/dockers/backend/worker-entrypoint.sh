#!/bin/sh

until cd /app/backend
do
    echo "Waiting for server volume..."
done

### concurrency is for the number of workers
celery -A backend worker --loglevel=info --concurrency 1 -E
