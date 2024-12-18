"""
This module contains signatures for various DSPy tasks.
"""

import dspy


class ChatCompletionSignature(dspy.ChainOfThought):
    """
    A signature for chat completion tasks.
    """
    def __init__(self, **kwargs):
        # super().__init__(**kwargs)
        super().__init__(self, **kwargs)

    question = dspy.InputField()
    answer = dspy.OutputField()

    def __deepcopy__(self, memo):
        return self.__class__(**self.__dict__)
