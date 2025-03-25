from argparse import ArgumentParser
from asyncio import run
from os import rename, path
from re import search, findall, sub, IGNORECASE
from python.scripts.db.post_problems import find_all_problem_files

IMAGE_DIR = 'python/images'

parser = ArgumentParser(description='Rename problems based on their title.')
parser.add_argument('--all', action='store_true', help='Rename all problem files.')
parser.add_argument('--file', type=str, help='Rename specific problem file(s).')
args = parser.parse_args()

async def rename_image_by_title(file_path: str):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            title_match = search(r'title:\s*(.*?)\n', content, IGNORECASE)

            if not title_match:
                print(f'❌ No title found in "{file_path}". Skipping.')
                return
            
            image_matches = findall(r'image_path_(e\d+):\s*(?:.*/)?([^/\s]+)', content, IGNORECASE) 

            if not image_matches or image_matches and image_matches[0][1].lower() == 'none':
                print(f'ℹ️ No images found in "{file_path}". Skipping.')
                return

        title = title_match.group(1).strip()
        sanitized_title = sub(r'[^a-zA-Z0-9\s]', '', title)
        snake_case_title = sub(r'\s+', '_', sanitized_title.strip().lower())
        
        rename_map = {}

        for suffix, old_image_name in image_matches:
            if old_image_name.lower() == 'none':
                break
            
            new_image_name = f'{snake_case_title}_{suffix}.png'
            rename_map[old_image_name] = new_image_name

        def replace_match(match):
            key = match.group(1)  
            old_filename = match.group(2)  
            new_filename = rename_map.get(old_filename, old_filename)  
            return f'{key}: {new_filename}' 

        updated_content = sub(r'(image_path_e\d+):\s*(?:.*/)?([^/\s]+)', replace_match, content)
        
        with open(file_path, 'w') as file:
            file.write(updated_content)
            print(f'✅ Updated image references in "{file_path}".')

        for old_image_name, new_image_name in rename_map.items():
            old_path = path.join(IMAGE_DIR, old_image_name)
            new_path = path.join(IMAGE_DIR, new_image_name)

            if path.exists(new_path):
                print(f'🚨 Image "{new_image_name}" already exists. Skipping.')
                continue

            if not path.exists(old_path):
                print(f'❌ Old image "{old_image_name}" not found. Skipping.')
                continue

            rename(old_path, new_path)

    except FileNotFoundError:
        print(f'❌ File not found: {file_path}')
    except PermissionError:
        print(f'❌ Permission denied: Cannot rename {file_path}')
    except Exception as e:
        print(f'❌ Unexpected error with file "{file_path}": {e}')

async def main() -> None:
    if args.all:
        print('▶️ Renaming all images...')
        problem_files = find_all_problem_files()
        for path in problem_files:
            print(f'Processing {path}...')
            await rename_image_by_title(path)
    elif args.file:
        print('▶️ Renaming image...')
        file_paths = [path.strip('"').strip("'") for path in args.file.split(',')]
        for path in file_paths:
            print(f'Processing {path}...')
            await rename_image_by_title(path)
    else:
        print('🚨 No file path passed as argument. Exiting.')
        return

if __name__ == '__main__':
    run(main())
    