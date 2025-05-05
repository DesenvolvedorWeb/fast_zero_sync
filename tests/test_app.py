from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient
from fast_zero.app import app

@pytest.fixture() # - Fixture to create a test client  Arrange
def client():
    """
    This fixture creates a test client for the FastAPI application.
    """
    return TestClient(app)
# Compare this snippet from fast_zero/schemas.py:

p
def test_read_root(client):
    response = client.get("/")  # - Act
    assert response.status_code == HTTPStatus.OK # - Assert
    assert response.json() == {"message": "Welcome to FastZero!"} # - Assert


def test_create_user(client):
    response =  client.post( # test for UserSchema endpoitnt
        "/users/",
        json={
            "username": 'testuser',
            "email": 'user@email.com',
            "password": 'securepassword',
        }
    )  # - Act
    assert response.status_code == HTTPStatus.CREATED  # - Assert status code
    assert response.json() == { # - Assert validar UserPublic
        "id": 1,
        "username": 'testuser',
        "email": 'user@email.com',
    }  # - Assert response data
