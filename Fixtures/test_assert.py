import pytest

#Fixtures

@pytest.fixture(scope="function")
def preWork():
    print("\nI setup browser instance.")
    return "pass"

def test_initialCheck(preWork):
    print("\nThis is First Test.")
    assert preWork=="fail"

def test_secondCheck(preWork):
    print("\nThis is Second Test.")
    return "pass"
