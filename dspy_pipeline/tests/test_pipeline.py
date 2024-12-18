import pytest
import dspy
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature


def test_dspy_pipeline_compile_and_forward():
    """Test compiling and running the DSPy pipeline."""
    # Create a dummy trainset
    trainset = [
        dspy.Example(question="What is the capital of France?"),
        dspy.Example(question="What is the largest planet in our solar system?"),
    ]

    # Define a dummy metric
    def dummy_metric(gold, pred, trace=None):
        return 1

    # Initialize and compile the pipeline
    pipeline = DSPyPipeline(metric=dummy_metric).compile(trainset=trainset)

    # Test forward pass
    question = "What is the capital of Germany?"
    prediction = pipeline(question)

    assert prediction is not None
    assert isinstance(prediction, dspy.Prediction)
    assert hasattr(prediction, "answer")


def test_dspy_pipeline_not_compiled():
    """Test that the pipeline raises an error if not compiled."""

    # Define a dummy metric
    def dummy_metric(gold, pred, trace=None):
        return 1

    # Initialize the pipeline without compiling
    pipeline = DSPyPipeline(metric=dummy_metric)

    # Test that forward pass raises an error
    with pytest.raises(
        ValueError, match="Pipeline not compiled yet. Call compile() first."
    ):
        pipeline("What is the capital of Germany?")
