#!/bin/bash

# Check if PROBLEM_FILES_PATHS has data
if [[ -n "$PROBLEM_FILES_PATHS" && "$PROBLEM_FILES_PATHS" != '""' ]]; then
  echo "📥 Processing problem files into post_problems.py: $PROBLEM_FILES_PATHS..."
  cd "$(git rev-parse --show-toplevel)" || exit 1
  python -m python.scripts.db.post_problems --file "$PROBLEM_FILES_PATHS"
else
  echo "❌ No problem files provided. Exiting script..."
fi
