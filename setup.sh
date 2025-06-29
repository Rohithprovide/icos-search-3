#!/bin/bash

# IcosSearch Setup Script
# This script sets up the environment for the IcosSearch application

set -e

echo "Setting up IcosSearch environment..."

# Create necessary directories
mkdir -p whoogle-search/static/css
mkdir -p whoogle-search/static/js
mkdir -p whoogle-search/templates
mkdir -p attached_assets

# Set permissions
chmod +x main.py

# Install UV package manager if not available
if ! command -v uv &> /dev/null; then
    echo "UV package manager not found, attempting to install..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.cargo/bin:$PATH"
fi

# Install dependencies using UV
echo "Installing Python dependencies..."
if command -v uv &> /dev/null; then
    uv sync
else
    echo "UV not available, using pip instead..."
    pip install -r whoogle-search/requirements.txt 2>/dev/null || echo "Requirements file not found, dependencies should be managed by uv"
fi

# Set environment variables
export FLASK_APP=main.py
export FLASK_ENV=production
export PYTHONPATH="${PYTHONPATH}:$(pwd)/whoogle-search"

echo "Setup complete! You can now run the application with: python main.py"
