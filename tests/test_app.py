from http import HTTPStatus
from urllib import response


def test_read_root(client):
    response = client.get('/')  # - Act
    assert response.status_code == HTTPStatus.OK # - Assert
    assert response.json() == {'message': 'Welcome to FastZero!'} # - Assert


def test_create_user(client):
    response =  client.post( # test for UserSchema endpoitnt
        '/users/',
        json={
            'username': 'testuser',
            'email': 'user@email.com',
            'password': 'securepassword',
        }
    )  # - Act
    assert response.status_code == HTTPStatus.CREATED  # - Assert status code
    assert response.json() == { # - Assert validar UserPublic
        'id': 1,
        'username': 'testuser',
        'email': 'user@email.com',
    }

# O teste não conta com base de dados real, por isso depende do teste acima,
# pratica educativa apenas para mostrar o funcionamento do CRUD
def test_read_users(client):
    response = client.get('/users/')  # - Act

    assert response.status_code == HTTPStatus.OK  # - Assert
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'testuser',
                'email': 'user@email.com',
            }
        ]
    }

