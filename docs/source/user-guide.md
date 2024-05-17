# User Guide

This section provides a high-level walk through of building an Apache Beam Python I/O connector package using the `pyio-cookiecutter` template.

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/1.7.2/) and [`poetry](https://python-poetry.org/) using `pip`:

    ```{prompt} bash
    pip install cookiecutter poetry
    ```

2. Generate a Python package file and directory structure.

    ```{prompt} bash
    cookiecutter https://github.com/beam-pyio/pyio-cookiecutter
    ```

3. Create and activate a virtual environment.

    ```{prompt} bash
    cd <package-name>
    python -m venv venv
    source venv/bin/activate
    ```

4. Add Python code to module(s) in the `src/` directory. If your project has dependencies, add them using `poetry`:

    ```{prompt} bash
    poetry add <dependency>
    ```

5. Install and try out your package in a Python interpreter.

    ```{prompt} bash
    poetry install
    ```

6. Write tests for your package in module(s) prefixed with *`test_`* in the *`tests/`* directory. Add `pytest` and `pytest-cov` as development dependencies and calcualte the coverage of your tests.

    ```{prompt} bash
    poetry add --dev pytest pytest-cov
    pytest tests/ --cov=<pkg-name>
    ```

7. Create documentation for your package. Add the necessary development dependencies listed below and then compile and render documentation to HTML.

    ```{prompt} bash
    poetry add --dev myst-nb sphinx-autoapi sphinx-rtd-theme
    make html --directory docs/
    ```

    Note that the document is published via GitHub Workflows (`.github/workflows/publish.yml`). For this, GitHub Pages should be enabled where the build and deploy source is set to *GitHub Actions*.

```{image} _static/github-pages.png
:alt: github-pages-config
:width: 600px
:align: center
```

8. Build sdist and wheel distributions for your package.

    ```{prompt} bash
    poetry build
    ```

9. Publish your distributions to [TestPyPi](https://test.pypi.org/) and try installing your package.

    ```{prompt} bash
    poetry config repositories.test-pypi https://test.pypi.org/legacy/
    poetry publish -r test-pypi
    pip install --index-url https://test.pypi.org/simple/ <pkg-name>
    ```

10. Publish your distributions to [PyPi](https://pypi.org/). Your package can now be installed by anyone using `pip`.

    ```{prompt} bash
    poetry publish
    pip install <pkg-name>
    ```

## Continuous integration and continuous deployment

**TO BE UPDATED**