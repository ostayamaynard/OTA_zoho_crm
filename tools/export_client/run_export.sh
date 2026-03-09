#!/bin/bash

echo "============================================"
echo "Zoho CRM Metadata Export"
echo "============================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "[1/4] Checking Python installation..."
python3 --version
echo ""

# Check if venv exists, create if not
if [ ! -d "venv" ]; then
    echo "[2/4] Creating virtual environment..."
    python3 -m venv venv
    echo "✅ Virtual environment created"
else
    echo "[2/4] Virtual environment found"
fi
echo ""

# Activate venv
echo "[3/4] Activating virtual environment and installing packages..."
source venv/bin/activate

# Upgrade pip and install requirements
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
echo "✅ Packages installed"
echo ""

echo "[4/4] Starting export..."
echo "This will take 5-15 minutes depending on your CRM size."
echo ""
python zoho_export.py

echo ""
echo "============================================"
echo "Export complete! Check the output files."
echo "============================================"
