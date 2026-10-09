@echo off
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONDONTWRITEBYTECODE=1
call .venv\Scripts\activate.bat
echo ============== DEMO (day02.py) ==============
python day02.py
echo.
echo ============== EXERCISE (day02_exercise.py) ==============
python day02_exercise.py
echo.
pause
