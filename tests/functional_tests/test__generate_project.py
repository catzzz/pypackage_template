"""Test the generate_project function in the generate_project module."""


from pathlib import Path


def test__can_generate_project(project_dir: Path):
    """Test that the generate_project function can generate a project.
    execute" `cookiecutter <template directory> `
    """
    assert project_dir.exists()
