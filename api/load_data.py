import json
import logging
import re

logging.basicConfig(level=logging.INFO)



def load_and_parse_log_data(log_file_path):
    """
    Loads and parses log data from a file.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a log entry.
              Returns None if the file is not found.
    """
    log_entries = []
    try:
        with open(log_file_path, "r") as f:
            for line in f:
                try:
                    log_entry = json.loads(line)
                    log_entries.append(log_entry)
                except json.JSONDecodeError:
                    logging.warning(f"Skipping invalid JSON line: {line.strip()}")
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        return None
def _extract_question(log_entry):
    """
    Extracts the question from a log entry.

    Args:
        log_entry (dict): A dictionary representing a log entry.

    Returns:
        str: The extracted question, or None if not found.
    """
    request_data = log_entry.get("request_data", {})
    messages = request_data.get("messages", [])
    if not messages:
        return None

    for message in reversed(messages):
        if message.get("role") == "user":
            return message.get("content")
    return None


def _extract_answer(log_entry):
    """
    Extracts the answer from a log entry.

    Args:
        log_entry (dict): A dictionary representing a log entry.

    Returns:
        str: The extracted answer, or None if not found.
    """
    response_data = log_entry.get("response_data", {})
    if response_data and "choices" in response_
        first_choice = response_data["choices"][0]
        if "message" in first_choice and first_choice["message"].get("role") == "assistant":
            return first_choice["message"].get("content")
    return None


def extract_qa_pairs(log_entries):
    """
    Extracts question-answer pairs from a list of log entries.

    Args:
        log_entries (list): A list of dictionaries, where each dictionary represents a log entry.

    Returns:
        list: A list of dictionaries, where each dictionary contains a question and an answer.
    """
    qa_pairs = []
    for entry in log_entries:
        question = _extract_question(entry)
        answer = _extract_answer(entry)
        if question and answer:
            qa_pairs.append({"question": question, "answer": answer})
    return qa_pairs




if __name__ == "__main__":
    log_file = "api_requests.log"
    loaded_data = load_and_parse_log_data(log_file)

    if loaded_data is not None:
        logging.info(f"Successfully loaded {len(loaded_data)} log entries.")
        # Example of how to access the data
        for entry in loaded_data[:5]:  # Print the first 5 entries
            logging.info(f"Log Entry: {entry}")
    else:
        logging.error("Failed to load log data.")
