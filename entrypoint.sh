#!/bin/bash

# Check if PROBLEM_FILES_PATHS has data
if [ -n "$PROBLEM_FILES_PATHS" ]; then
  # If there are files listed in PROBLEM_FILES_PATHS, pass them as arguments
  echo "📥 Processing problem files into parse_and_post.py: $PROBLEM_FILES_PATHS..."
  python python/db_scripts/parse_and_post.py --file "$PROBLEM_FILES_PATHS"
else
  # If PROBLEM_FILES_PATHS is empty or null, run parse_and_post.py without arguments
  echo "❌ No problem files provided, running parse_and_post.py with no arguments..."
  python python/db_scripts/parse_and_post.py
fi
