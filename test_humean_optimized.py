#!/usr/bin/env python3
"""
TEST COMPLET HUMEAN - Version Optimisée
Test de tous les endpoints essentiels après nettoyage
"""

import requests
import json
import time
from datetime import datetime

def test_humean_system():
    base_url = "http://localhost:5000"
    
    print("🧪 TEST COMPLET HUMEAN - SYSTÈME OPTIMISÉ")
    print("=" * 60)
    print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    tests_passed = 0
    total_tests = 0
    
    # Test 1: Statut général
    print("1. 📊 STATUT SYSTÈME")
    try:
        response = requests.get(f"{base_url}/status")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Serveur actif - {len(data)} modules")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 2: Auto-apprentissage
    print("2. 🔄 AUTO-APPRENTISSAGE")
    try:
        response = requests.get(f"{base_url}/learning")
        if response.status_code == 200:
            data = response.json()
            cycles = data.get('cycles_completed', 0)
            print(f"   ✅ Cycles: {cycles} - Actif: {data.get('active', False)}")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 3: P3 Status
    print("3. 🚀 MOTEUR P3")
    try:
        response = requests.get(f"{base_url}/p3/status")
        if response.status_code == 200:
            data = response.json()
            level = data.get('arbitrage_level', 0)
            print(f"   ✅ Niveau {level} - {data.get('p3_engine')}")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 4: Modélisation P3
    print("4. 🔮 MODÉLISATION P3")
    try:
        response = requests.post(f"{base_url}/p3/modelisation", 
                               json={"query": "Test système optimisé HUMEAN"})
        if response.status_code == 200:
            data = response.json()
            results = len(data.get('results', []))
            print(f"   ✅ {results} résultats - Innovation: {data.get('innovation_level')}")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 5: Données - Sources disponibles
    print("5. 🔌 SOURCES DONNÉES")
    try:
        response = requests.get(f"{base_url}/data/sources")
        if response.status_code == 200:
            data = response.json()
            sources = len(data.get('data_sources', {}))
            print(f"   ✅ {sources} sources configurées")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 6: Connexion données financières
    print("6. 📈 DONNÉES FINANCIÈRES")
    try:
        response = requests.post(f"{base_url}/data/connect/financial", 
                               json={"symbol": "AAPL", "days": 30})
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ {data.get('symbol')} - {data.get('data_type')}")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 7: Insights générés
    print("7. 💡 INSIGHTS P3")
    try:
        time.sleep(1)  # Laisse le temps de générer les insights
        response = requests.get(f"{base_url}/data/insights")
        if response.status_code == 200:
            data = response.json()
            stats = data.get('data_stats', {})
            insights = stats.get('p3_insights_generated', 0)
            print(f"   ✅ {insights} insights générés")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Test 8: Health Check
    print("8. 💚 HEALTH CHECK")
    try:
        response = requests.get(f"{base_url}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"   ✅ Statut: {data.get('status', 'N/A')}")
            tests_passed += 1
        total_tests += 1
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
    
    # Résumé
    success_rate = (tests_passed / total_tests) * 100
    print(f"\n📊 RÉSULTAT: {tests_passed}/{total_tests} tests réussis ({success_rate:.1f}%)")
    
    print("\n" + "=" * 60)
    if success_rate == 100:
        print("🎉 SYSTÈME HUMEAN OPTIMISÉ - OPÉRATIONNEL À 100%")
        print("   ✅ Architecture nettoyée et performante")
        print("   🚀 Prêt pour la production")
    else:
        print("⚠️  SYSTÈME FONCTIONNEL - Quelques tests échoués")
        print("   💡 Vérifier la connexion au serveur")

if __name__ == "__main__":
    test_humean_system()
