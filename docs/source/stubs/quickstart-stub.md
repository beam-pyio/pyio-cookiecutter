Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

```{prompt} bash
pip install cookiecutter
```

Generate a Python package structure using [`pyio-cookiecutter`](https://github.com/beam-pyio/pyio-cookiecutter):

```{prompt} bash
cookiecutter https://github.com/beam-pyio/pyio-cookiecutter
```

```text
pkg
├── .github                    ┐
│   └── workflows              │
│       ├── doc.yml            │ GitHub Actions workflow
│       ├── release.yml        │
│       └── test.yml           ┘
├── .gitignore                 ┐
├── CHANGELOG.md               │
├── CONDUCT.md                 │
├── CONTRIBUTING.md            │
├── LICENSE                    │
├── README.md                  ┘
├── docs                       ┐
│   ├── Makefile               │
│   ├── changelog.md           │
│   ├── conduct.md             │ Package documentation
│   ├── conf.py                │
│   ├── contributing.md        │
│   ├── index.md               │
│   └── requirements.txt       ┘
├── pyproject.toml             ┐ 
├── src                        │
│   └── pkg                    │ Package source code, metadata,
│       ├── __init__.py        │ and build instructions 
│       └── pkg.py             ┘
└── tests                      ┐
    └── test_pkg.py            ┘ Package tests
```
