import json
import datetime
import logging

def _serialize_response(response):
    """
    Helper function to serialize the ModelResponse object
    """
    if hasattr(response, "choices") and isinstance(response.choices, list):
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
    return response


def _log_request(data):
    """
    Helper function to log the request data with timestamp in JSON format
    """
    timestamp = datetime.datetime.now().isoformat()
    log_data = {"timestamp": timestamp, "request_data": data}
    logging.info(json.dumps(log_data))
