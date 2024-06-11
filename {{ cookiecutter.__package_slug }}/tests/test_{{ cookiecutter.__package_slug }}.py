from {{ cookiecutter.__package_slug }} import {{ cookiecutter.__package_slug }}

def test_my_fn():
    assert {{ cookiecutter.__package_slug }}.my_fn() == 1
