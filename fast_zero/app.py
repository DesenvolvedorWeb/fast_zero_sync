"""FastZero Application"""

from fastapi import FastAPI  # type: ignore

app = FastAPI()


@app.get('/')
def read_root():
    """
    This function reads the root directory of the FastZero application.
    It is a placeholder for future functionality.
    """

    return {'message': 'Welcome to FastZero!'}
