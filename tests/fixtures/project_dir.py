"""Fixtures for testing the project generation."""


import shutil
from pathlib import Path

import pytest
from utils.project import generate_project


@pytest.fixture(scope="function")
def project_dir() -> Path:
    """Create an instance of our cookiecutter template to be re-used in tests."""

    template_values = {
        "repo_name": "test-repo"
    }
    print("Setup")
    generated_repo_dir = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)
    print("Teardown")
