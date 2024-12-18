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

    def predictors(self):
        """Return the list of predictors needed for this signature."""
        return ['answer']

    def __deepcopy__(self, memo):
        """Return a deep copy of the signature."""
        return self.__class__(**self.__dict__)
