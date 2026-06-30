import pytest

#Fixtures

@pytest.fixture(scope="function")
def preWork():
    print("\nI setup browser instance.")


def test_initialCheck(preWork):
    print("\nThis is First Test.")


def test_secondCheck(preWork):
    print("\nThis is Second Test.")