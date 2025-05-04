"""FastZero Application"""

from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """
    This function reads the root directory of the FastZero application.
    It is a placeholder for future functionality.
    """

    return {'message': 'Welcome to FastZero!'}
