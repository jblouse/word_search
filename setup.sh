#!/bin/bash

# This script installs the prerequisite python packages in a python virtualenv.
# The pip, invoke and virtualenv packages are installed on the host machine as
# this setup process uses python invoke and python virtualenv.
# sudo is required for one or more of the required python packages.

echo `date` :: "Installing prerequisite python packages (pip, invoke, and virtualenv)..."
sudo -H pip install pip invoke virtualenv
echo `date` :: "Prerequisite install complete!"

echo `date` :: "Running setup..."
invoke setup
echo `date` :: "Setup complete!"
