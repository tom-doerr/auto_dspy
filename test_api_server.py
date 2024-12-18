import pytest
import json
from api_server import app
import os
import litellm

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_chat_completions_success(client):
    # Mock environment variable for custom base url
    os.environ["CUSTOM_BASE_URL"] = "http://test_url"
    
    # Test with a valid request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10
    }
    response = client.post('/chat/completions', json=data)
    assert response.status_code == 200
    assert response.get_json() is not None
    # Add more assertions to check the response content if needed

def test_chat_completions_missing_model(client):
    # Test with missing model
    data = {
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10
    }
    response = client.post('/chat/completions', json=data)
    assert response.status_code == 400
    assert "Missing 'model' or 'messages' in request" in response.get_json()["error"]

def test_chat_completions_missing_messages(client):
    # Test with missing messages
    data = {
        "model": "gpt-3.5-turbo",
        "temperature": 0.5,
        "max_tokens": 10
    }
    response = client.post('/chat/completions', json=data)
    assert response.status_code == 400
    assert "Missing 'model' or 'messages' in request" in response.get_json()["error"]

def test_chat_completions_error(client, monkeypatch):
    # Test with an error from litellm
    def mock_completion(*args, **kwargs):
        raise Exception("Test Error")
    monkeypatch.setattr(litellm, "completion", mock_completion)
    
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10
    }
    response = client.post('/chat/completions', json=data)
    assert response.status_code == 500
    assert "Test Error" in response.get_json()["error"]
