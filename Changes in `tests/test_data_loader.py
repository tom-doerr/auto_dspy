"""
Test module for the data loader functionality.
"""

import os
import json
import pytest
import dspy
from dspy_pipeline.data_loader import create_dspy_dataset_from_logs  # Corrected path

def create_dummy_log_file(content, filename="test_log.log"):
    """
    Creates a dummy log file with the given content.

    Args:
        content (str): The content to write to the log file.
        filename (str): The name of the log file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

def remove_dummy_log_file(filename):
    """
    Removes the dummy log file.

    Args:
        filename (str): The name of the log file to remove.
    """
    if os.path.exists(filename):
        os.remove(filename)
