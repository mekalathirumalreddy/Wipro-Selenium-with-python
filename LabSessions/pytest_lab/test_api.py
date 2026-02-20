import pytest


# Fixture that generates authentication token once per session


@pytest.fixture(scope="session")
def auth_token():
    print("\nGenerating auth token")
    return "token_123"


def test_get_users(auth_token):
    print("Using token in get users:", auth_token)
    assert auth_token == "token_123"


def test_get_orders(auth_token):
    print("Using token in get orders:", auth_token)
    assert auth_token == "token_123"



# Fixture that creates user before test and deletes after test

@pytest.fixture
def test_user():
    print("\nCreating test user")
    user_id = 101

    yield user_id   # test runs here

    print("Deleting test user")


def test_user_profile(test_user):
    print("Testing user profile for:", test_user)
    assert test_user == 101



# Validate JSON response schema


def test_json_schema_validation():
    response = {
        "id": 1,
        "name": "John",
        "email": "john@test.com"
    }

    assert "id" in response
    assert "name" in response
    assert "email" in response

    assert isinstance(response["id"], int)
    assert isinstance(response["name"], str)
    assert isinstance(response["email"], str)



# Parametrized test for multiple HTTP status codes

@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_http_status_codes(status_code):
    print("Validating status code:", status_code)
    assert status_code in [200, 400, 401, 500]



# Fixture chain: base_url → auth_token → user → test case

@pytest.fixture(scope="session")
def base_url():
    print("\nSetting base URL")
    return "https://api.example.com"


@pytest.fixture(scope="session")
def chained_auth_token(base_url):
    print("Creating auth token using:", base_url)
    return "token_abc"


@pytest.fixture
def user(chained_auth_token):
    print("Creating user using token:", chained_auth_token)
    return {"id": 1, "name": "John"}


def test_user_flow(user):
    print("Running test with user:", user)
    assert user["id"] == 1
