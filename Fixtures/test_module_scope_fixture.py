import pytest

#Fixtures

@pytest.fixture(scope="module") #runs once against a file
def preWork():
    print("\nI setup browser instance.")


def test_initialCheck(preWork):
    print("\nThis is First Test.")


def test_secondCheck(preWork):
    print("\nThis is Second Test.")



