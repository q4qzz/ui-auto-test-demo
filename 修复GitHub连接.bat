@echo off
chcp 65001 >nul
title Fix GitHub connection
net session >nul 2>&1
if %errorlevel% neq 0 (
  echo.
  echo  ==================================================
  echo    ADMINISTRATOR RIGHTS REQUIRED
  echo  ==================================================
  echo.
  echo    Please CLOSE this window, then:
  echo.
  echo      1. RIGHT-CLICK this file
  echo      2. Choose "Run as administrator"
  echo.
  echo  ==================================================
  echo.
  pause
  exit /b 1
)
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0fix_github_hosts.ps1"
echo.
pause
