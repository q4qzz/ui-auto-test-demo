@echo off
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONDONTWRITEBYTECODE=1
if not exist "%~dp0.tmp" mkdir "%~dp0.tmp"
if not exist "%~dp0.cache" mkdir "%~dp0.cache"
set TMP=%~dp0.tmp
set TEMP=%~dp0.tmp
set SE_CACHE_PATH=%~dp0.cache\selenium
call .venv\Scripts\activate.bat
echo ============================================
echo   Running ALL tests...

echo ============================================
echo.
pytest
echo.
pause
