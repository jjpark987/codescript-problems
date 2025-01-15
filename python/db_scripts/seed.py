import json
import os
import re
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# Function to convert file into json data
def parse_file(file_path) -> Dict[str, str]:
    try:
        # Open file as 'read'
        with open(file_path, 'r') as file:
            content = file.read()

        # Extract the comment block
        comment_block = re.search(r'("""[\s\S]*?""")', content)
        if not comment_block:
            raise ValueError("No comment block found")
        comment = comment_block.group().strip('"""').strip()

        # Define patterns for each field
        patterns = {
            'category': r'category:\s*(.*)',
            'subcategory': r'subcategory:\s*(.*)',
            'difficulty': r'difficulty:\s*(.*)',
            # 'image_url_e1': r'image_url_e1:\s*(?:.*/)?([\w_]+_e1\.png)',
            # 'image_url_e2': r'image_url_e2:\s*(?:.*/)?([\w_]+_e2\.png)',
            # 'image_url_e3': r'image_url_e3:\s*(?:.*/)?([\w_]+_e3\.png)',
            'title': r'title:\s*(.*)',
            'description': r'description:\s*((.|\n)+?)\n\nExample',
            'example1': r'Example 1:\s*((.|\n)+?)(Example 2:|$)',
            'example2': r'Example 2:\s*((.|\n)+?)(Example 3:|Constraints:|$)',
            'example3': r'Example 3:\s*((.|\n)+?)(Constraints:|$)',
            'constraints': r'Constraints:\s*((.|\n)+?)$'
        }

        example_patterns = {
            'input': r'Input:\s*(.*)',
            'output': r'Output:\s*(.*)',
            'explanation': r'Explanation:\s*((.|\n)+)'
        }

        # Extract information using regex patterns
        parsed_data = {}
        examples = []
        for field, pattern in patterns.items():
            match = re.search(pattern, comment)
            if match:
                # Create an example dictionary for each example content
                example = {}
                example_content = match.group(1)

                # Loop through each part (input, output, explanation) and apply pattern
                for part, part_pattern in example_patterns.items():
                    part_match = re.search(part_pattern, example_content)
                    if part_match:
                        example[part] = part_match.group(1).strip()
                
                # Add the example dictionary to the examples list
                examples.append(example)
                
                    # content = re.sub(r'^\s*/python/images/.+\n\n', '', content)
                # if field.startswith('image_url'):
                #     file_name = match.group(1)
                #     if file_name.lower() == 'none':
                #         parsed_data[field] = None
                #     else:
                #         parsed_data[field] = f'https://storage.googleapis.com/code-problem-images/{file_name}'
                # elif field.startswith('example'):
                #     example_content = match.group(1)
                #     example_content = re.sub(r'^\s*/python/images/.+\n\n', '', example_content)
                #     parsed_data[field] = example_content.strip()
                # else:
                #     parsed_data[field] = match.group(1)
            else:
                parsed_data[field] = None

        # Convert to JSON and return
        json_data = json.dumps(parsed_data, indent=4)
        return json_data
    
    except Exception as e:
        print(f'Error occurred: {e}')

# Function to store this in database CRUD

# Test parse.py on main.py
if __name__ == '__main__':
    file_path = 'python/main.py'
    data = parse_file(file_path)
    if data:
        print(data)
