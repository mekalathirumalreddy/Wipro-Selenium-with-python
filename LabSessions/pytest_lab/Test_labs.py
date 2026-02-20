#1.Write a test that is skipped because a feature is not implemented yet.
import pytest

@pytest.mark.skip(reason="Feature not implemented yet")
def test_new_dashboard():
    assert False


#2.write a test that runs only on Linux and skips on Windows.
import pytest
import sys

@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_linux_only():
    assert True

#3. Write a test that checks an API health endpoint.
#If status code is not 200 → skip the test dynamically.
import pytest
import requests

def test_api_health():
    response = requests.get("https://api.example.com/health")
    if response.status_code != 200:
        pytest.skip("API is down or unhealthy")
    assert response.status_code == 200

# 4. 4.Mark a failing test as xfail with reason: "Bug #123".
import pytest

@pytest.mark.xfail(reason="Bug #123")
def test_known_failing_feature():
    assert False # This test will fail but not fail the whole build