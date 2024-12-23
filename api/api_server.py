"""
API server for handling chat completions using litellm.
"""

import os
import json
import datetime
from flask import Flask, request, jsonify
from api.litellm_client import _call_litellm
from api.utils import _serialize_response, _log_request
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature
import dspy
import litellm
import os


# Define your LLM model using LiteLLM
model_name = "gpt-3.5-turbo" # Replace with your desired model
lm = dspy.LM(model=f"openai/{model_name}", max_tokens=500, temperature=0.1)

# Configure DSPy to use the LLM
dspy.configure(lm=lm)


# Ensure logging configuration is correctly set up
if not os.path.exists(os.path.join(os.getcwd(), "logs")):
    os.makedirs(os.path.join(os.getcwd(), "logs"))

app = Flask(__name__)

# Initialize and compile the DSPy pipeline
pipeline = DSPyPipeline(student=ChatCompletionSignature)
# Compile the pipeline with an empty trainset
pipeline.compile(trainset=[])


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

        try:
            # Use the DSPy pipeline to generate the response
            question = messages[-1]["content"]
            prediction = pipeline(question)
            serialized_response = _serialize_response(prediction)
            _log_request(data, serialized_response)
            return jsonify(serialized_response)
        except Exception as e:
            print(f"Error during DSPy pipeline execution: {e}")
            return jsonify({"error": str(e)}), 500
    except ValueError as e:
        print(f"Error handling chat completions: {e}")
        return jsonify({"error": str(e)}), 500
    
    # Initialize and compile the DSPy pipeline
    # pipeline = DSPyPipeline(student=ChatCompletionSignature).compile(trainset=[])


if __name__ == "__main__":
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
