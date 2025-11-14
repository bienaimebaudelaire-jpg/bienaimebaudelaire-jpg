#!/usr/bin/env python3
"""
NETTOYAGE INTELLIGENT HUMEAN
Conserve les fichiers essentiels, supprime les doublons et temporaires
"""

import os
import shutil
from pathlib import Path

class HumeanCleaner:
    def __init__(self):
        self.essential_files = {
            # Fichiers principaux
            'humean_server.py',
            'humean_data_connector.py', 
            'humean_data_api.py',
            'requirements.txt',
            
            # Tests essentiels
            'test_all_endpoints.py',
            'test_real_data.py',
            'test_p3_force.py',
            'test_meta_cognition.py',
            'test_modelisation_p3.py',
            'test_search_connection.py',
            
            # Clients essentiels
            'humean_client_port5000.py',
            'humean_monitoring_comprehensive.py',
            
            # Documentation
            'README.md'  # Si existe
        }
        
        self.essential_patterns = [
            'humean_',
            'test_',
            'requirements',
            'README'
        ]
        
        self.files_to_keep = set()
        self.files_to_delete = []
        
    def analyze_project(self):
        """Analyse la structure du projet"""
        print("🔍 ANALYSE DU PROJET HUMEAN...")
        print("=" * 50)
        
        all_files = []
        for root, dirs, files in os.walk('.'):
            for file in files:
                if file.endswith('.py') or file.endswith('.txt') or file.endswith('.md'):
                    full_path = os.path.join(root, file)
                    all_files.append(full_path)
        
        print(f"📁 Fichiers trouvés: {len(all_files)}")
        
        # Identifier les fichiers essentiels
        for file_path in all_files:
            file_name = os.path.basename(file_path)
            
            # Fichiers dans la liste essentielle
            if file_name in self.essential_files:
                self.files_to_keep.add(file_path)
                continue
                
            # Fichiers avec patterns essentiels
            is_essential = any(pattern in file_name for pattern in self.essential_patterns)
            if is_essential:
                self.files_to_keep.add(file_path)
                continue
                
            # Fichiers de données (à conserver)
            if 'humean_data.db' in file_path or '.db' in file_path:
                self.files_to_keep.add(file_path)
                continue
                
            # Autres fichiers Python (à vérifier)
            if file_path.endswith('.py'):
                # Lire le contenu pour déterminer l'importance
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Fichiers avec des imports HUMEAN importants
                    if any(keyword in content for keyword in ['HumeanDataConnector', 'humean_server', 'p3_modelling', 'tpse_engine']):
                        self.files_to_keep.add(file_path)
                    else:
                        self.files_to_delete.append(file_path)
                except:
                    self.files_to_keep.add(file_path)  # En cas d'erreur, on conserve
            else:
                self.files_to_delete.append(file_path)
    
    def show_cleanup_plan(self):
        """Affiche le plan de nettoyage"""
        print("\n📋 PLAN DE NETTOYAGE:")
        print("=" * 50)
        
        print(f"✅ À CONSERVER ({len(self.files_to_keep)} fichiers):")
        for file in sorted(self.files_to_keep):
            print(f"   📄 {file}")
        
        print(f"\n🗑️  À SUPPRIMER ({len(self.files_to_delete)} fichiers):")
        for file in sorted(self.files_to_delete):
            print(f"   ❌ {file}")
    
    def execute_cleanup(self, dry_run=True):
        """Exécute le nettoyage"""
        print(f"\n🚀 EXÉCUTION DU NETTOYAGE (Dry Run: {dry_run})")
        print("=" * 50)
        
        deleted_count = 0
        errors = []
        
        for file_path in self.files_to_delete:
            try:
                if dry_run:
                    print(f"   🔸 SIMULATION: Suppression de {file_path}")
                else:
                    os.remove(file_path)
                    print(f"   ✅ SUPPRIMÉ: {file_path}")
                    deleted_count += 1
            except Exception as e:
                errors.append(f"❌ Erreur avec {file_path}: {e}")
        
        # Nettoyage des dossiers vides
        self.clean_empty_folders(dry_run)
        
        print(f"\n📊 RÉSULTAT:")
        print(f"   📁 Fichiers conservés: {len(self.files_to_keep)}")
        print(f"   🗑️  Fichiers supprimés: {deleted_count}")
        print(f"   ⚠️  Erreurs: {len(errors)}")
        
        for error in errors:
            print(f"   {error}")
    
    def clean_empty_folders(self, dry_run=True):
        """Nettoie les dossiers vides"""
        print(f"\n🧹 NETTOYAGE DES DOSSIERS VIDES...")
        
        empty_folders = []
        for root, dirs, files in os.walk('.', topdown=False):
            # Ignorer certains dossiers
            if any(ignore in root for ignore in ['.git', '__pycache__', '.vscode']):
                continue
                
            if not dirs and not files:
                empty_folders.append(root)
        
        for folder in empty_folders:
            try:
                if dry_run:
                    print(f"   🔸 SIMULATION: Suppression dossier vide {folder}")
                else:
                    os.rmdir(folder)
                    print(f"   ✅ DOSSIER VIDÉ: {folder}")
            except Exception as e:
                print(f"   ⚠️  Impossible de supprimer {folder}: {e}")
    
    def create_clean_structure_report(self):
        """Crée un rapport de la structure finale"""
        print(f"\n📊 STRUCTURE FINALE DU PROJET:")
        print("=" * 50)
        
        essential_categories = {
            "🚀 SERVEUR & CORE": [],
            "🔌 DONNÉES & API": [],
            "🧪 TESTS & VALIDATION": [],
            "📊 MONITORING & CLIENT": [],
            "📁 DONNÉES & CONFIG": []
        }
        
        for file_path in sorted(self.files_to_keep):
            file_name = os.path.basename(file_path)
            
            if 'server' in file_name.lower():
                essential_categories["🚀 SERVEUR & CORE"].append(file_path)
            elif 'data' in file_name.lower() or 'api' in file_name.lower():
                essential_categories["🔌 DONNÉES & API"].append(file_path)
            elif 'test' in file_name.lower():
                essential_categories["🧪 TESTS & VALIDATION"].append(file_path)
            elif 'monitor' in file_name.lower() or 'client' in file_name.lower():
                essential_categories["📊 MONITORING & CLIENT"].append(file_path)
            elif '.db' in file_name or '.txt' in file_name or '.md' in file_name:
                essential_categories["📁 DONNÉES & CONFIG"].append(file_path)
            else:
                essential_categories["🚀 SERVEUR & CORE"].append(file_path)
        
        for category, files in essential_categories.items():
            if files:
                print(f"\n{category}:")
                for file in files:
                    print(f"   📄 {file}")

def main():
    cleaner = HumeanCleaner()
    
    # Analyse
    cleaner.analyze_project()
    cleaner.show_cleanup_plan()
    
    # Demande confirmation
    response = input("\n❓ Voulez-vous exécuter le nettoyage pour de vrai ? (oui/NON): ").strip().lower()
    
    if response in ['oui', 'yes', 'y', 'o']:
        cleaner.execute_cleanup(dry_run=False)
        print("\n🎉 NETTOYAGE TERMINÉ !")
    else:
        cleaner.execute_cleanup(dry_run=True)
        print("\n🔸 NETTOYAGE SIMULÉ - Aucun fichier supprimé")
    
    # Rapport final
    cleaner.create_clean_structure_report()
    
    print(f"\n💡 Conseil: Exécutez à nouveau pour un vrai nettoyage si satisfait")

if __name__ == "__main__":
    main()
