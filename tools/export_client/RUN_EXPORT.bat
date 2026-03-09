@echo off
echo ============================================
echo Zoho CRM Metadata Export
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

echo [1/3] Checking Python installation...
python --version
echo.

echo [2/3] Installing required packages...
pip install -r requirements.txt
echo.

echo [3/3] Starting export...
echo This will take 5-15 minutes depending on your CRM size.
echo.
python zoho_export.py

echo.
echo ============================================
echo Export complete! Check the output files.
echo ============================================
pause
