import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_todo_status_200():
    response = requests.get(f"{BASE_URL}/todos/1")
    assert response.status_code == 200

def test_get_todo_has_required_fields():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "completed" in data
    assert "userId" in data

def test_get_todo_correct_id():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert data["id"] == 1

def test_user_multiple_todos():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert len(data) > 0

def test_todo_completed_is_boolean():
    response = requests.get(f"{BASE_URL}/todos/1")
    data = response.json()
    assert isinstance(data["completed"], bool)


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])