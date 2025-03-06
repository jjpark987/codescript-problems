from argparse import ArgumentParser
from asyncio import run
from dotenv import load_dotenv
from google.cloud.storage import Client
from os import getenv, listdir, path, environ
from typing import List

load_dotenv()

# Argument parser
parser = ArgumentParser(description='Upload images to Google Cloud Storage')
parser.add_argument('--all', action='store_true', help='Upload all images.')
parser.add_argument('--file', type=str, help='Upload specific image(s).')
args = parser.parse_args()

# Global variables
ROOT_DIR = 'python/images/'
GCP_CREDENTIALS = getenv('GCP_CREDENTIALS')
GC_BUCKET_NAME = getenv('GC_BUCKET_NAME')

# Function to find all images
def find_image_files() -> List[str]:
    image_files = []

    for file in listdir(ROOT_DIR):
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
            image_files.append(path.join(ROOT_DIR, file))

    return image_files

# Function to upload a single image to Google Cloud Storage
async def upload_image(file_path: str) -> None:
    if not GCP_CREDENTIALS:
        print('❌ GCP_CREDENTIALS is not set. Check your environment variables.')
        return
    if not GC_BUCKET_NAME:
        print('❌ GC_BUCKET_NAME is not set. Check your environment variables.')
        return

    print(GCP_CREDENTIALS, GC_BUCKET_NAME)
    try:
        with open('/tmp/gcp_credentials.json', 'w') as cred_file:
            cred_file.write(GCP_CREDENTIALS)

        environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/tmp/gcp_credentials.json'
        
        bucket = Client().get_bucket(GC_BUCKET_NAME)
        blob = bucket.blob(file_path)
        
        if not blob.exists():
            blob.upload_from_filename(file_path)
            print(f'✅ Uploaded {file_path} to Google Cloud Storage.')
        else:
            print(f'⏭️ Skipping over duplicate image: {file_path}')
    except Exception as e:
        print(f'🚨 Unexpected error while uploading {file_path}: {e}')

async def main() -> None:
    if args.all:
        print('▶️ Uploading all images to Google Cloud Storage...')
        problem_files = find_image_files()
        for path in problem_files:
            print(f'Processing {path}...')
            await upload_image(path)
    elif args.file:
        print('▶️ Uploading images in IMAGE_FILES_PATHS....')
        file_paths = [path.strip() for path in args.file.split() if path.strip()]
        for path in file_paths:
            print(f'Processing {path}...')
            await upload_image(path)
    else:
        print('🙅‍♂️ No image file path passed as argument. Exiting.')
        return

if __name__ == '__main__':
    run(main())
