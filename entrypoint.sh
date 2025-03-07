#!/bin/bash

if [[ -n "$PROBLEM_FILES_PATHS" ]]; then
  echo "📥 Processing problem files into post_problems.py: $PROBLEM_FILES_PATHS..."
  python -m python.scripts.db.post_problems --file "$PROBLEM_FILES_PATHS"
else
  echo "✅ No problem files provided"
fi

if [[ -n "$IMAGE_FILES_PATHS" ]]; then
  echo "🖼️ Processing images into upload_images.py: $IMAGE_FILES_PATHS..."
  python -m python.scripts.db.upload_images --file "$IMAGE_FILES_PATHS"
else
  echo "✅ No images to upload"
fi
