import json
import subprocess
from pathlib import Path

from pytest import (
    fixture,
    mark,
)

IGNORE = [".DS_Store", "__pycache__"]


@fixture()
def base_command(tmpdir):
    return (f"cookiecutter . --no-input --output-dir {tmpdir}", tmpdir)


def num_items(path, directory=[""]):
    files = [
        file
        for file in path.joinpath(*directory).iterdir()
        if file.name not in IGNORE
    ]
    return len(files)


def test_cookiecutter_default_options(base_command):
    result = subprocess.run(base_command[0], shell=True)
    assert result.returncode == 0


with open("cookiecutter.json") as f:
    options = json.load(f)


@mark.parametrize("open_source_license", options["open_source_license"])
def test_cookiecutter_all_options(
    base_command, open_source_license
):
    params = f' open_source_license="{open_source_license}"'
    path = Path(base_command[1]).joinpath(options["package_name"])
    result = subprocess.run(base_command[0] + params, shell=True)
    assert result.returncode == 0
    assert num_items(path, ["tests"]) == 1
    assert num_items(path, [f"src/{options['package_name']}"]) == 2
    assert num_items(path, ["docs"]) == 7
    assert num_items(path, [".github", "workflows"]) == 3
    if open_source_license == "None":
        assert num_items(path) == 10
    else:
        assert num_items(path) == 11
