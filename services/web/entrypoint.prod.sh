#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for Cloud SQL instance..."

    while ! pg_isready -h "$DB_HOST" -p "$DB_PORT"; do
      sleep 0.1
    done

    echo "Cloud SQL instance is up"
fi

exec "$@"
