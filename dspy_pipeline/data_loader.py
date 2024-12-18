"""
This module provides functions to create DSPy datasets from log files.
"""

import dspy
from correct_module.load_data import load_and_parse_log_data  # Replace with the correct module path


def create_dspy_dataset_from_logs(log_file_path):
    """
    Creates a DSPy dataset from the log file.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of dspy.Example objects.
    """
    log_entries = load_and_parse_log_data(log_file_path)
    if log_entries is None:
        return []

    dspy_examples = []
    for entry in log_entries:
        request_data = entry.get("request_data", {})
        messages = request_data.get("messages", [])
        if messages:
            # Assuming the last message is the user's query
            last_message = messages[-1]
            if last_message.get("role") == "user":
                question = last_message.get("content")
                # Create a dspy.Example with the question
                dspy_example = dspy.Example(question=question)
                dspy_examples.append(dspy_example)
    return dspy_examples
