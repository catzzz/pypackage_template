"""Fixtures for testing the project generation."""


import shutil
import subprocess
from pathlib import Path

import pytest
from utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="function")
def project_dir() -> Path:
    """Create an instance of our cookiecutter template to be re-used in tests."""

    template_values = {"repo_name": "test-repo"}
    print("Setup")
    generated_repo_dir = generate_project(template_values=template_values)
    initialize_git_repo(generated_repo_dir)
    subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)
    print("Teardown")
