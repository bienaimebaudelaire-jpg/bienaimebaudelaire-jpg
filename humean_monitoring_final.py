#!/usr/bin/env python3
"""
DASHBOARD MONITORING HUMEAN - VERSION FINALE
Basé sur les vraies données de l'API HUMEAN
"""

import requests
import time
import os
from datetime import datetime

def get_real_humean_metrics():
    """Récupère les métriques réelles du système HUMEAN"""
    base_url = "http://localhost:5000"
    metrics = {}
    
    try:
        # Statut des modules
        status_response = requests.get(f"{base_url}/status")
        if status_response.status_code == 200:
            metrics['modules'] = status_response.json()
        
        # Métriques d'apprentissage
        learning_response = requests.get(f"{base_url}/learning")
        if learning_response.status_code == 200:
            learning_data = learning_response.json()
            metrics['learning'] = learning_data
            
    except Exception as e:
        metrics['error'] = str(e)
    
    return metrics

def humean_final_dashboard():
    print("🧠 DASHBOARD HUMEAN - MONITORING RÉEL")
    print("=" * 60)
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"🕐 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        
        metrics = get_real_humean_metrics()
        
        if 'error' in metrics:
            print(f"❌ Erreur: {metrics['error']}")
        else:
            # AUTO-APPRENTISSAGE
            learning_data = metrics.get('learning', {})
            is_active = learning_data.get('active', False)
            cycles = learning_data.get('cycles_completed', 0)
            last_cycle = learning_data.get('last_cycle', 'N/A')
            
            performance = learning_data.get('performance_metrics', {})
            cognitive_eff = performance.get('cognitive_efficiency', 0.0)
            memory_usage = performance.get('memory_usage', 0.0)
            energy_balance = performance.get('energy_balance', 0.0)
            
            print("🎯 AUTO-APPRENTISSAGE:")
            print(f"   🔄 Statut: {'✅ ACTIVÉ' if is_active else '❌ DÉSACTIVÉ'}")
            print(f"   📈 Cycles complétés: {cycles}")
            print(f"   ⏱️  Dernier cycle: {last_cycle}")
            print(f"   🧠 Efficacité cognitive: {cognitive_eff:.2f}")
            print(f"   💾 Utilisation mémoire: {memory_usage:.2f}")
            print(f"   ⚡ Balance énergétique: {energy_balance:.2f}")
            
            # MODULES
            print("\n📦 ÉTAT DES MODULES:")
            modules = metrics.get('modules', {})
            
            module_status = {
                'humean_core': modules.get('humean_core', {}).get('status', 'unknown'),
                'tpse_engine': modules.get('tpse_engine', {}).get('status', 'unknown'),
                'p3_modelling_engine': modules.get('p3_modelling_engine', {}).get('status', 'unknown'),
                'auto_learning_engine': modules.get('auto_learning_engine', {}).get('status', 'unknown'),
                'governance_ai': modules.get('governance_ai', {}).get('status', 'unknown'),
                'ppbe_regulator': modules.get('ppbe_regulator', {}).get('status', 'unknown')
            }
            
            for module, status in module_status.items():
                status_icon = "✅" if status == "operational" else "🟡" if status == "ready" else "❌"
                # Formatage du nom du module
                display_name = module.replace('_', ' ').title()
                print(f"   {status_icon} {display_name}: {status}")
            
            # ACTIVITÉ
            print(f"\n🔍 ACTIVITÉ COGNITIVE:")
            print(f"   🌐 Port: 5000")
            print(f"   📍 Endpoints: /status, /learning")
            print(f"   🔄 Cycles aujourd'hui: {cycles}")
            
            # RECOMMANDATIONS
            if cognitive_eff < 0.8:
                print(f"   💡 Recommandation: Optimiser l'efficacité cognitive")
            if cycles < 10:
                print(f"   💡 Recommandation: Augmenter les cycles d'apprentissage")
        
        print("\n" + "=" * 60)
        print("🔄 Mise à jour automatique - CTRL+C pour arrêter")
        time.sleep(5)

if __name__ == "__main__":
    try:
        humean_final_dashboard()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring arrêté - HUMEAN Cognitive System reste actif")
