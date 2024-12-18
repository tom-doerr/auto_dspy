import pytest
import json
from .load_data import load_and_parse_log_data
import os

def create_dummy_log_file(content, filename="test_log.log"):
    """Helper function to create a dummy log file for testing."""
    with open(filename, 'w') as f:
        f.write(content)
    return filename

def remove_dummy_log_file(filename):
    """Helper function to remove the dummy log file after testing."""
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass

def test_load_and_parse_log_data_success():
    """Test loading and parsing valid JSON log data."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "hello"}]}}
    {"timestamp": "2024-05-02T10:05:00", "request_data": {"model": "gpt-4", "messages": [{"role": "user", "content": "how are you?"}]}}
    """
    log_file = create_dummy_log_file(log_content)
    loaded_data = load_and_parse_log_data(log_file)
    remove_dummy_log_file(log_file)

    assert loaded_data is not None
    assert len(loaded_data) == 2
    assert loaded_data[0]["request_data"]["model"] == "gpt-3.5-turbo"
    assert loaded_data[1]["request_data"]["model"] == "gpt-4"

def test_load_and_parse_log_data_with_invalid_json():
    """Test loading and parsing log data with invalid JSON lines."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "hello"}]}}
    invalid json line
    {"timestamp": "2024-05-02T10:05:00", "request_data": {"model": "gpt-4", "messages": [{"role": "user", "content": "how are you?"}]}}
    """
    log_file = create_dummy_log_file(log_content)
    loaded_data = load_and_parse_log_data(log_file)
    remove_dummy_log_file(log_file)

    assert loaded_data is not None
    assert len(loaded_data) == 2
    assert loaded_data[0]["request_data"]["model"] == "gpt-3.5-turbo"
    assert loaded_data[1]["request_data"]["model"] == "gpt-4"

def test_load_and_parse_log_data_file_not_found():
    """Test loading data when the log file does not exist."""
    log_file = "non_existent_log.log"
    loaded_data = load_and_parse_log_data(log_file)
    assert loaded_data is None

def test_load_and_parse_log_data_empty_file():
    """Test loading data from an empty log file."""
    log_file = create_dummy_log_file("")
    loaded_data = load_and_parse_log_data(log_file)
    remove_dummy_log_file(log_file)
    assert loaded_data == []
