import argparse
import asyncio
import glob
import httpx
import os
import re
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

# Global variables
ROOT_DIR = 'python/problems/'
CATEGORIES = ['data_manipulations', 'combinatorics', 'optimizations']
PATTERNS = {
    'subcategory': r'subcategory:\s*(.*?)\n',
    'difficulty': r'difficulty:\s*(.*?)\n',
    'image_url_e1': r'image_url_e1:\s*(.*?)\n',
    'image_url_e2': r'image_url_e2:\s*(.*?)\n',
    'image_url_e3': r'image_url_e3:\s*(.*?)\n',
    'title': r'title:\s*(.*?)\n',
    'description': r'description:\s*((?:.|\n)+?)\n\nExample',
    'constraints': r'Constraints:\s*((?:.|\n)+?)$'
}
SUBCATEGORY_MAP = {
    "reformatting": 1,
    "reducing": 2,
    "counting": 3,
    "generating": 4,
    "strings": 5,
    "arrays": 6,
    "structures": 7,
    "heaps": 8,
    "processes": 9
}
DIFFICULTY_MAP = {
    'easy': 1, 
    'medium': 2, 
    'hard': 3
}
BASE_IMAGE_URL = 'https://storage.googleapis.com/code-problem-images/'

# Function to check if we are inside a docker container
def is_running_in_docker() -> bool:
    return os.path.exists('/.dockerenv') or os.path.exists('/run/.containerenv')

API_URL = f'{os.getenv("DOCKER_API_BASE_URL")}/problems' if is_running_in_docker() else f'{os.getenv("API_BASE_URL")}/problems'
HEADERS = { 'Content-Type': 'application/json' }

# Argument parser to accept file path
parser = argparse.ArgumentParser(description='Parse and post problem files.')
parser.add_argument('--all', action='store_true', help='Process all problem files')
parser.add_argument('--file', type=str, help='Path to the newly added problem file')
args = parser.parse_args()

# Function to find all Python problem files in the subcategories
def find_problem_files() -> List[str]:
    problem_files = []

    for category in CATEGORIES:
        category_path = os.path.join(ROOT_DIR, category)
        files = glob.glob(os.path.join(category_path, '**', '*.py'), recursive=True)
        problem_files.extend(files)

    return problem_files

# Function to parse file into json data
def parse_file(file_path: str) -> Dict[str, str]:
    try:
        with open(file_path, 'r') as file:
            content = file.read()

        comment_block = re.search(r'(""".*?""")', content, re.DOTALL)        
        if not comment_block:
            raise ValueError('No comment block found')
        comment = comment_block.group()[3:-3].strip()

        parsed_data = {'examples': [], 'image_urls': []}

        # Extract information using regex PATTERNS and update image_urls
        for field, pattern in PATTERNS.items():
            match = re.search(pattern, comment, re.DOTALL)
            if match:
                value = match.group(1).strip()

                if field.startswith('image_url'):
                    if value.lower() != 'none':
                        parsed_data['image_urls'].append(f'{BASE_IMAGE_URL}{value.split("/")[-1]}')
                elif field == 'difficulty':
                    parsed_data[field] = DIFFICULTY_MAP.get(value.lower(), None)
                else:
                    parsed_data[field] = value
            else:
                parsed_data[field] = None

        # Convert subcategory to subcategory_id
        if parsed_data.get('subcategory'):
            parsed_data['subcategory_id'] = SUBCATEGORY_MAP.get(parsed_data.pop('subcategory'), None)

        # Extract and structure examples
        example_pattern = re.findall(
            r'Example \d+:\s*Input:\s*(.*?)\s*Output:\s*(.*?)(?:\s*Explanation:\s*((?:.|\n)+?))?(?=Example \d+:|Constraints:|$)',
            comment, re.DOTALL
        )

        parsed_data['examples'] = [
            {
                'input': ex[0].strip(), 
                'output': ex[1].strip(), 
                'explanation': ex[2].strip() if ex[2] else ""
            }
            for ex in example_pattern
        ]

        print(f'✅ Successfully parsed: {file_path}')
        return parsed_data
    
    except Exception as e:
        print(f'🚨 Error parsing {file_path}: {e}')

# Function to store this in database
async def post_problem(json_data: Dict[str, str]) -> None:
    print(f"🔍 API_URL: {API_URL}")
    print(f"✅ API_URL is correctly set: {API_URL == 'http://app:80/problems'}")

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.post(API_URL, json=json_data, headers=HEADERS)

        if response.status_code == 201:
            print(f'✅ Successfully posted problem: {json_data["title"]}')
            print('Response:', response.json())  
        elif response.status_code == 400:
            print('❌ Subcategory not found.')
        elif response.status_code == 409:
            print(f'⏭️ Skipping over duplicate problem: {json_data["title"]}')
        else:
            print(f'❌ Failed to post problem: {response.status_code}')

    except httpx.RequestError as e:
        print(f'🚨 Error sending request: {e}')

# Main function
async def main() -> None:
    if args.all:
        print('▶️ Executing parse and post on all problems.')
        problem_files = find_problem_files()
        for path in problem_files:
            print(f'Processing {path}...')
            data = parse_file(path)
            await post_problem(data) if data else print(f'❌ No valid problem data extracted from: {path}')
    else:
        if args.file:
            print('▶️ Executing parse and post on problem_files_paths.')
            file_paths = args.file.split(',')
            print(file_paths)
            for path in file_paths:
                print(f'Processing {path}...')
                data = parse_file(path)
                await post_problem(data) if data else print(f'❌ No valid problem data extracted from: {path}')
        else:
            print('▶️ Executing parse and post on main.py.')
            path = '/python/main.py'
            print(f'Processing {path}...')
            data = parse_file(path)
            await post_problem(data) if data else print(f'❌ No valid problem data extracted from: {path}')

# Run script
if __name__ == '__main__':
    asyncio.run(main())
