import litellm

def _call_litellm(model, messages, temperature, max_tokens):
    """
    Helper function to call litellm.completion
    """
    return litellm.completion(
        model=model, messages=messages, temperature=temperature, max_tokens=max_tokens
    )
