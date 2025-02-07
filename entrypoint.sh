#!/bin/bash

echo "PROBLEM_FILES_PATHS: $PROBLEM_FILES_PATHS"

echo "🔍 Debugging Environment Variables..."
echo "DOCKER_API_BASE_URL: $DOCKER_API_BASE_URL"
echo "PROBLEM_FILES_PATHS: $PROBLEM_FILES_PATHS"

# Install curl if not present
# if ! command -v curl &> /dev/null
# then
#     echo "📦 Installing curl..."
#     apt update && apt install -y curl
# fi

# # Ensure FastAPI (`app:80`) is reachable before proceeding
# echo "🔍 Checking if FastAPI is reachable at app:80..."
# if curl -s -o /dev/null -w "%{http_code}" http://app:80/docs | grep -q "200"; then
#     echo "✅ FastAPI is reachable!"
# else
#     echo "❌ FastAPI is NOT reachable! Exiting..."
#     exit 1
# fi

# Check if PROBLEM_FILES_PATHS has data
if [ -n "$PROBLEM_FILES_PATHS" ]; then
  echo "📥 Processing problem files into parse_and_post.py: $PROBLEM_FILES_PATHS..."
  python python/db_scripts/parse_and_post.py --file "$PROBLEM_FILES_PATHS"
else
  echo "❌ No problem files provided. Exiting script..."
fi

# tail -f /dev/null
