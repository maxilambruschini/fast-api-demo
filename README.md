# FastApi ORM demo

## Introduction

This project is merely a demo of how a backend service works when implementing api calls leveraging SQLAlchemy ORM communication with the database and Alembic for generating migrations

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them.

- Python 3.12+
- Pip
- A virtual environment (optional, but recommended)

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository:
    ```bash
    git clone https://github.com/maxilambruschini/fast-api-demo.git
    ```

2. Change into the project directory:
    ```bash
    cd fast-api-demo
    ```

3. (Optional) Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.\venv\Scripts\activate`
    ```

4. Install the requirements:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Database Server with Docker

To start the database server using Docker, follow these steps:

1. Change into the Docker directory:
    ```bash
    cd docker
    ```

2. Run the Docker Compose command:
    ```bash
    docker-compose up
    ```

This will start the database server in a Docker container. Make sure Docker is running on your machine before executing these commands. Also make sure the database has finished startup before running the application

## Connecting to the Database Server

After starting the database server with Docker, you can connect to it using the following details:

- **Server name:** `localhost`
- **Port:** This is specified in your `.env` file. If left untouched, it will be `1433`.
- **Authentication type:** SQL Login
- **Username:** `SA` (if left untouched)
- **Password:** `YourStrongPassword1234` (if left untouched)

Please ensure that these details match the configuration in your `.env` file. If you have made changes to the default settings, you will need to update these details accordingly.

## Running the Application

To start the FastAPI application, run the following command:

```bash
uvicorn main:app --reload --port 8000
```

## Database Migrations with Alembic

Alembic is a database migration tool for SQLAlchemy and is used to track changes in your database schema. 

### Creating Migrations

You can generate a new migration file with Alembic using the `revision` command. If you want Alembic to populate the migration script with detected changes from your models, use the `--autogenerate` option.

```bash
alembic revision --autogenerate -m "Your message"
```

Replace "Your message" with a brief description of the changes the migration will make.

### Running Migrations

To apply the migrations to your database, use the `upgrade` command followed by the `head` keyword to apply all migrations, or a specific revision number to apply migrations up to that number.

```bash
alembic upgrade head
```

### Rolling Back Migrations

If you need to undo a migration, you can use the `downgrade` command followed by the `base` keyword to undo all migrations, or a specific revision number to undo migrations down to that number.

```bash
alembic downgrade base
```

Remember to replace `base` with the specific revision number if you only want to undo migrations down to a specific revision.

Please note that Alembic can only detect simple changes automatically. For complex changes like table renaming, you will have to edit the migration script manually.

### Relative Migrations

Alembic also allows you to upgrade or downgrade your database schema relatively. This can be done by using `+n` or `-n` where `n` is the number of versions you want to upgrade or downgrade.

To upgrade your database schema by one version, you can use:

```bash
alembic upgrade +1
```

Similarly, to downgrade your database schema by one version, you can use:

```bash
alembic downgrade -1
```

This is particularly useful when you want to step through your migrations one at a time.