# CalculatorLibrary

This repository is only intended for playing around with the circleCI tool for implementing a CI on a GitHub repository
as well as exploring pre-commit hooks.

Commands for using pre-commit hooks in a python project (When using poetry as a dependency management tool):

* `poetry add --dev pre-commit` (Adding pre-commit as a dev dependency to the pyproject.toml and locking the used version in poetry.lock)
* `poetry run pre-commit install --hook-type pre-commit` (Read the configuration from .pre-commit-config.yaml and override the pre-commit bash script
pre-commit.sample located in .git/hooks and remove the ending .sample -> Only then will git execute the script when a commit command was issued.)
