import pytest
import requests

BASE_URL = 'http://localhost:5000'
tasks = []

def testCreateTask():
    newTask = {
        "title": "Task",
        "description": "Test Task"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=newTask)

    assert response.status_code == 201
