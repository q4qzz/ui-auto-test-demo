@echo off
cd /d "%~dp0"
chcp 65001 >nul
title Practice ONE exercise
set PYTHONIOENCODING=utf-8
set PYTHONDONTWRITEBYTECODE=1
if not exist "%~dp0.tmp" mkdir "%~dp0.tmp"
if not exist "%~dp0.cache" mkdir "%~dp0.cache"
set TMP=%~dp0.tmp
set TEMP=%~dp0.tmp
set SE_CACHE_PATH=%~dp0.cache\selenium
call .venv\Scripts\activate.bat
echo ============================================
echo    Run ONE exercise (fast, about 5 seconds)
echo ============================================
echo.
echo   Type the exercise code and press Enter.
echo   Examples:  A1   A2   B1   C3   D4
echo.
set /p ex=Exercise: 
echo.
pytest exercises/day4_practice.py -k "%ex%" -v --tb=short
echo.
pause
