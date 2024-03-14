"""Test the generate_project function in the generate_project module."""

import shutil
from pathlib import Path

import pytest
from utils.project import generate_project


@pytest.fixture(scope="function")
def project_dir() -> Path:
    """Setup a project directory for testing."""

    template_values = {
        "repo_name": "test-repo"
    }
    print("Setup")
    generated_repo_dir = generate_project(template_values=template_values)
    yield generated_repo_dir
    shutil.rmtree(generated_repo_dir)
    print("Teardown")


def test__can_generate_project(project_dir: Path):
    """Test that the generate_project function can generate a project.
        execute" `cookiecutter <template directory> `
    """
    assert project_dir.exists()
