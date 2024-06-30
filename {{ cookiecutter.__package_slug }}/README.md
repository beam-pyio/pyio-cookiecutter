# {{ cookiecutter.__package_slug }}

![doc](https://github.com/beam-pyio/{{ cookiecutter.__package_slug }}/workflows/doc/badge.svg)
![test](https://github.com/beam-pyio/{{ cookiecutter.__package_slug }}/workflows/test/badge.svg)
[![release](https://img.shields.io/github/release/beam-pyio/{{ cookiecutter.__package_slug }}.svg)](https://github.com/beam-pyio/{{ cookiecutter.__package_slug }}/releases)
![python](https://img.shields.io/badge/python-3.8%2C%203.9%2C%203.10%2C%203.11%2C%203.12-blue)
![os](https://img.shields.io/badge/OS-Ubuntu%2C%20Mac%2C%20Windows-purple)

{{ cookiecutter.package_short_description }}

## Installation

```bash
$ pip install {{ cookiecutter.__package_slug }}
```

## Usage

- TODO

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`{{ cookiecutter.__package_slug }}` was created by {{ cookiecutter.author_name }}. {% if cookiecutter.open_source_license != 'None' -%}It is licensed under the terms of the {{ cookiecutter.open_source_license }} license.{% else %}{{ cookiecutter.author_name }} retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.{% endif %}

## Credits

`{{ cookiecutter.__package_slug }}` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `pyio-cookiecutter` [template](https://github.com/beam-pyio/pyio-cookiecutter).
