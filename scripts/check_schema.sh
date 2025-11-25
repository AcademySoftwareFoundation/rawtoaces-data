#!/usr/bin/env bash

error=0

for DIR in camera cmf illuminant training; do
    for FILE in ./data/$DIR/*; do
        echo "Processing file $FILE"
        if ! check-jsonschema --schemafile ./schema_1.0.0.json $FILE; then
            error=1
        fi
    done
done

exit $error
