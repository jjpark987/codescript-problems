#!/bin/bash

echo "PROBLEM_FILES_PATHS: $PROBLEM_FILES_PATHS"

# Check if PROBLEM_FILES_PATHS has data
if [ -n "$PROBLEM_FILES_PATHS" ]; then
  echo "CHECKING FOR DATABASE URL"
  docker exec codescript-fastapi env | grep DOCKER_DATABASE_URL
  echo "📥 Processing problem files into parse_and_post.py: $PROBLEM_FILES_PATHS..."
  python python/db_scripts/parse_and_post.py --file "$PROBLEM_FILES_PATHS"
else
  echo "❌ No problem files provided. Exiting script..."
fi

# To keep container running
# tail -f /dev/null
