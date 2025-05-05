from http import HTTPStatus


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
