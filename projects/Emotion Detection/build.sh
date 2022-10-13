#!/bin/bash

# Change current directory to project directory. 
CURRENT_PATH="$( cd "$(dirname "$0")" || exit ; pwd -P )"
cd "$CURRENT_PATH" || exit


# Upgrade Python 
python3 -m pip install --upgrade pip

# Check version of pip
# Version must be below 18.XX and compatible with Python 3.4+
pip --version

# Install dependencies
pip install -I opencv-python
pip install -I dlib==19.21.1
pip install -I pandas
pip install -I scikit-learn
