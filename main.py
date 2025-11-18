#!/usr/bin/env python3
"""
🚀 HUMEAN PROJECT - POINT D'ENTRÉE PRINCIPAL
Système d'IA Auto-améliorant avec Architecture Modulaire
"""

import sys
import os
import webbrowser
import subprocess
import logging
import time

# Configuration des paths et encodage
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
sys.path.insert(0, src_path)

# Configurer l'encodage pour les émojis
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

def clear_screen():
    """Nettoyer l'écran"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Afficher la bannière"""
    banner = r'''
 _    _ _   _ _____  _    _  ___   __  __  
| |  | | | | |  __ \| |  | |/ _ \ |  \/  | 
| |__| | | | | |__) | |  | | | | || \  / | 
|  __  | | | |  ___/| |  | | | | || |\/| | 
| |  | | |_| | |    | |__| | |_| || |  | | 
|_|  |_|\___/|_|     \____/ \___/ |_|  |_| 
                                            
    Système d'IA Auto-Améliorant - v1.0
    '''
    print(banner)

def start_web_server():
    """Démarrer le serveur web - VERSION SIMPLIFIÉE"""
    print("🌐 Démarrage du serveur HUMEAN...")
    print("⏳ Initialisation en cours...")
    
    try:
        # Import simple qui démarre automatiquement le serveur
        import core.humean_server
        
        print("✅ Système HUMEAN initialisé avec succès!")
        print("")
        print("📍 Serveur accessible sur: http://127.0.0.1:5000")
        print("")
        print("📋 Endpoints disponibles:")
        print("   - GET  /              → Dashboard principal")
        print("   - POST /api/query     → Interroger l'IA")
        print("   - GET  /api/health    → Statut du système")
        print("   - POST /api/feedback  → Envoyer du feedback")
        print("   - GET  /api/models    → Modèles disponibles")
        print("   - GET  /api/system-status → Statut détaillé")
        print("")
        print("🔧 Composants actifs:")
        print("   - Base de données connectée")
        print("   - Modèle IA humean_core initialisé") 
        print("   - Système d'auto-amélioration actif")
        print("")
        print("🛑 Appuyez sur Ctrl+C pour arrêter le serveur")
        print("="*50)
        
        # Maintenir le programme en vie
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n👋 Arrêt du serveur HUMEAN...")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        input("Appuyez sur Entrée pour continuer...")

def run_tests():
    """Exécuter les tests"""
    print("🧪 Exécution des tests unitaires...")
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests/", "-v"], 
            capture_output=True, 
            text=True, 
            encoding='utf-8'
        )
        print(result.stdout)
        if result.stderr:
            print("Erreurs:", result.stderr)
    except Exception as e:
        print(f"❌ Erreur lors de l'exécution des tests: {e}")

def system_status():
    """Afficher le statut du système"""
    print("🔍 Vérification du statut système...")
    try:
        import requests
        response = requests.get("http://127.0.0.1:5000/api/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Serveur actif et en bonne santé")
            print(f"   📊 Statut: {data.get('status', 'N/A')}")
            print(f"   🕐 Timestamp: {data.get('timestamp', 'N/A')}")
            components = data.get('components', {})
            for comp, status in components.items():
                print(f"   🔧 {comp}: {status}")
        else:
            print(f"❌ Serveur accessible mais erreur: {response.status_code}")
    except Exception as e:
        print(f"❌ Serveur non démarré: {e}")
        print("💡 Démarrez d'abord le serveur avec l'option 1")

def open_dashboard():
    """Ouvrir le dashboard dans le navigateur"""
    print("🌐 Ouverture du dashboard HUMEAN...")
    try:
        webbrowser.open("http://127.0.0.1:5000")
        print("✅ Dashboard ouvert dans le navigateur par défaut")
        print("💡 Si la page ne s'ouvre pas, visitez manuellement:")
        print("   http://127.0.0.1:5000")
        
        # Vérifier que le serveur répond
        print("\\n🔍 Vérification de l'accessibilité...")
        import requests
        try:
            response = requests.get("http://127.0.0.1:5000/", timeout=5)
            if response.status_code == 200:
                print("✅ Serveur accessible et répond correctement")
            else:
                print(f"⚠️  Serveur accessible mais code: {response.status_code}")
        except:
            print("❌ Le serveur ne semble pas démarré")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'ouverture: {e}")

def direct_server_start():
    """Démarrage direct du serveur sans menu"""
    print("🚀 DÉMARRAGE DIRECT DU SERVEUR HUMEAN")
    print("=" * 40)
    
    try:
        # Méthode directe - importer le module qui démarre automatiquement
        print("⏳ Chargement du système HUMEAN...")
        import core.humean_server
        
        print("\\n🎉 SYSTÈME HUMEAN OPÉRATIONNEL!")
        print("=" * 40)
        print("📍 URL: http://127.0.0.1:5000")
        print("📊 Dashboard: http://127.0.0.1:5000/")
        print("❤️  Santé: http://127.0.0.1:5000/api/health")
        print("\\n🔧 Le système inclut:")
        print("   - Serveur web Flask")
        print("   - Base de données SQLite")
        print("   - Modèle IA humean_core")
        print("   - Système d'auto-amélioration")
        print("\\n🛑 Appuyez sur Ctrl+C pour arrêter")
        print("=" * 40)
        
        # Maintenir l'exécution
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\\n👋 Arrêt du serveur HUMEAN")
    except Exception as e:
        print(f"❌ Erreur: {e}")

def main():
    """Menu principal SIMPLIFIÉ"""
    while True:
        clear_screen()
        print_banner()
        
        print("\\n" + "="*50)
        print("📋 MENU PRINCIPAL - HUMEAN PROJECT")
        print("="*50)
        
        print("\\n1. 🌐 Lancer le serveur web")
        print("2. 🚀 Démarrage direct (recommandé)")
        print("3. 🧪 Exécuter les tests unitaires") 
        print("4. 🔍 Statut du serveur")
        print("5. 📊 Ouvrir le dashboard")
        print("0. 🚪 Quitter")
        
        choice = input("\\n🎯 Choisissez une option (0-5): ").strip()
        
        if choice == "1":
            start_web_server()
        elif choice == "2":
            direct_server_start()
        elif choice == "3":
            run_tests()
            input("\\nAppuyez sur Entrée pour continuer...")
        elif choice == "4":
            system_status()
            input("\\nAppuyez sur Entrée pour continuer...")
        elif choice == "5":
            open_dashboard()
            input("\\nAppuyez sur Entrée pour continuer...")
        elif choice == "0":
            print("👋 À bientôt sur HUMEAN PROJECT!")
            break
        else:
            print("❌ Option invalide, veuillez réessayer.")
            input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    main()
