#!/bin/bash

VENV_PATH="$HOME/scd30venv"

# Check if the virtual environment exists, if not, create it
if [ ! -d "$VENV_PATH" ]; then
    python3 -m venv "$VENV_PATH"

	# Activate the virtual environment
	source "$VENV_PATH/bin/activate"

	# Ensure required dependencies are installed
	pip install -r ./modules/MMM-SCD-30/requirements.txt
fi

# Activate the virtual environment
source "$VENV_PATH/bin/activate"

# Run the Python script
python3 ./modules/MMM-SCD-30/scd_30.py