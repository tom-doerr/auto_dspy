import pytest
import os
import dspy
import json
from dspy_pipeline.data_loader import create_dspy_dataset_from_logs


def create_dummy_log_file(content, filename="test_log.log"):
    """Helper function to create a dummy log file for testing."""
    with open(filename, "w") as f:
        f.write(content)
    return filename


def remove_dummy_log_file(filename):
    """Helper function to remove the dummy log file after testing."""
    try:
        os.remove(filename)
    except FileNotFoundError:
        pass


def test_create_dspy_dataset_from_logs_success():
    """Test creating a DSPy dataset from valid log data."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {"messages": [{"role": "user", "content": "hello"}]}}
    {"timestamp": "2024-05-02T10:05:00", "request_data": {"messages": [{"role": "user", "content": "how are you?"}]}}
    """
    log_file = create_dummy_log_file(log_content)
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    remove_dummy_log_file(log_file)

    assert len(dspy_dataset) == 2
    assert isinstance(dspy_dataset[0], dspy.Example)
    assert dspy_dataset[0].question == "hello"
    assert dspy_dataset[0].answer == "hi there"
    assert dspy_dataset[1].question == "how are you?"
    assert dspy_dataset[1].answer == "I am fine, thank you"
    assert dspy_dataset[0].answer is None
    assert dspy_dataset[1].answer is None


def test_create_dspy_dataset_from_logs_with_response_success():
    """Test creating a DSPy dataset from valid log data with responses."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {"messages": [{"role": "user", "content": "hello"}]}, "response_data": {"choices": [{"message": {"role": "assistant", "content": "hi there"}}]}}
    {"timestamp": "2024-05-02T10:05:00", "request_data": {"messages": [{"role": "user", "content": "how are you?"}]}, "response_data": {"choices": [{"message": {"role": "assistant", "content": "I am fine, thank you"}}]}}
    """
    log_file = create_dummy_log_file(log_content)
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    remove_dummy_log_file(log_file)

    assert len(dspy_dataset) == 2
    assert isinstance(dspy_dataset[0], dspy.Example)
    assert dspy_dataset[0].question == "hello"
    assert dspy_dataset[0].answer == "hi there"
    assert dspy_dataset[1].question == "how are you?"
    assert dspy_dataset[1].answer == "I am fine, thank you"


def test_create_dspy_dataset_from_logs_no_messages():
    """Test creating a DSPy dataset when messages are missing."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {}}
    """
    log_file = create_dummy_log_file(log_content)
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    remove_dummy_log_file(log_file)

    assert len(dspy_dataset) == 0


def test_create_dspy_dataset_from_logs_file_not_found():
    """Test creating a DSPy dataset when the log file does not exist."""
    log_file = "non_existent_log.log"
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    assert len(dspy_dataset) == 0


def test_create_dspy_dataset_from_logs_empty_file():
    """Test creating a DSPy dataset from an empty log file."""
    log_file = create_dummy_log_file("")
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    remove_dummy_log_file(log_file)
    assert len(dspy_dataset) == 0


def test_create_dspy_dataset_from_logs_invalid_json():
    """Test creating a DSPy dataset with invalid JSON lines."""
    log_content = """
    {"timestamp": "2024-05-02T10:00:00", "request_data": {"messages": [{"role": "user", "content": "hello"}]}}
    invalid json line
    {"timestamp": "2024-05-02T10:05:00", "request_data": {"messages": [{"role": "user", "content": "how are you?"}]}}
    """
    log_file = create_dummy_log_file(log_content)
    dspy_dataset = create_dspy_dataset_from_logs(log_file)
    remove_dummy_log_file(log_file)

    assert len(dspy_dataset) == 2
    assert isinstance(dspy_dataset[0], dspy.Example)
    assert dspy_dataset[0].question == "hello"
    assert dspy_dataset[1].question == "how are you?"
