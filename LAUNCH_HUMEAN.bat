@echo off
chcp 65001 > nul
title 🧠 HUMEAN Launcher
echo.
echo 🧠 LANCEUR HUMEAN v2.0
echo ======================
echo.
echo Démarrage automatique de HUMEAN...
echo.

powershell -ExecutionPolicy Bypass -File "LAUNCH_HUMEAN.ps1"

pause
