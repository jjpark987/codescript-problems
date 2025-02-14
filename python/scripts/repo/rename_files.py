import asyncio
import argparse
import os
import re
from python.scripts.db.post_problems import find_all_problem_files

# Argument parser
parser = argparse.ArgumentParser(description='Rename files based on their problem title.')
parser.add_argument('--all', action='store_true', help='Rename all problem files.')
parser.add_argument('--file', type=str, help='Rename specific problem file(s).')
args = parser.parse_args()

# Function to rename file based on title
async def rename_file_by_title(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            match = re.search(r'title:\s*(.*?)\n', content, re.IGNORECASE)

            if not match:
                print(f'❌ No title found in "{file_path}". Skipping.')
                return
            
            title = match.group(1).strip()

        sanitized_title = re.sub(r'[^a-zA-Z0-9\s]', '', title)
        snake_case_title = re.sub(r'\s+', '_', sanitized_title.strip().lower()) + '.py'
        old_title = os.path.basename(file_path)

        if snake_case_title != old_title:
            current_dir = os.path.dirname(file_path)
            new_file_path = os.path.join(current_dir, snake_case_title)

            if not os.path.exists(new_file_path):
                os.rename(file_path, new_file_path)
                print(f'✅ Renamed "{old_title}" to "{snake_case_title}"')
            else:
                print(f'🚨 File "{snake_case_title}" already exists. Skipping rename.')
        else:
            print(f'ℹ️ File "{file_path}" is already correctly named.')

    except FileNotFoundError:
        print(f'🚨 File not found: {file_path}')
    except PermissionError:
        print(f'🚨 Permission denied: Cannot rename {file_path}')
    except Exception as e:
        print(f'🚨 Unexpected error with file "{file_path}": {e}')

async def main() -> None:
    if args.all:
        print('▶️ Renaming all problems...')
        problem_files = find_all_problem_files()
        for path in problem_files:
            print(f'Processing {path}...')
            await rename_file_by_title(path)
    elif args.file:
        print('▶️ Renaming problem...')
        file_paths = [path.strip('"').strip("'") for path in args.file.split(',')]
        for path in file_paths:
            print(f'Processing {path}...')
            await rename_file_by_title(path)
    else:
        print('🙅‍♂️ No file path passed as argument. Exiting.')
        return

if __name__ == '__main__':
    asyncio.run(main())
    