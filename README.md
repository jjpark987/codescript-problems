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

2. Seed database

```zsh
python python/db_scripts/seed.py
```
