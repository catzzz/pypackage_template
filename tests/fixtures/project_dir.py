"""Fixtures for testing the project generation."""


import shutil
import subprocess
from pathlib import Path
from uuid import uuid4

import pytest
from utils.project import (
    generate_project,
    initialize_git_repo,
)


@pytest.fixture(scope="session")
def project_dir() -> Path:
    """Create an instance of our cookiecutter template to be re-used in tests."""
    test_session_id:str = generate_test_session_id()
    template_values = {"repo_name": f"test-repo-{test_session_id}"}

    generated_repo_dir = generate_project(template_values=template_values, 
                                          test_session_id=test_session_id)
    try:
        initialize_git_repo(generated_repo_dir)
        subprocess.run(["make", "lint-ci"], cwd=generated_repo_dir, check=False)
        yield generated_repo_dir
    finally:
        shutil.rmtree(path=generated_repo_dir)
        print("Teardown")


def generate_test_session_id() -> str:
    """Generate a unique session id for the test session."""
    test_session_id = str(uuid4())[:6]
    return test_session_id