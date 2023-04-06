#!/bin/bash

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done

echo "$(date) - Rabbit is up and running."

until nc -z ${MONGODB_HOST} ${MONGODB_PORT}; do
    echo "$(date) - waiting for mongodb..."
    sleep 1
done

echo "$(date) - MongoDB is up and running."


nameko run --config config.yml rdf_builder.service