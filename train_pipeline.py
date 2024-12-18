"""
This script loads log data, creates a DSPy dataset, and compiles the DSPy pipeline.
"""

import os
import logging
import dspy
from dspy_pipeline.pipeline import DSPyPipeline
from dspy_pipeline.signatures import ChatCompletionSignature
from dspy_pipeline.data_loader import create_dspy_dataset_from_logs

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Define your LLM model using LiteLLM
model_name = "gpt-3.5-turbo"  # Replace with your desired model
lm = dspy.LM(model=f"openai/{model_name}", max_tokens=500, temperature=0.1)

# Configure DSPy to use the LLM
dspy.configure(lm=lm)

def train_dspy_pipeline():
    """
    Loads log data, creates a DSPy dataset, and compiles the DSPy pipeline.
    """
    log_file_path = "api_requests.log"  # Path to your log file
    logging.info(f"Loading log data from: {log_file_path}")
    trainset = create_dspy_dataset_from_logs(log_file_path)

    if not trainset:
        logging.warning("No training data found in log file. Skipping training.")
        return

    logging.info(f"Training data loaded. Number of examples: {len(trainset)}")

    # Initialize and compile the DSPy pipeline
    pipeline = DSPyPipeline(student=ChatCompletionSignature).compile(trainset=trainset)
    logging.info("DSPy pipeline compiled successfully.")


if __name__ == "__main__":
    train_dspy_pipeline()
    logging.info("Training script finished.")
    
