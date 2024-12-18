"""
This module contains signatures for various DSPy tasks.
"""

import dspy
from dspy.functional import chain_of_thought


class ChatCompletionSignature(ChainOfThought):
    """
    A signature for chat completion tasks.
    """

    question = dspy.InputField()
    answer = dspy.OutputField()
