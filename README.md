# Apache Beam Python I/O Cookiecutter

![doc](https://github.com/beam-pyio/pyio-cookiecutter/workflows/doc/badge.svg)
![test](https://github.com/beam-pyio/pyio-cookiecutter/workflows/test/badge.svg)
[![release](https://img.shields.io/github/release/beam-pyio/pyio-cookiecutter.svg)](https://github.com/beam-pyio/pyio-cookiecutter/releases)
[![python](https://img.shields.io/badge/python-3.8%2C%203.9%2C%203.10%2C%203.11-blue)]()
[![os](https://img.shields.io/badge/OS-Ubuntu%2C%20Mac-purple)]()

<p align="center">
  <img src="docs/source/_static/logo.png" width="220" alt="pyio-cookiecutter logo">
</p>

<br>

`pyio-cookiecutter` is a [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) template for creating a package for the [Apache Beam Python I/O Connectors](https://github.com/beam-pyio) project using [`poetry`](https://python-poetry.org).

## Usage

Please see the [documentation](https://beam-pyio.github.io/pyio-cookiecutter/) for more detail on using `pyio-cookiecutter`. We provide the fundamental steps below:

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

    ```bash
    pip install cookiecutter
    ```

2. Generate a Python package structure using [`pyio-cookiecutter`](https://github.com/beam-pyio/pyio-cookiecutter):

    ```bash
    cookiecutter https://github.com/beam-pyio/pyio-cookiecutter.git
    ```

3. After responding to the prompts you should have a directory structure similar to that shown below. To learn more about the contents of this directory structure, please see the `pyio-cookiecutter` [documentation](https://beam-pyio.github.io/pyio-cookiecutter/).

    ```text
    pkg
    ├── .github                    ┐
    │   └── workflows              │ GitHub Actions workflow
    │       └── ci-cd.yml          ┘
    ├── .gitignore                 ┐
    ├── .readthedocs.yml           │
    ├── CHANGELOG.md               │
    ├── CONDUCT.md                 │
    ├── CONTRIBUTING.md            │
    ├── docs                       │
    │   ├── make.bat               │
    │   ├── Makefile               │
    │   ├── requirements.txt       │
    │   ├── changelog.md           │
    │   ├── conduct.md             │
    │   ├── conf.py                │ Package documentation
    │   ├── contributing.md        │
    │   ├── index.md               │
    │   └── usage.ipynb            │
    ├── LICENSE                    │
    ├── README.md                  ┘
    ├── pyproject.toml             ┐ 
    ├── src                        │
    │   └── pkg                    │ Package source code, metadata,
    │       ├── __init__.py        │ and build instructions 
    │       └── pkg.py             ┘
    └── tests                      ┐
        └── test_pkg.py            ┘ Package tests
    ```

## Contributing

Interested in contributing? Check out the [Contributing Guidelines](https://beam-pyio.github.io/pyio-cookiecutter/contributing.html). Please note that this project is released with a [Code of Conduct](https://beam-pyio.github.io/pyio-cookiecutter/conduct.html). By contributing to this project, you agree to abide by its terms.

## License

`pyio-cookiecutter` is licensed under the terms of the BSD license.

## Acknowledgements

`pyio-cookiecutter` was originally developed for use in the [Apache Beam Python I/O Connectors](https://github.com/beam-pyio) project. It was inspired by the `Py-Pkgs-Cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
