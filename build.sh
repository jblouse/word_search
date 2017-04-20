#!/bin/bash

# This script calls the setup.sh bash script to install prerequisite packages
# and then runs the build task using python invoke.

echo `date` :: "Calling setup script..."
. ./setup.sh
echo `date` :: "Setup script complete!"

echo `date` :: "Running build..."
invoke build
echo `date` :: "Build complete!"
