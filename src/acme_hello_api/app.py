import os

from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def hello_world():
    """
    Prints Hello World

    Returns:
        dict: hello world message
    """
    env_var_value = os.getenv("PUBLIC_ENV_VAR", "default_value")
    return {"message": "Hello World!",
            "env_var_value": f"PUBLIC_ENV_VAR has value: {env_var_value}"}