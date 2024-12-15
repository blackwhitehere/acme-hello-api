from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def hello_world():
    """
    Prints Hello World

    Returns:
        dict: hello world message
    """
    return {"message": "Hello World!"}