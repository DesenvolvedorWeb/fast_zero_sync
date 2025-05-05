"""FastZero Application"""

from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserInDB, UserList, UserPublic, UserSchema

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


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    """
    This function updates an existing user.
    """
    if user_id < 1 or user_id > len(database):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail='User not found')

    user_with_id = UserInDB(
        id=user_id,
        **user.model_dump(),
    )
    database[user_id - 1] = user_with_id
    return user_with_id
