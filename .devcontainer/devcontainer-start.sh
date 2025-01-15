#!/usr/bin/bash


# Run start commads such as poetry install to keep dependecies updates and in sync with your lock file.

set -xeo pipefail

poetry install --no-ansi --no-root

# Run backend
poetry run uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
