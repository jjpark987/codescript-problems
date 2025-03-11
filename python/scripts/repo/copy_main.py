from asyncio import run
from os import path, makedirs
from re import search, IGNORECASE
from python.scripts.repo.rename_problems import rename_problem_by_title
from shutil import copy

def copy_into_subcat():
    main_file_path = 'python/main.py'
    with open(main_file_path, 'r') as file:
        content = file.read()

        category_match = search(r'category:\s*(.*?)\n', content, IGNORECASE)
        if not category_match:
            print(f'❌ No category found in main.py')
            return
        category = category_match.group(1).strip().replace(' ', '_')
        print(category)

        subcategory_match = search(r'subcategory:\s*(.*?)\n', content, IGNORECASE)
        if not subcategory_match:
            print(f'❌ No subcategory found in main.py')
            return
        subcategory = subcategory_match.group(1).strip().replace(' ', '_')
        print(subcategory)
            
    new_directory = path.join('python', 'problems', category, subcategory)
    new_file_path = path.join(new_directory, 'main.py')

    makedirs(new_directory, exist_ok=True)
    copy(main_file_path, new_file_path)

    print(f'✅ main.py copied to: {new_file_path}')
    return new_file_path

async def main() -> None:
    path = copy_into_subcat()
    await rename_problem_by_title(path)

if __name__ == '__main__':
    run(main())
