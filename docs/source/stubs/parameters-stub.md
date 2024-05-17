When generating a Python package structure using [`pyio-cookiecutter`](https://github.com/beam-pyio/pyio-cookiecutter), you will be prompted for the input parameters shown below.

```{table} Description of <code>pyio-cookiecutter</code> configuration parameters.
:name: config-table-features

| Parameters | Default value | Description |
| :--- | :--- | :--- |
|`author_name`               |Monty Python  |Your name.|
|`package_name`              |mypkg                               |Package name (check if your name<br>is already taken [here](http://ivantomic.com/projects/ospnc/)).|
|`package_short_description` |A package for building<br>Python I/O!|Brief description of your project.|
|`package_version`           |0.1.0                               |Initial package version. In [semantic<br>versioning](https://semver.org) `0.1.0` is used for the<br>initial version release.|
|`python_version`            |3.8                                 | Minimum Python version your package<br>will support.|
|`open_source_license`       |MIT                                 |License to use for your package.|
|`include_github_actions`    |no                                  | Whether to include a GitHub Actions<br>workflow file for CI or CI/CD.|
```
