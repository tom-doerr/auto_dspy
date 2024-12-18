import json
import datetime
import logging

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
    logging.info(json.dumps(log_data))
