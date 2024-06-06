# User Guide

This section provides a high-level walk through of building an Apache Beam Python I/O connector package using the `pyio-cookiecutter` template.

## Prerequisites

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/) and [`poetry`](https://python-poetry.org/) using `pip`:

    ```{prompt} bash
    pip install cookiecutter poetry
    ```

## Development workflow

1. Generate a Python package file and directory structure.

    ```{prompt} bash
    cookiecutter https://github.com/beam-pyio/pyio-cookiecutter
    ```

2. Create and activate a virtual environment.

    ```{prompt} bash
    cd <package-name>
    python -m venv venv
    source venv/bin/activate
    ```

3. Add Python code to module(s) in the `src/` directory. If your project has dependencies, add them using `poetry`:

    ```{prompt} bash
    poetry add <dependency>
    ```

4. Install and try out your package in a Python interpreter.

    ```{prompt} bash
    poetry install
    ```

5. Write tests for your package in module(s) prefixed with *`test_`* in the *`tests/`* directory. Add `pytest` and `pytest-cov` as development dependencies and calculate the coverage of your tests.

    ```{prompt} bash
    poetry add --group dev pytest pytest-cov
    pytest tests/ --cov=<pkg-name>
    ```

6. Create documentation for your package. Add the necessary development dependencies listed below and then compile and render documentation to HTML. As the *myst-nb* package doesn't support Python 3.8, it is not installed via *poetry* but by *pip* directly.

    ```{prompt} bash
    pip install -r docs/requirements.txt
    make html --directory docs/
    python -m http.server -d docs/_build/html/ 8000 # serve on port 8000
    ```

7. Build source and wheel distributions for your package.

    ```{prompt} bash
    poetry build
    ```

8. Publish your distributions to [TestPyPi](https://test.pypi.org/) and try installing your package. Include `--build` flag if not built earlier.

    ```{prompt} bash
    poetry config repositories.test-pypi https://test.pypi.org/legacy/
    poetry publish -r test-pypi -u __token__ -p pypi-yourlongtestpypitokengoeshere...
    pip install --index-url https://test.pypi.org/simple/ <pkg-name>
    ```

9. Publish your distributions to [PyPi](https://pypi.org/). Your package can now be installed by anyone using `pip`.  Include `--build` flag if not built earlier.

    ```{prompt} bash
    poetry publish -u __token__ -p pypi-yourlongpypitokengoeshere...
    pip install <pkg-name>
    ```

## Link to remote repository

Create an empty public repository on GitHub. The repository name should match to the package name.

```{image} _static/create-repo.png
:alt: create-repo
:width: 600px
:align: center
```

As the document is published via GitHub Workflows (`.github/workflows/doc.yml`), GitHub Pages should be enabled where the build and deploy source is set to *GitHub Actions*.

```{image} _static/github-pages.png
:alt: github-pages-config
:width: 600px
:align: center
```

## Continuous integration and continuous deployment

There are three workflows in the `.github/workflows` folder.

```text
.github/workflows
├── doc.yml
├── release.yml
└── test.yml
```

The *test* workflow performs unit testing with all the supported Python versions, and it gets triggered on a push or pull request event to the *main* branch.

The *doc* workflow gets triggered when the *test* workflow completes. The package document is built and published to GitHub Pages only if the upstream workflow is succeeded.

The *release* workflow is for creating a release and publish it to the Python Package Index (PyPI). It gets triggered when a tag whose name begins with *v* is pushed. Currently, only a draft release is created, and it is expected to finalize manually. Note the API token that is used to publish a package is stored in the organization secrets.
