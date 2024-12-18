import json
import datetime
import os

LOG_FILE_PATH = os.path.join(os.getcwd(), "api_requests.log")
MAX_LOG_SIZE = 10 * 1024 * 1024  # 10 MB


def _serialize_response(response):
    """
    Helper function to serialize the response object.
    Handles both litellm ModelResponse and dspy.Prediction objects.
    """
    if hasattr(response, "choices") and isinstance(response.choices, list):
        # Handle litellm ModelResponse
        return {
            "choices": [
                {
                    "message": {
                        "content": choice.message.content,
                        "role": choice.message.role,
                    },
                    "finish_reason": choice.finish_reason,
                    "index": choice.index,
                }
                for choice in response.choices
            ],
            "model": response.model,
            "usage": {
                "completion_tokens": response.usage.completion_tokens,
                "prompt_tokens": response.usage.prompt_tokens,
                "total_tokens": response.usage.total_tokens,
            },
        }
    elif isinstance(response, dspy.Prediction):
        # Handle dspy.Prediction
        return {"answer": response.answer}
    return response


def _log_request(data, response=None):
    """
    Helper function to log the request data with timestamp in JSON format
    """
    timestamp = datetime.datetime.now().isoformat()
    log_data = {"timestamp": timestamp, "request_data": data}
    if response:
        log_data["response_data"] = response
    
    _write_to_log_file(log_data)


def _write_to_log_file(log_data):
    """
    Helper function to write log data to the log file.
    """
    # Check if log file exists and is too large
    if os.path.exists(LOG_FILE_PATH) and os.path.getsize(LOG_FILE_PATH) > MAX_LOG_SIZE:
        _rotate_log_file()
    
    try:
        with open(LOG_FILE_PATH, "a") as f:
            json.dump(log_data, f)
            f.write("\n")  # Add a newline for each JSON object
    except IOError as e:
        print(f"Error writing to log file: {e}")


def _rotate_log_file():
    """
    Helper function to rotate the log file.
    """
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    rotated_log_file = f"{LOG_FILE_PATH}.{timestamp}"
    os.rename(LOG_FILE_PATH, rotated_log_file)
    print(f"Log file rotated to: {rotated_log_file}")
