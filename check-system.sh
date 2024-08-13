#!/bin/bash

# Function to check if a package is installed
check_package() {
    dpkg -s "$1" &> /dev/null
    
    if [ $? -eq 0 ]; then
        echo "$1 is already installed."
    else
        echo "$1 is not installed. Installing..."
        sudo apt-get install -y "$1"
    fi
}

# Check and install system packages
check_package python3
check_package python3-venv
check_package python3-pip

# Check for pip packages and install if necessary
pip_check_install() {
    pip3 show "$1" &> /dev/null
    
    if [ $? -eq 0 ]; then
        echo "Python package $1 is already installed."
    else
        echo "Python package $1 is not installed. Installing..."
        pip3 install "$1" --break-system-packages
    fi
}

# Check and install pip packages
pip_check_install python-dotenv
pip_check_install tailer
pip_check_install sendgrid

echo "All necessary packages are checked and installed."
echo "intialising Virtual Environment"
python3 -m venv .
echo "Virtual Environment created"
echo "Running Script"
python3 monitor.py
