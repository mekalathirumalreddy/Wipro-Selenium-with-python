import pytest
import requests

@pytest.fixture(scope="session")
def auth_token():
    response = requests.post(
        "https://api.example.com/login",
        json={"username": "admin", "password": "secret"}
    )
    token = response.json()["token"]
    return token
