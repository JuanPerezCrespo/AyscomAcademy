#!/bin/bash

FOLDER="data"
OUTPUT="output/cleaned.csv"

python3 process_data.py "$FOLDER" "$OUTPUT"
