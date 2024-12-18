import pytest
from api_server import app
import os


@pytest.fixture
def client():
    """Fixture to provide a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_chat_completions_success(client):
    """Test successful chat completions."""
    # Mock environment variable for custom base url
    os.environ["CUSTOM_BASE_URL"] = "http://test_url"

    # Test with a valid request
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10,
    }
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 200
    assert response.get_json() is not None
    # Add more assertions to check the response content if needed


def test_chat_completions_missing_model(client):
    """Test chat completions with missing model."""
    # Test with missing model
    data = {
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10,
    }
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 400
    assert "Missing 'model' or 'messages' in request" in response.get_json()["error"]


def test_chat_completions_missing_messages(client):
    """Test chat completions with missing messages."""
    # Test with missing messages
    data = {"model": "gpt-3.5-turbo", "temperature": 0.5, "max_tokens": 10}
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 400
    assert "Missing 'model' or 'messages' in request" in response.get_json()["error"]


def test_chat_completions_error(client, monkeypatch):
    """Test chat completions with an error from litellm."""

    # Test with an error from litellm
    def mock_handle_chat_completions(*args, **kwargs):
        raise ValueError("Test Error")

    monkeypatch.setattr(
        "api_server._handle_chat_completions", mock_handle_chat_completions
    )

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10,
    }
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 500
    assert "Test Error" in response.get_json()["error"]
import os
import pytest
from flask import Flask
from api_server import app
from unittest.mock import patch
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
        "max_tokens": 10,
    }
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 200

@patch("api_server._call_litellm")
def test_chat_completions_error(mock_call_litellm, client):
    # Test with an error from litellm
    mock_call_litellm.side_effect = Exception("Test Error")

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "hello"}],
        "temperature": 0.5,
        "max_tokens": 10,
    }
    response = client.post("/chat/completions", json=data)
    assert response.status_code == 500
    assert response.get_json()["error"] == "Test Error"

def test_chat_completions_missing_data(client):
    # Test with missing data
    response = client.post("/chat/completions", json={})
    assert response.status_code == 400
    assert response.get_json()["error"] == "Missing 'model' or 'messages' in request"

def test_chat_completions_empty_body(client):
    # Test with empty request body
    response = client.post("/chat/completions", data=None, content_type='application/json')
    assert response.status_code == 400
    json_response = response.get_json()
    assert json_response is not None and json_response.get("error") == "Request body is empty or not properly formatted"
