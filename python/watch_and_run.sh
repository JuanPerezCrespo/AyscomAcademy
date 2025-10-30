#!/bin/bash

INPUT_DIR="incoming"
PROCESSED_DIR="processed"
mkdir -p "$PROCESSED_DIR"

# Watch for new files every 60 seconds
while true; do
  for file in "$INPUT_DIR"/*.csv; do
    if [ -f "$file" ]; then
      echo "Processing $file..."
      python3 clean_and_save.py "$file"
      mv "$file" "$PROCESSED_DIR"/
    fi
  done
  sleep 60
done
