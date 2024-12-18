from flask import Flask, request, jsonify
import litellm
import os
import logging
import json
import datetime

logging.basicConfig(level=logging.INFO, filename='api_requests.log', filemode='a')

app = Flask(__name__)


@app.route("/chat/completions", methods=["POST"])
def chat_completions():
    return _handle_chat_completions()


def _call_litellm(model, messages, temperature, max_tokens):
    """
    Helper function to call litellm.completion
    """
    return litellm.completion(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )


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
    log_data = {
        "timestamp": timestamp,
        "request_data": data
    }
    logging.info(json.dumps(log_data))


def _handle_chat_completions():
    try:
        data = request.get_json()
        _log_request(data)
        model = data.get("model")
        messages = data.get("messages")
        temperature = data.get("temperature")
        max_tokens = data.get("max_tokens")

        if not model or not messages:
            return jsonify({"error": "Missing 'model' or 'messages' in request"}), 400

        logging.debug(f"Request  {data}")
        try:
            response = _call_litellm(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            logging.debug(f"Response  {response}")
            return jsonify(response)
        except Exception as e:
            logging.error(f"Error during litellm.completion: {e}")
            return jsonify({"error": str(e)}), 500
    except Exception as e:
        logging.error(f"Error handling chat completions: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))