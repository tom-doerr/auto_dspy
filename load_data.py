import json
import logging

logging.basicConfig(level=logging.INFO)

def load_and_parse_log_data(log_file_path):
    """
    Loads and parses JSON data from a log file.

    Args:
        log_file_path (str): The path to the log file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a log entry.
    """
    log_entries = []
    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                try:
                    log_entry = json.loads(line.strip())
                    log_entries.append(log_entry)
                except json.JSONDecodeError:
                    logging.warning(f"Skipping invalid JSON line: {line.strip()}")
    except FileNotFoundError:
        logging.error(f"Log file not found: {log_file_path}")
        return None
    return log_entries


if __name__ == '__main__':
    log_file = 'api_requests.log'
    loaded_data = load_and_parse_log_data(log_file)

    if loaded_
        logging.info(f"Successfully loaded {len(loaded_data)} log entries.")
        # Example of how to access the data
        for entry in loaded_data[:5]:  # Print the first 5 entries
            logging.info(f"Log Entry: {entry}")
    else:
        logging.error("Failed to load log data.")
