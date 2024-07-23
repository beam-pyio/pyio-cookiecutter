from {{ cookiecutter.__package_slug }}.io import my_fn

def test_my_fn():
    assert my_fn() == 1
