#!/bin/bash

until nc -z ${RABBIT_HOST} ${RABBIT_PORT}; do
    echo "$(date) - waiting for rabbitmq..."
    sleep 1
done

cd ./rdf_builder/rdf_builder

nameko run --config /code/rdf_builder/rdf_builder/config.yml service