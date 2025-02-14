import os

# Function to check if we are inside a docker container
def is_running_in_docker() -> bool:
    return os.path.exists('/.dockerenv') or os.path.exists('/run/.containerenv')
