#!/usr/bin/env bash

for DIR in camera cmf illuminant training; do
    for FILE in ./data/$DIR/*; do
        echo "Processing file $FILE"
        check-jsonschema --schemafile ./schema_0.1.0.json $FILE
    done
done
