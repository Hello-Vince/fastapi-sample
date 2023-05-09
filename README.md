# FastAPI Template

## Table of Contents

- Introduction
- Requirements
- Installation
- Local Usage
- API Specification
- Directory Structure
- Contributing

## Introduction

This GitHub repo contains the template to initiate an application project using FastAPI. The application follows the principles of Object-oriented programming which aims modularity, reusability, easily upgradable and scalable.

## Requirements

Creating environment variables. Add more variables if needed.

```bash
# APPLICATION
ENVIRONMENT=[str] # development | production

# DATABASE
DATABASE_URL=[str] # PostgreSQL database

# SECURITY
JWT_EXPIRE_MINUTES=[int] # It is recommended to be shorter than 5 minutes
JWT_ALGORITHM=[str] # It is recommended to use one of the following: HS256 | RS256 | HS512 | RS512
JWT_SECRET_KEY=[str] # To generate a secure random secret key use the command: openssl rand -hex <256 or 512 depending on algo used>
```

Learn how to set up environment variables on Github [here](https://adamtheautomator.com/github-actions-environment-variables/#Managing_Environment_Variables_via_GitHub_Actions_environment_variables_and_Secrets). This step is crutial for running tests without crashing.

## Installation

Installing dependencies.

```python
git clone https://github.com/BalloonBox-Inc/bbox-templates-fastapi.git # clone template to your project directory as a sub-directory

mv -v bbox-templates-fastapi/{*,.*} . # move template content to your project root directory (out of the cloned sub-directory)

python -m venv venv # create environment

source venv/bin/activate # activate environment

pip install --upgrade pip setuptools -r requirements.txt # install packages

pre-commit install # install hooks
```

Delete bbox-templates-fastapi sub-directory from your project since now it's empty.

## Development

Creating your own APIs. Build them under `./apis/routers/**.py`. There are currently two API examples that can be used as guidance.

Remember to update the following files as appropriate:

```bash
./apis/middleware.py
./apis/schemas.py
```

## Local Usage

Running the application.

```python
uvicorn main:app --reload
```

## API Specification

[Documentation](http://127.0.0.1:8000/redoc) and [test environment](http://127.0.0.1:8000/docs) are available while running locally. **Make sure to not be in the production environment.**

## Directory Structure

If have added new variables to the environment, please make sure to udpate the files tagged with [customizable] as appropriate.

```bash
.
├── .github/workflows
│   └── on_push.yaml                # GitHub actions executed whenever a push is made (quality and test checks)
├── .vscode
│   └── settings.json               # VS Code setting preferences
├── apis
│   ├── routers/**.py               # [directory] multiple API routers, including webhooks
│   ├── schemas/**.py               # [directory] multiple API schemas (http request/response formats)
│   └── middleware.py               # API routers aggregator
├── database
│   ├── crud.py                     # Create, Read, Update, Delete (CRUD) operations to manage data elements of relational databases
│   ├── models.py                   # database tables
│   ├── session.py                  # database connection setup
│   └── startup.py                  # database initial data insertion.
├── helpers
│   ├── api_exceptions.py           # API exceptions settings
│   ├── api_routers.py              # include API routers
│   ├── api_throttling.py           # API throttling settings
│   ├── http_requests.py            # HTTP requests settings and error handling
│   ├── lru_caching.py              # LRU cache decorator settings
│   └── misc.py                     # miscellaneous collection of unit functions
├── security
│   ├── admin.py                    # admin authentication setup
│   ├── dependencies.py             # required inejctions (security and authentication) to happen before running an API router
│   ├── hashing.py                  # encrypting and verifying signatures
│   └── tokens.py                   # JWT access tokens
├── tests
│   ├── api_tests/**.py             # [directory] multiple API tests: process of checking the functionality, reliability, performance, and security of the programming interfaces
│   └── unit_tests/**.py            # [directory] multiple Unit tests: process of checking each individual units of source code
├── .env                            # [customizable] project environment variables
├── .flake8                         # Flake8 settings and coding standards on a module-by-module basis
├── .gitignore                      # files/directories to be ignored by GitHub when commiting code
├── .pre-commit-config.yaml         # pre-commit hooks settings
├── .pylintrc                       # Pylint settings and coding standards on a module-by-module basis
├── config.py                       # project settings
├── config.yaml                     # [customizable] project settings
├── main.py                         # FastAPI application
├── Procfile                        # [deployment] Heroku commands that are executed by the dyno's app on startup
├── README.md                       # this project guide
├── requirements.txt                # required Python libraries, modules, and packages to run and deploy the project
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.
