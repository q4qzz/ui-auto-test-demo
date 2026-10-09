@echo off
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONIOENCODING=utf-8
set PYTHONDONTWRITEBYTECODE=1
echo ============================================
echo   Running automated tests...
echo ============================================
echo.
call .venv\Scripts\activate.bat
pytest
echo.
echo ============================================
echo   Done. Report: reports\report.html
echo ============================================
echo.
pause
