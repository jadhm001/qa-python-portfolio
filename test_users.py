import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_user_status_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200

def test_user_has_required_fields():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "name" in data
    assert "email" in data
    assert "address" in data

def test_user_contains_at_symbol():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert "@" in data["email"]

def test_get_all_users_return_list():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()
    assert isinstance(data, list)
    assert len(data)>0

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])