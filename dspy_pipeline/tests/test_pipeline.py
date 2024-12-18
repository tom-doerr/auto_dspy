import pytest
import dspy
from ...dspy_pipeline.pipeline import DSPyPipeline  # Ensure this path is correct
from ...dspy_pipeline.signatures import ChatCompletionSignature
from ...dspy_pipeline.utils import dummy_metric


def test_dspy_pipeline_compile_and_forward():
    """Test compiling and running the DSPy pipeline."""
    # Create a dummy trainset
    trainset = [
        dspy.Example(question="What is the capital of France?"),
        dspy.Example(question="What is the largest planet in our solar system?"),
    ]

    # Initialize and compile the pipeline
    pipeline = DSPyPipeline(student=ChatCompletionSignature()).compile(
        trainset=trainset
    )

    # Test forward pass
    question = "What is the capital of Germany?"
    prediction = pipeline(question)

    assert prediction is not None
    assert isinstance(prediction, dspy.Prediction)
    assert hasattr(prediction, "answer")


def test_dspy_pipeline_not_compiled():
    """Test that the pipeline raises an error if not compiled."""
    # Initialize the pipeline without compiling
    pipeline = DSPyPipeline(student=ChatCompletionSignature())

    # Test that forward pass raises an error
    with pytest.raises(
        ValueError, match="Pipeline not compiled yet. Call compile() first."
    ):
        pipeline("What is the capital of Germany?")


def test_dspy_pipeline_compile_and_forward_with_custom_student():
    """Test compiling and running the DSPy pipeline with a custom student signature."""

    class CustomSignature(dspy.Signature):
        question = dspy.InputField()
        answer = dspy.OutputField()

    # Create a dummy trainset
    trainset = [
        dspy.Example(question="What is the capital of France?"),
        dspy.Example(question="What is the largest planet in our solar system?"),
    ]

    # Initialize and compile the pipeline
    pipeline = DSPyPipeline(student=CustomSignature()).compile(trainset=trainset)

    # Test forward pass
    question = "What is the capital of Germany?"
    prediction = pipeline(question)

    assert prediction is not None
    assert isinstance(prediction, dspy.Prediction)
    assert hasattr(prediction, "answer")
