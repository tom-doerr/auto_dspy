from flask import Flask, request, jsonify
import litellm
import os
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/chat/completions', methods=['POST'])
def chat_completions():
    try:
        data = request.get_json()
        model = data.get('model')
        messages = data.get('messages')
        temperature = data.get('temperature')
        max_tokens = data.get('max_tokens')
        
        if not model or not messages:
            return jsonify({"error": "Missing 'model' or 'messages' in request"}), 400

        logging.debug(f"Request  {data}")
        try:
            response = _call_litellm(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens
            )
            logging.debug(f"Response  {response}")
            return jsonify(response)
        except Exception as e:
            logging.error(f"Error during litellm.completion: {e}")
            return jsonify({"error": str(e)}), 500

def _call_litellm(model, messages, temperature, max_tokens):
    """
    Helper function to call litellm.completion
    """
    return litellm.completion(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get("PORT", 5000)))
