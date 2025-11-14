#!/usr/bin/env python3
"""
🚀 HUMEAN - Système de Synchronisation Auto GitHub
Pont automatique entre l'auto-apprentissage et le repository GitHub
"""

import json
import os
import subprocess
import datetime
import logging
from pathlib import Path

class HumeanGitHubSync:
    def __init__(self):
        self.repo_path = Path(".")
        self.sync_log = "humean_sync_log.json"
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('humean_sync.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def auto_commit_learning(self, learning_data):
        """Commit automatique des données d'apprentissage"""
        try:
            # Sauvegarder les données d'apprentissage
            learning_file = "humean_learning_data.json"
            
            # Charger les données existantes
            if os.path.exists(learning_file):
                with open(learning_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            else:
                existing_data = {"learning_sessions": []}
            
            # Ajouter la nouvelle session
            new_session = {
                "timestamp": datetime.datetime.now().isoformat(),
                "input": learning_data.get('input', ''),
                "mode": learning_data.get('mode', ''),
                "context": learning_data.get('context', ''),
                "results": learning_data.get('results', {})
            }
            
            existing_data["learning_sessions"].append(new_session)
            
            # Sauvegarder
            with open(learning_file, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            
            # Git operations
            self.git_add_commit_push(
                message=f"🧠 Auto-learning: {learning_data.get('input', 'New learning')[:50]}...",
                files=[learning_file]
            )
            
            return {"status": "success", "message": "Learning data synchronized with GitHub"}
            
        except Exception as e:
            self.logger.error(f"Auto-commit error: {e}")
            return {"status": "error", "message": str(e)}
    
    def auto_commit_innovation(self, innovation_data):
        """Commit automatique des innovations P3"""
        try:
            innovation_file = "humean_innovations.json"
            
            # Charger les innovations existantes
            if os.path.exists(innovation_file):
                with open(innovation_file, 'r', encoding='utf-8') as f:
                    existing_data = json.load(f)
            else:
                existing_data = {"innovations": []}
            
            # Ajouter la nouvelle innovation
            new_innovation = {
                "timestamp": datetime.datetime.now().isoformat(),
                "concept": innovation_data.get('concept', ''),
                "domain": innovation_data.get('domain', ''),
                "innovation": innovation_data.get('innovation', ''),
                "pattern": innovation_data.get('pattern', ''),
                "innovation_type": innovation_data.get('innovation_type', '')
            }
            
            existing_data["innovations"].append(new_innovation)
            
            # Sauvegarder
            with open(innovation_file, 'w', encoding='utf-8') as f:
                json.dump(existing_data, f, indent=2, ensure_ascii=False)
            
            # Git operations
            self.git_add_commit_push(
                message=f"🔮 P3 Innovation: {innovation_data.get('concept', 'New concept')[:50]}...",
                files=[innovation_file]
            )
            
            return {"status": "success", "message": "Innovation synchronized with GitHub"}
            
        except Exception as e:
            self.logger.error(f"Innovation commit error: {e}")
            return {"status": "error", "message": str(e)}
    
    def git_add_commit_push(self, message, files=None):
        """Opérations Git automatisées"""
        try:
            # Add files
            if files:
                for file in files:
                    subprocess.run(['git', 'add', file], check=True, capture_output=True)
            else:
                subprocess.run(['git', 'add', '.'], check=True, capture_output=True)
            
            # Commit
            subprocess.run(['git', 'commit', '-m', message], check=True, capture_output=True)
            
            # Push
            result = subprocess.run(['git', 'push'], check=True, capture_output=True, text=True)
            
            self.logger.info(f"GitHub sync successful: {message}")
            return True
            
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Git operation failed: {e}")
            return False
    
    def get_sync_status(self):
        """Obtenir le statut de synchronisation"""
        try:
            result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            changes = result.stdout.strip()
            
            return {
                "status": "needs_sync" if changes else "up_to_date",
                "changes": changes,
                "last_sync": self.get_last_sync_time()
            }
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def get_last_sync_time(self):
        """Obtenir le dernier temps de synchronisation"""
        try:
            result = subprocess.run(['git', 'log', '-1', '--format=%cd', '--date=iso'], 
                                  capture_output=True, text=True)
            return result.stdout.strip()
        except:
            return "Unknown"

# Instance globale
github_sync = HumeanGitHubSync()

if __name__ == "__main__":
    # Test de la synchronisation
    sync = HumeanGitHubSync()
    print("🚀 HUMEAN GitHub Sync initialisé avec succès!")
