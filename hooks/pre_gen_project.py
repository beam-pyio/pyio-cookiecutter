import sys

MIN_CC_VERSION = "2.0.0"

try:
    import cookiecutter # type: ignore
except ImportError:
    print(f"ERROR: please install cookiecutter >= {MIN_CC_VERSION}")
    sys.exit(1)

cc_version = cookiecutter.__version__
# assert cookiecutter >= 2.0.0
if cc_version < MIN_CC_VERSION:
    print(
        f"ERROR: please install cookiecutter >= {MIN_CC_VERSION} (current "
        f"version is {cc_version}):\n"
        f"\tpip install 'cookiecutter>=2', OR\n"
        f"\tconda install 'cookiecutter>=2'"
    )
    sys.exit(1)
