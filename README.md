# CodeScript Problems

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

## Scripts

### Posting Problems to Database

- Make sure codescript-fastapi is running

- To parse and post /python/main.py

```zsh
python -m python.scripts.db.post_problems
```

- To parse and post a problem

```zsh
python -m python.scripts.db.post_problems --file "python/problems/combinatorics/counting/new_problem.py"
```

- To parse and post all problems in problems/

```zsh
python -m python.scripts.db.post_problems --all
```

### Uploading Images to Google Cloud Storage

- To upload an image

```zsh
python -m python.scripts.db.upload_images --file "python/images/new_image.png"
```

- To upload all images

```zsh
python -m python.scripts.db.upload_images --all
```

### Renaming files

- To rename a file

```zsh
python -m python.scripts.repo.rename_files --file "python/problems/combinatorics/counting/new_problem.py"
```

- To rename all files in problems/

```zsh
python -m python.scripts.repo.rename_files --all
```

## Docker

### Commands

- Build image and create container in the foreground

```zsh
docker compose up --build
```

- List all containers

```zsh
docker ps -a
```

- Prune all stopped containers

```zsh
docker container prune -f
```

## GitHub Action

### Pre-workflow

1. Make sure Docker Desktop is running in the background

2. Make sure GitHub Runner from ~/actions-runner is running in the background

- Verify runner from ~/actions-runner

```zsh
cd ~/actions-runner && ./svc.sh status
```

- Start runner from ~/actions-runner

```zsh
cd ~/actions-runner && ./svc.sh start
```

3. Add new files to python/problems/ and images/ to trigger GitHub Action workflow
