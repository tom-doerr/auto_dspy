#!/bin/bash

# Set the FLASK_APP environment variable
export FLASK_APP=api/api_server.py

# Set the FLASK_ENV environment variable
export FLASK_ENV=development

# Activate the virtual environment if you have one
# source path/to/your/venv/bin/activate

# Run the Flask development server
flask run --host=0.0.0.0
