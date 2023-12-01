#!/bin/sh
# This script is used to setup the environment for the project

# Install the required packages
sudo apt-get update
sudo apt-get install python3-virtualenv

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install the required python packages
pip install -r requirements.txt

# Setup session ID
# read -p "Enter your session ID: " session_id
$session_id = read-host -prompt "Enter your session ID: "
$session_id > ~/.config/aocd/token