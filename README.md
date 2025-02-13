# CodeScript

This repository contains the code problems for CodeScript.

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL server

### Installation

1. Clone the repository

```zsh
git clone git@github.com:jjpark987/codescript-db.git
```

2. Create a virtual environment if there isn't one already

```zsh
python -m venv .venv
```

3. Activate virtual environment

```zsh
source .venv/bin/activate
```

4. Install dependencies

```zsh
pip install -r requirements.txt
```

## Seeding Database

- Make sure MySQL database is set up and migrated with the latest migration

- To parse and post all problems

```zsh
python python/db_scripts/parse_and_post.py --all
```

- To parse and post a specific file path

```zsh
python python/db_scripts/parse_and_post.py --file "python/problems/combinatorics/counting/new_problem.py"
```

- To parse and post /python/main.py

```zsh
python python/db_scripts/parse_and_post.py
```

## Uploading to Google Cloud Storage

- To upload all images

```zsh
python python/db_scripts/upload_images.py --all
```

- To upload a single image

```zsh
python python/db_scripts/upload_images.py --file "python/images/new_image.png"
```

## Docker

- Build and run containers in the foreground

```zsh
docker compose up
```

- Stop and remove containers

```zsh
docker compose down
```

- Check container status

```zsh
docker ps
```
