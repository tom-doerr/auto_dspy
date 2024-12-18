import requests
import json
import time

def trigger_training(api_url, model, messages):
    """
    Triggers the training of the DSPy pipeline by making a request to the API.

    Args:
        api_url (str): The URL of the API endpoint.
        model (str): The model to use for inference.
        messages (list): The list of messages for the chat.

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

    # Initial request to log data
    messages = [{"role": "user", "content": "What is the capital of France?"}]
    print("Making initial request to log data...")
    response = trigger_training(api_url, model, messages)
    if response:
        print("Initial API Response:")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to get a response from the API.")

    time.sleep(2) # Wait for the log to be written

    # Second request to trigger training
    messages = [{"role": "user", "content": "What is the capital of Germany?"}]
    print("Making second request to trigger training...")
    response = trigger_training(api_url, model, messages)
    if response:
        print("Second API Response:")
        print(json.dumps(response, indent=4))
    else:
        print("Failed to get a response from the API.")
