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

        # Find the user's question (from messages) and assistant's response (from response_data)
        question = None
        answer = None
        
        # Get the question from the last user message
        for message in reversed(messages):
            if message.get("role") == "user":
                question = message.get("content")
                break
        
        # Get the answer from the response data
        response_data = entry.get("response_data", {})
        if response_data and "choices" in response_data:
            first_choice = response_data["choices"][0]
            if "message" in first_choice and first_choice["message"].get("role") == "assistant":
                answer = first_choice["message"].get("content")
        
        # Create example only if we have both question and answer
        if question and answer:
            dspy_example = dspy.Example(question=question, answer=answer).with_inputs("question")
            dspy_examples.append(dspy_example)
    return dspy_examples
