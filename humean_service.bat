@echo off
chcp 65001 > nul
title 🧠 HUMEAN Service Manager v2.0

:menu
cls
echo.
echo ========================================
echo      🧠 HUMEAN SERVICE MANAGER v2.0
echo ========================================
echo.
echo 1. 🚀 Démarrer HUMEAN (Launcher Auto)
echo 2. ⏹️  Arrêter HUMEAN
echo 3. 🔄 Redémarrer HUMEAN
echo 4. 📊 Ouvrir Dashboard
echo 5. 🎛️  Ouvrir Panneau de Contrôle
echo 6. 🐍 Démarrer Manuellement
echo 7. ❌ Quitter
echo.
set /p choice="Choisissez une option [1-7]: "

if "%choice%"=="1" goto auto_launch
if "%choice%"=="2" goto stop_server
if "%choice%"=="3" goto restart_server
if "%choice%"=="4" goto open_dashboard
if "%choice%"=="5" goto open_control_panel
if "%choice%"=="6" goto manual_start
if "%choice%"=="7" goto exit

goto menu

:auto_launch
echo.
echo 🚀 Démarrage automatique de HUMEAN...
LAUNCH_HUMEAN.bat
goto menu

:stop_server
echo.
echo ⏹️  Arrêt de HUMEAN...
curl -X POST http://localhost:5001/api/stop-server || echo Le serveur de contrôle est hors ligne
timeout /t 3 /nobreak > nul
goto menu

:restart_server
echo.
echo 🔄 Redémarrage de HUMEAN...
curl -X POST http://localhost:5001/api/restart-server || echo Démarrage manuel nécessaire
timeout /t 5 /nobreak > nul
goto menu

:open_dashboard
echo.
echo 📊 Ouverture du dashboard...
start http://localhost:5000
goto menu

:open_control_panel
echo.
echo 🎛️  Ouverture du panneau de contrôle...
start http://localhost:5001
goto menu

:manual_start
echo.
echo 🐍 Démarrage manuel du serveur HUMEAN...
python humean_server.py
goto menu

:exit
echo.
echo 🧠 Au revoir !
timeout /t 2 > nul
exit
