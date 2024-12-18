import json
import logging
import re

logging.basicConfig(level=logging.INFO)


def extract_qa_pairs(log_entries):
    """
    Extracts question-answer pairs from log entries.

    Args:
        log_entries (list): A list of log entry dictionaries.

    Returns:
        list: A list of dictionaries, where each dictionary contains a question and an answer.
    """
    qa_pairs = []
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
            qa_pairs.append({"question": question, "answer": answer})
    return qa_pairs


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
    return log_entries


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
