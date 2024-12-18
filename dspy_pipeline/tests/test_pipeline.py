import pytest
import dspy
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature
from dspy_pipeline.utils import dummy_metric
from dspy.functional import chain_of_thought




def test_dspy_pipeline_not_compiled():
    """Test that the pipeline raises an error if not compiled."""
    # Initialize the pipeline without compiling
    pipeline = DSPyPipeline(student=ChatCompletionSignature)

    # Test that forward pass raises an error
    with pytest.raises(
        ValueError, match=r"Pipeline not compiled yet. Call compile\(\) first."
    ):
        pipeline("What is the capital of Germany?")


def test_dspy_pipeline_compile_and_forward():
    """Test compiling and running the DSPy pipeline."""
    # Create a dummy trainset
    trainset = [
        dspy.Example(question="What is the capital of France?"),
        dspy.Example(question="What is the largest planet in our solar system?"),
    ]

    # Initialize and compile the pipeline
    pipeline = DSPyPipeline(student=ChatCompletionSignature).compile(trainset=trainset)

    # Test that forward pass returns a prediction
    prediction = pipeline("What is the capital of France?")
    assert isinstance(prediction, dspy.Prediction)


def test_dspy_pipeline_compile_empty_trainset():
    """Test that the pipeline raises an error if the trainset is empty."""
    # Initialize the pipeline
    pipeline = DSPyPipeline(student=ChatCompletionSignature)

    # Test that compile raises an error
    with pytest.raises(ValueError, match=r"trainset cannot be empty"):
        pipeline.compile(trainset=[])


