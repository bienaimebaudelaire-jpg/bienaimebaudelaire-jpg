# humean_launcher.ps1
# Lanceur automatique pour HUMEAN - Double-cliquez pour tout démarrer

Write-Host "🧠 LANCEUR HUMEAN v2.0" -ForegroundColor Magenta
Write-Host "======================" -ForegroundColor Magenta

# Vérifier si Python est disponible
try {
    $pythonVersion = python --version
    Write-Host "✅ Python trouvé: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python n'est pas installé ou n'est pas dans le PATH" -ForegroundColor Red
    Write-Host "💡 Téléchargez Python depuis: https://python.org" -ForegroundColor Yellow
    pause
    exit
}

# Se déplacer dans le dossier HUMEAN
$humeanPath = "C:\Users\Big Boss\HumeanProject\bienaimebaudelaire-jpg"
if (Test-Path $humeanPath) {
    Set-Location $humeanPath
    Write-Host "📁 Dossier HUMEAN: $humeanPath" -ForegroundColor Green
} else {
    Write-Host "❌ Dossier HUMEAN introuvable: $humeanPath" -ForegroundColor Red
    pause
    exit
}

# Vérifier les dépendances
Write-Host "`n📦 Vérification des dépendances..." -ForegroundColor Yellow
try {
    python -c "import flask" 2>$null
    Write-Host "✅ Flask installé" -ForegroundColor Green
} catch {
    Write-Host "❌ Flask non installé - Installation..." -ForegroundColor Yellow
    pip install flask
}

try {
    python -c "import requests" 2>$null
    Write-Host "✅ Requests installé" -ForegroundColor Green
} catch {
    Write-Host "❌ Requests non installé - Installation..." -ForegroundColor Yellow
    pip install requests
}

# Démarrer le serveur de contrôle
Write-Host "`n🎛️  Démarrage du serveur de contrôle..." -ForegroundColor Cyan
$controlServer = Start-Process python -ArgumentList "humean_control_server.py" -PassThru

# Attendre que le serveur de contrôle soit prêt
Start-Sleep -Seconds 3

# Démarrer HUMEAN via le serveur de contrôle
Write-Host "🚀 Démarrage de HUMEAN..." -ForegroundColor Cyan
try {
    $response = Invoke-RestMethod -Uri "http://localhost:5001/api/start-server" -Method POST
    Write-Host "✅ $($response.message)" -ForegroundColor Green
} catch {
    Write-Host "⚠️  Impossible de démarrer via API: $_" -ForegroundColor Yellow
    Write-Host "💡 Démarrage manuel..." -ForegroundColor Yellow
    $humeanServer = Start-Process python -ArgumentList "humean_server.py" -PassThru
}

# Ouvrir le panneau de contrôle
Write-Host "`n🌐 Ouverture du panneau de contrôle..." -ForegroundColor Cyan
Start-Process "http://localhost:5001"

Write-Host "`n🎉 HUMEAN EST MAINTENANT OPÉRATIONNEL !" -ForegroundColor Green
Write-Host "======================================" -ForegroundColor Green
Write-Host "🎛️  Panneau de contrôle: http://localhost:5001" -ForegroundColor White
Write-Host "📊 Dashboard: http://localhost:5000" -ForegroundColor White
Write-Host "🛑 Pour arrêter: Fermez les fenêtres ou utilisez le panneau de contrôle" -ForegroundColor Yellow

Write-Host "`n⏳ Les serveurs démarrent..." -ForegroundColor Cyan

# Garder le script actif
Write-Host "`n🔄 Le launcher reste actif. Fermez cette fenêtre pour tout arrêter." -ForegroundColor Magenta
pause
