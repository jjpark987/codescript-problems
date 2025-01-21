import json
import os
import re
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Function to convert file into json data
def parse_file(file_path: str) -> Dict[str, str]:
    try:
        # Open file as 'read'
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract the comment block
        comment_block = re.search(r'(""".*?""")', content, re.DOTALL)        
        if not comment_block:
            raise ValueError('No comment block found')
        comment = comment_block.group()[3:-3].strip()

        # Define patterns for each field
        patterns = {
            'category': r'category:\s*(.*?)\n',
            'subcategory': r'subcategory:\s*(.*?)\n',
            'difficulty': r'difficulty:\s*(.*?)\n',
            'image_url_e1': r'image_url_e1:\s*(.*?)\n',
            'image_url_e2': r'image_url_e2:\s*(.*?)\n',
            'image_url_e3': r'image_url_e3:\s*(.*?)\n',
            'title': r'title:\s*(.*?)\n',
            'description': r'description:\s*((?:.|\n)+?)\n\nExample',
            'constraints': r'Constraints:\s*((?:.|\n)+?)$'
        }

        DIFFICULTY_MAP = {'easy': 1, 'medium': 2, 'hard': 3}
        BASE_IMAGE_URL = 'https://storage.googleapis.com/code-problem-images/'

        parsed_data = {'examples': []} 

        # Extract information using regex patterns
        for field, pattern in patterns.items():
            match = re.search(pattern, comment, re.DOTALL)
            if match:
                value = match.group(1).strip()

                if field.startswith('image_url'):
                    parsed_data[field] = None if value.lower() == 'none' else f'{BASE_IMAGE_URL}{value.split('/')[-1]}'
                elif field == 'difficulty':
                    parsed_data[field] = DIFFICULTY_MAP.get(value.lower(), None)  # Convert to int
                else:
                    parsed_data[field] = value
            else:
                parsed_data[field] = None

        # Extract and structure examples
        example_pattern = re.findall(
            r'Example \d+:\s*Input:\s*(.*?)\s*Output:\s*(.*?)\s*Explanation:\s*((?:.|\n)+?)(?=Example \d+:|Constraints:|$)',
            comment, re.DOTALL
        )
        
        parsed_data['examples'] = [
            {'input': ex[0].strip(), 'output': ex[1].strip(), 'explanation': ex[2].strip()}
            for ex in example_pattern
        ]

        # Convert to JSON and return
        return json.dumps(parsed_data, indent=4)
    
    except Exception as e:
        print(f'Error occurred: {e}')
        return None

# Function to store this in database CRUD

# Test parse.py on main.py
if __name__ == '__main__':
    file_path = 'python/main.py'
    data = parse_file(file_path)
    if data:
        print(data)
