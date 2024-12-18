import requests
import json

def run_inference(api_url, model, messages, temperature=0.7, max_tokens=150):
    """
    Runs inference on the API.

    Args:
        api_url (str): The URL of the API endpoint.
        model (str): The model to use for inference.
        messages (list): The list of messages for the chat.
        temperature (float): The temperature for the model.
        max_tokens (int): The maximum number of tokens for the response.

    Returns:
        dict: The JSON response from the API.
    """
    headers = {"Content-Type": "application/json"}
    data = {
        "model": model,
        "messages": messages,
    }

    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")
        return None


if __name__ == "__main__":
    api_url = "http://0.0.0.0:5000/chat/completions"  # Replace with your API URL
    model = "gpt-3.5-turbo"  # Replace with your desired model
    messages = [{"role": "user", "content": "What is the capital of France?"}]

    response = run_inference(api_url, model, messages)

    if response:
        print("API Response:")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to get a response from the API.")