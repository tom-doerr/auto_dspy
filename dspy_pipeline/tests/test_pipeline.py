import pytest
import dspy
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature
from dspy_pipeline.utils import dummy_metric




def test_dspy_pipeline_not_compiled():
    """Test that the pipeline raises an error if not compiled."""
    # Initialize the pipeline without compiling
    pipeline = DSPyPipeline(student=ChatCompletionSignature)

    # Test that forward pass raises an error
    with pytest.raises(
        ValueError, match=r"Pipeline not compiled yet. Call compile\(\) first."
    ):
        pipeline("What is the capital of Germany?")


