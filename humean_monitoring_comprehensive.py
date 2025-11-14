#!/usr/bin/env python3
"""
DASHBOARD HUMEAN COMPLET - API + P3
Monitoring en temps réel du système cognitif HUMEAN
"""

import requests
import time
import os
import subprocess
import json
from datetime import datetime

def get_humean_metrics():
    """Récupère les métriques réelles du système HUMEAN"""
    base_url = "http://localhost:5000"
    metrics = {}
    
    try:
        # Statut des modules
        status_response = requests.get(f"{base_url}/status", timeout=5)
        if status_response.status_code == 200:
            metrics['modules'] = status_response.json()
        
        # Métriques d'apprentissage
        learning_response = requests.get(f"{base_url}/learning", timeout=5)
        if learning_response.status_code == 200:
            learning_data = learning_response.json()
            metrics['learning'] = learning_data
            
        # Statut P3
        p3_status_response = requests.get(f"{base_url}/p3/status", timeout=5)
        if p3_status_response.status_code == 200:
            metrics['p3'] = p3_status_response.json()
            
    except Exception as e:
        metrics['error'] = str(e)
    
    return metrics

def test_p3_modelisation():
    """Test rapide de modélisation P3"""
    base_url = "http://localhost:5000"
    try:
        response = requests.post(f"{base_url}/p3/modelisation", 
                               json={"query": "Test monitoring P3"}, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return {
                "success": True,
                "results_count": len(data.get('results', [])),
                "p3_activated": data.get('p3_activated', False),
                "innovation_level": data.get('innovation_level', 'N/A')
            }
        else:
            return {"success": False, "error": f"Status {response.status_code}"}
    except Exception as e:
        return {"success": False, "error": str(e)}

def humean_comprehensive_dashboard():
    print("🧠 DASHBOARD HUMEAN COMPLET - TEMPS RÉEL")
    print("=" * 70)
    
    p3_test_count = 0
    cycle_count = 0
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 70)
        
        # Métriques API
        metrics = get_humean_metrics()
        
        if 'error' in metrics:
            print(f"❌ Erreur API: {metrics['error']}")
        else:
            # AUTO-APPRENTISSAGE
            learning_data = metrics.get('learning', {})
            is_active = learning_data.get('active', False)
            cycles = learning_data.get('cycles_completed', 0)
            
            performance = learning_data.get('performance_metrics', {})
            cognitive_eff = performance.get('cognitive_efficiency', 0.0)
            memory_usage = performance.get('memory_usage', 0.0)
            energy_balance = performance.get('energy_balance', 0.0)
            
            print("🎯 AUTO-APPRENTISSAGE:")
            print(f"   🔄 Statut: {'✅ ACTIVÉ' if is_active else '❌ DÉSACTIVÉ'}")
            print(f"   📈 Cycles: {cycles}")
            print(f"   🧠 Efficacité: {cognitive_eff:.3f}")
            print(f"   💾 Mémoire: {memory_usage:.2f}")
            print(f"   ⚡ Énergie: {energy_balance:.2f}")
            
            # STATUT P3
            p3_data = metrics.get('p3', {})
            print(f"\n🚀 MOTEUR P3:")
            print(f"   🔧 Statut: {p3_data.get('p3_engine', 'N/A')}")
            print(f"   📊 Niveau: {p3_data.get('arbitrage_level', 'N/A')}")
            print(f"   🎯 Précision: {p3_data.get('performance', {}).get('accuracy', 0):.2f}")
            
            # TEST P3 ACTIF (toutes les 2 itérations)
            if p3_test_count % 2 == 0:
                print(f"\n🔮 TEST P3 ACTIF:")
                p3_result = test_p3_modelisation()
                if p3_result.get('success'):
                    print(f"   ✅ Modélisation réussie")
                    print(f"   📊 Résultats: {p3_result.get('results_count', 0)}")
                    print(f"   🌟 Innovation: {p3_result.get('innovation_level', 'N/A')}")
                else:
                    print(f"   ❌ Erreur P3: {p3_result.get('error', 'Inconnue')}")
            
            # MODULES CRITIQUES
            print(f"\n📦 MODULES CRITIQUES:")
            modules_data = metrics.get('modules', {})
            
            critical_modules = {
                'humean_core': 'Cœur Cognitif',
                'tpse_engine': 'Moteur TPSE', 
                'p3_modelling_engine': 'Modélisation P3',
                'auto_learning_engine': 'Auto-Apprentissage'
            }
            
            for module, display_name in critical_modules.items():
                module_info = modules_data.get(module, {})
                status = module_info.get('status', 'unknown')
                status_icon = "✅" if status == "operational" else "🟡" if status == "ready" else "❌"
                print(f"   {status_icon} {display_name}: {status}")
            
            # RECOMMANDATIONS
            print(f"\n💡 RECOMMANDATIONS:")
            if cognitive_eff < 0.85:
                print(f"   🔧 Optimiser l'efficacité cognitive")
            if cycles < 5:
                print(f"   📈 Augmenter les cycles d'apprentissage")
            if energy_balance < 0.8:
                print(f"   ⚡ Surveiller la consommation énergétique")
            else:
                print(f"   🎉 Système optimal - Continuer le monitoring")
        
        p3_test_count += 1
        cycle_count += 1
        
        print("\n" + "=" * 70)
        print("🔮 P3 testé en direct | 🔄 Auto-apprentissage | 📊 Métriques temps réel")
        print("⏸️  CTRL+C pour arrêter le monitoring (rafraîchissement: 5s)")
        time.sleep(5)

if __name__ == "__main__":
    try:
        humean_comprehensive_dashboard()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring arrêté - HUMEAN Cognitive System reste actif")
        print("🌐 Serveur toujours disponible sur http://localhost:5000")
