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
if exist exercises\__pycache__ rmdir /s /q exercises\__pycache__
echo ============================================
echo    Run ONE exercise (about 5 seconds)
echo ============================================
echo.
echo   A1-A6 / B1-B5 / C1-C5 / D1-D4   (basic)
echo   E1-E10                          (advanced)
echo.
set /p ex=Exercise: 
echo.
pytest exercises/day4_practice.py exercises/day7_advanced.py -k "%ex%" -v --tb=short
echo.
pause
