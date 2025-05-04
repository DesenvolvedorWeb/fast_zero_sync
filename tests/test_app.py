from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app


def test_read_root():
    client = TestClient(app)  #This is the root endpoint - Arrange
    response = client.get("/")  # - Act
    assert response.status_code == HTTPStatus.OK # - Assert
    assert response.json() == {"message": "Welcome to FastZero!"} # - Assert


def test_create_user():
    client = TestClient(app)  # This is the create user endpoint - Arrange
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
