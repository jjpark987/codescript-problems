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

1. Make sure MySQL database is set up and migrated with the latest migration

2. To parse and post all problems

```zsh
python python/db_scripts/parse_and_post.py
```

## Docker

- Force build and run containers in the foreground

```zsh
docker compose up --build
```

- Build and run containers in the foreground

```zsh
docker compose up
```

- Build and run containers in background

```zsh
docker compose up -d
```

- Start previously stopped containers

```zsh
docker compose start
```

- Stop and remove containers

```zsh
docker compose down
```

- Stop containers without removing

```zsh
docker compose stop
```

- Restart containers in the background (compose down and up)

```zsh
docker compose restart
```

- Check container status

```zsh
docker ps
```
