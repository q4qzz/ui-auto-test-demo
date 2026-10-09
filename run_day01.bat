@echo off
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONDONTWRITEBYTECODE=1
call .venv\Scripts\activate.bat
python day01.py
echo.
pause
