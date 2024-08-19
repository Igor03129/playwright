import pytest

from pages.home import HomePage
from pages.professions import ProfessionsPage
from helpers.config import load_config


def pytest_addoption(parser: pytest.Parser) -> None:
    parser.addoption("--domain", action="store", default="ru")


@pytest.fixture()
def home_page(page):
    return HomePage(page)


@pytest.fixture()
def professions_page(page):
    return ProfessionsPage(page)


@pytest.fixture(scope="session")
def config(request):
    domain = request.config.getoption("--domain").lower()
    return load_config(domain)
