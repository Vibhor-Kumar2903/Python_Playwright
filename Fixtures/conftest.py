import pytest

@pytest.fixture(scope="session") #runs once across the session
def global_instance():
    print("\nI setup browser global instance.")