"""
API server for handling chat completions using litellm.
"""

import os
import logging
import json
import datetime
from flask import Flask, request, jsonify
from api.litellm_client import _call_litellm
from api.utils import _serialize_response, _log_request
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(os.getcwd(), "api_requests.log"),
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Ensure logging configuration is correctly set up
if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.makedirs(os.path.join(os.getcwd(), "logs"))

app = Flask(__name__)

# Initialize and compile the DSPy pipeline
pipeline = DSPyPipeline(student=ChatCompletionSignature).compile(trainset=[])


@app.route("/chat/completions", methods=["POST"])
def chat_completions():
    """Handle chat completions endpoint."""
    return _handle_chat_completions()


def _handle_chat_completions():
    try:
        data = request.get_json()
        if data is None:
            return (
                jsonify({"error": "Request body is empty or not properly formatted"}),
                400,
            )
        _log_request(data)
        model = data.get("model")
        messages = data.get("messages")
        temperature = data.get("temperature")
        max_tokens = data.get("max_tokens")

        if not model or not messages:
            return jsonify({"error": "Missing 'model' or 'messages' in request"}), 400

        logging.debug("Request  %s", data)
        try:
            # Use the DSPy pipeline to generate the response
            question = messages[-1]["content"]
            prediction = pipeline(question)
            serialized_response = _serialize_response(prediction)
            _log_request(data, serialized_response)
            return jsonify(serialized_response)
        except Exception as e:
            logging.error("Error during DSPy pipeline execution: %s", e)
            print(f"Error during DSPy pipeline execution: {e}")
            return jsonify({"error": str(e)}), 500
    except ValueError as e:
        logging.error("Error handling chat completions: %s", e)
        print(f"Error handling chat completions: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
