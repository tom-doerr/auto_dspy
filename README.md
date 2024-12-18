# Auto-DSPy: Automated DSPy Pipeline

This project provides an automated pipeline for training and running DSPy models, integrated with a Flask API for easy access.

## Overview

The project consists of the following main components:

-   **`api/`**: Contains the Flask API server, which handles chat completions using DSPy.
-   **`dspy_pipeline/`**: Contains the DSPy pipeline logic, including custom signatures, data loading, and training.
-   **`tests/`**: Contains unit tests for the API server and DSPy pipeline.
-   **`train_pipeline.py`**: A script to train the DSPy pipeline using logged data.
-   **`run_inference.py`**: A script to run inference using the API.

## Setup

### Prerequisites

-   Python 3.10+
-   pip
-   A virtual environment (recommended)

### Installation

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd auto_dspy
    ```
2.  Create a virtual environment:

    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:

    ```bash
    source venv/bin/activate
    ```
4.  Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Environment Variables

-   `FLASK_APP`: Set to `api/api_server.py`
-   `FLASK_ENV`: Set to `development`
-   `PORT`: (Optional) Set the port for the Flask app (default is 5000)

## Running the Project

### Start the API Server

```bash
./start_server.sh
```

This will start the Flask development server.

### Run Inference

To run inference, use the `run_inference.py` script:

```bash
python run_inference.py
```

This script will send requests to the API and print the responses.

### Train the DSPy Pipeline

To train the DSPy pipeline, use the `train_pipeline.py` script:

```bash
python train_pipeline.py
```

This script will load log data from `api_requests.log`, create a DSPy dataset, and compile the pipeline.

## Testing

To run the tests, use the following command:

```bash
pytest -v
```

## Contributing

Contributions are welcome! Please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with clear messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

## License

This project is licensed under the [LICENSE](LICENSE) file.

## Contact

If you have any questions or suggestions, please feel free to open an issue or contact the maintainers.
