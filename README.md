# CodeScript Problems

This repository contains the code problems for CodeScript.

- [codescript-backend](https://github.com/jjpark987/codescript-backend)
- [codescript-frontend](https://github.com/jjpark987/codescript-frontend)

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

### Renaming Problems

- To rename a problem

```zsh
python -m python.scripts.repo.rename_problems --file "python/main.py"
```

- To rename all problems

```zsh
python -m python.scripts.repo.rename_problems --all
```

### Renaming Images

- To rename an image

```zsh
python -m python.scripts.repo.rename_images --file "python/main.py"
```

- To rename all images

```zsh
python -m python.scripts.repo.rename_images --all
```

## Docker

- Build image, create container, and activate in the foreground

```zsh
docker compose up --build --abort-on-container-exit
```

## GitHub Action

1. Verify Docker Desktop is running in the background

2. Verify GitHub Runner from ~/actions-runner is running in the background

- Verify runner from ~/actions-runner

```zsh
cd ~/Projects/codescript/codescript-runner && ./svc.sh status
```

- Start runner from ~/actions-runner

```zsh
cd ~/Projects/codescript/codescript-runner && ./svc.sh start
```

3. Add new files to python/problems/ and images/ to trigger GitHub Action workflow
