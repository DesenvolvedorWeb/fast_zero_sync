import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app

@pytest.fixture()  # - Fixture to create a test client  Arrange
def client():
    """
    This fixture creates a test client for the FastAPI application.
    """
    return TestClient(app)
# Compare this snippet from fast_zero/schemas.py:

