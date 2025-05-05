"""FastZero Application"""

from collections import UserList
from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserInDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """
    This function reads the root directory of the FastZero application.
    """

    return {'message': 'Welcome to FastZero!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    """
    This function creates a new user.
    """
    user_with_id = UserInDB(
        id=len(database) + 1,
        **user.model_dump(),
    )

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    """
    This function retrieves all users.
    """
    return {'users': database}
