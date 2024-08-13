#!/bin/bash

# Set the virtual environment directory name
VENV_DIR="./bin"

# Check if the virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists."
else
    echo "Creating virtual environment..."
    python3 -m venv "$VENV_DIR"
fi

# Activate the virtual environment
source "./bin/activate"

# Check if the virtual environment is active
if [ "$VIRTUAL_ENV" != "" ]; then
    echo "Virtual environment is activated."
    # Run the Python script
    echo "running script monitor.py..."
    echo "displaying auth logs to stdoutput...."
    echo -e "\n\n"
    python3 monitor.py
else
    echo "Failed to activate virtual environment."
    exit 1
fi
