"""
This module contains signatures for various DSPy tasks.
"""

import dspy


class ChatCompletionSignature(dspy.Signature):
    """
    A signature for chat completion tasks.
    """

    question = dspy.InputField()
    answer = dspy.OutputField()

    def predictors(self) -> list[str]:
        """Return the list of predictors needed for this signature."""
        return ["answer"]

