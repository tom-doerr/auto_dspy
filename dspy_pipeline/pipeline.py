"""
This module contains the DSPyPipeline class, which is responsible for compiling and running DSPy pipelines.
"""

import dspy
from dspy.teleprompt import MIPROv2
from dspy_pipeline.utils import dummy_metric


class DSPyPipeline(dspy.Module):
    """
    A class to represent a DSPy pipeline, which compiles and runs DSPy pipelines using MIPROv2.
    """

    def __init__(self, metric=dummy_metric, auto="light", student=None):
        super().__init__()
        self.mipro_optimizer = MIPROv2(metric=metric, auto=auto)
        self.predictor = None
        self.student_class = student

    def forward(self, question):
        """
        Executes the forward pass of the pipeline.

        Args:
            question (str): The input question to process.

        Returns:
            dspy.Prediction: The prediction result.

        Raises:
            ValueError: If the pipeline is not compiled yet.
        """
        if self.predictor is None:
            raise ValueError("Pipeline not compiled yet. Call compile() first.")
        return self.predictor(question=question)

    def compile(self, trainset, max_bootstrapped_demos=3, max_labeled_demos=4):
        """
        Compiles the DSPy pipeline using MIPROv2.

        Args:
            trainset (list): A list of dspy.Example objects.
            max_bootstrapped_demos (int): Maximum number of bootstrapped demos.
            max_labeled_demos (int): Maximum number of labeled demos.
        """
        if self.student_class is None:
            raise ValueError(
                "Student signature not provided. Pass a student signature to the constructor."
            )
        if not trainset:
            import logging
            logging.warning("No training data provided. Skipping training.")
            self.predictor = self.student_class()
            return self
        self.predictor = self.mipro_optimizer.compile(
            student=self.student_class,
            trainset=trainset,
            max_bootstrapped_demos=max_bootstrapped_demos,
            max_labeled_demos=max_labeled_demos,
            requires_permission_to_run=False,
        )
        return self
