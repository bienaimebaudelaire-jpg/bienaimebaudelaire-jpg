#!/usr/bin/env python3
"""
🚀 HUMEAN GitHub Sync - Version Simplifiée
Synchronisation automatique entre HUMEAN et GitHub
"""

import json
import os
import subprocess
from datetime import datetime

def sync_to_github(data_type, data, description=""):
    """Fonction simple de synchronisation"""
    try:
        # Fichier de données
        filename = f"humean_{data_type}.json"
        
        # Charger ou créer les données
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                all_data = json.load(f)
        else:
            all_data = {"entries": []}
        
        # Ajouter nouvelle entrée
        new_entry = {
            "timestamp": datetime.now().isoformat(),
            "data": data,
            "description": description
        }
        all_data["entries"].append(new_entry)
        
        # Sauvegarder
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(all_data, f, indent=2, ensure_ascii=False)
        
        # Git operations
        subprocess.run(['git', 'add', filename], check=True)
        subprocess.run(['git', 'commit', '-m', f"🤖 Auto-sync {data_type}: {description[:50]}"], check=True)
        subprocess.run(['git', 'push'], check=True)
        
        return {"status": "success", "message": f"{data_type} synchronized"}
        
    except Exception as e:
        return {"status": "error", "message": str(e)}

def get_sync_status():
    """Statut de synchronisation simple"""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
        return {
            "has_changes": bool(result.stdout.strip()),
            "status": "up_to_date" if not result.stdout.strip() else "needs_sync"
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

print("✅ HUMEAN GitHub Sync - Ready!")
