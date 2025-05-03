from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/") # This is the root endpoint - Arrange
    assert response.status_code == HTTPStatus.OK # - Act
    assert response.json() == {"message": "Welcome to FastZero!"} # - Assert
