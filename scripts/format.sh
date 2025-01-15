#!/bin/bash

printf "\nRunning pyright...\n"
pyright

printf "\nRunning ruff check...\n"
ruff check --fix

printf "\nRunning ruff format...\n"
ruff format
