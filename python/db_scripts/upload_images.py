import argparse
import asyncio
import os
from dotenv import load_dotenv
from google.cloud import storage
from typing import List

load_dotenv()

# Argument parser to accept image paths
parser = argparse.ArgumentParser(description='Upload images to Google Cloud Storage')
parser.add_argument('--all', action='store_true', help='Upload all images.')
parser.add_argument('--file', type=str, help='Comma-separated list of image paths to upload')
args = parser.parse_args()

# Function to find all images
def find_image_files() -> List[str]:
    ROOT_DIR = 'python/images/'
    image_files = []

    for file in os.listdir(ROOT_DIR):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            image_files.append(os.path.join(ROOT_DIR, file))

    return image_files

# Function to upload a single image to Google Cloud Storage
async def upload_image(file_path: str) -> None:
    GCP_CREDENTIALS = os.getenv('GCP_CREDENTIALS')

    if not GCP_CREDENTIALS:
        print('❌ GCP_CREDENTIALS is not set. Check your environment variables.')
        return

    with open('/tmp/gcp_credentials.json', 'w') as cred_file:
        cred_file.write(GCP_CREDENTIALS)

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp_credentials.json'

    client = storage.Client()

    GC_BUCKET_NAME = os.getenv('GC_BUCKET_NAME')
    if not GC_BUCKET_NAME:
        print('❌ GC_BUCKET_NAME is not set. Check your environment variables.')
        return
    
    print(f'✅ Using bucket: {GC_BUCKET_NAME}')
    bucket = client.get_bucket(GC_BUCKET_NAME)

    blob = bucket.blob(file_path)
    if blob.exists():
        print(f'❌ File {file_path} already exists in the bucket. Skipping upload.')
    else:
        try:
            blob.upload_from_filename(file_path)
            print(f'✅ Uploaded {file_path} to Google Cloud Storage.')
        except Exception as e:
            print(f'❌ Failed to upload {file_path}: {e}')

# Main function
async def main() -> None:
    if args.all:
        print('▶️ Executing upload images on all images.')
        problem_files = find_image_files()
        for path in problem_files:
            print(f'Processing {path}...')
            await upload_image(path)
    else:
        if args.file:
            print('▶️ Executing upload images on image_files_paths.')
            file_paths = args.file.split(',')
            for path in file_paths:
                print(f'Processing {path}...')
                await upload_image(path)
        else:
            print('No file path passed as argument to upload_image(). Exiting.')
            return

# Run script
if __name__ == '__main__':
    asyncio.run(main())
