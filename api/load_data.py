import json
import logging
import re

logging.basicConfig(level=logging.INFO)


def load_and_parse_log_data(log_file_path):
    """
    Loads and parses JSON data from a log file, filtering out non-JSON lines
    and only including entries with a response.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a log entry.
    """
    log_entries = []
    try:
        with open(log_file_path, "r") as log_file:
            for line_number, line in enumerate(log_file, start=1):
                line = line.strip()
                if line.startswith('{') and line.endswith('}'):
                    try:
                        log_entry = json.loads(line)
                        if "response_data" in log_entry:
                            log_entries.append(log_entry)
                            logging.debug(f"Parsed log entry at line {line_number}: {log_entry}")
                        else:
                            logging.debug(f"Skipping log entry without response at line {line_number}: {line}")
                    except json.JSONDecodeError:
                        logging.warning(f"Skipping invalid JSON line at line {line_number}: {line}")
                else:
                    logging.debug(f"Skipping non-JSON line at line {line_number}: {line}")
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
