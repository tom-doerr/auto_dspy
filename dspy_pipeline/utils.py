"""
Utility functions for the DSPy pipeline.
"""

def dummy_metric(gold, pred, trace=None):
    """
    A dummy metric function that always returns 1.

    Args:
        gold: The expected output (unused).
        pred: The predicted output (unused).
        trace: Additional trace information (unused).

    Returns:
        int: Always returns 1.
    """
    return 1
