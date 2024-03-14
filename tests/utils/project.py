"""Helper functions for testing projects."""

import json
import subprocess
from copy import deepcopy
from typing import Dict

from tests.consts import PROJECT_DIR


def generate_project(template_values: Dict[str, str]):
    """Generate a project using the cookiecutter."""
    template_values = deepcopy(template_values)
    cookiecutter_config = {"default_context": template_values}
    cookiecutter_config_file = PROJECT_DIR / "cookiecutter-config.json"
    cookiecutter_config_file.write_text(json.dumps(cookiecutter_config))
    cmd = [
        "cookiecutter",
        str(PROJECT_DIR),
        "--output-dir",
        str(PROJECT_DIR / "sample"),
        "--no-input",
        "--config-file",
        str(cookiecutter_config_file),
         "--verbose",

    ]

    generated_repo_dir = PROJECT_DIR / "sample" / template_values["repo_name"]
    subprocess.run(cmd, check=True)
    return generated_repo_dir
