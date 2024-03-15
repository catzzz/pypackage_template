"""
Test Makefile.

1. generate a project using the cookiecutter
2. create a virtual environment and install project deppendencies
---
3. run tests
4. run linting
---
Cleanu up / Tear down
5. remove the virtual environment
6. remove the generated project

"""
import subprocess
from pathlib import Path


def test__linting_passes(project_dir: Path):
    """Test that the linting passes."""
    subprocess.run(["make", "lint-ci"], cwd=project_dir, check=True)


def test__tests_pass(project_dir: Path):
    """Test that the tests pass."""
    subprocess.run(["make", "install"], cwd=project_dir, check=True)
    subprocess.run(["make", "test-wheel-locally"], cwd=project_dir, check=True)


def test__install_succeeds():
    """Test that the project can be installed."""
    subprocess.run(["make", "install"], check=True)
