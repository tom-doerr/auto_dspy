"""
This module provides functions to create DSPy datasets from log files.
"""

import dspy
from api.load_data import (
    load_and_parse_log_data,
)


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
        if not messages:
            continue

        # Find the user's question and the assistant's response
        question = None
        answer = None
        for message in reversed(messages):
            if message.get("role") == "user" and question is None:
                question = message.get("content")
            elif message.get("role") == "assistant" and answer is None:
                answer = message.get("content")
        
        if question and answer:
            dspy_example = dspy.Example(question=question, answer=answer)
            dspy_examples.append(dspy_example)
    return dspy_examples
