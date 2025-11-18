#!/usr/bin/env python3
"""
NETTOYAGE AGGRESSIF HUMEAN - Version finale
Ne conserve que l'essentiel pour production
"""

import os
import shutil

# Liste blanche des fichiers ABSOLUMENT essentiels
ESSENTIAL_FILES = {
    # 🚀 CORE SYSTEM
    'humean_server.py',
    'humean_data_connector.py',
    'humean_data_api.py',
    
    # 🧪 TESTS PRINCIPAUX
    'test_all_endpoints.py',
    'test_real_data.py', 
    'test_p3_force.py',
    'test_meta_cognition.py',
    'test_modelisation_p3.py',
    
    # 📊 MONITORING & CLIENTS
    'humean_monitoring_comprehensive.py',
    'humean_client_port5000.py',
    
    # 📁 CONFIGURATION
    'requirements.txt',
    
    # 🗃️ DONNÉES (patterns)
    'humean_data.db'  # Si existe
}

# Dossiers essentiels à conserver
ESSENTIAL_DIRS = {
    'integration_layer',
    'tpse-engine'
}

def aggressive_cleanup():
    print("🧹 NETTOYAGE AGGRESSIF HUMEAN")
    print("=" * 50)
    
    deleted_count = 0
    kept_count = 0
    
    # Parcourir tous les fichiers
    for root, dirs, files in os.walk('.'):
        # Ignorer .git et autres dossiers système
        if any(ignore in root for ignore in ['.git', '__pycache__', '.vscode']):
            continue
            
        for file in files:
            file_path = os.path.join(root, file)
            file_name = file
            
            # CONSERVER si dans liste blanche
            if (file_name in ESSENTIAL_FILES or 
                any(file_name.startswith(prefix) for prefix in ['test_', 'humean_']) and 
                file_name.endswith('.py')):
                
                # Vérifier que c'est un fichier utile (pas un doublon)
                if is_file_useful(file_path):
                    print(f"✅ CONSERVER: {file_path}")
                    kept_count += 1
                    continue
            
            # SUPPRIMER le reste
            try:
                os.remove(file_path)
                print(f"🗑️  SUPPRIMÉ: {file_path}")
                deleted_count += 1
            except Exception as e:
                print(f"⚠️  Erreur avec {file_path}: {e}")
    
    # Nettoyer dossiers vides
    clean_empty_folders()
    
    print(f"\n📊 RÉSULTAT FINAL:")
    print(f"   ✅ Fichiers conservés: {kept_count}")
    print(f"   🗑️  Fichiers supprimés: {deleted_count}")
    print(f"   📁 Structure optimisée pour production")

def is_file_useful(file_path):
    """Détermine si un fichier est utile"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Fichiers avec du vrai code HUMEAN
        keywords = ['HumeanDataConnector', 'humean_server', 'Flask', 'jsonify', 'p3_modelling']
        return any(keyword in content for keyword in keywords)
    
    except:
        return True  # En cas de doute, on conserve

def clean_empty_folders():
    """Nettoie les dossiers vides"""
    print(f"\n🧹 NETTOYAGE DOSSIERS VIDES...")
    
    empty_folders = []
    for root, dirs, files in os.walk('.', topdown=False):
        if any(ignore in root for ignore in ['.git', '__pycache__', '.vscode']):
            continue
            
        # Conserver les dossiers essentiels même s'ils sont vides
        folder_name = os.path.basename(root)
        if folder_name in ESSENTIAL_DIRS:
            continue
            
        if not dirs and not files:
            empty_folders.append(root)
    
    for folder in empty_folders:
        try:
            os.rmdir(folder)
            print(f"   ✅ DOSSIER VIDÉ: {folder}")
        except Exception as e:
            print(f"   ⚠️  Impossible de supprimer {folder}: {e}")

def show_final_structure():
    """Affiche la structure finale"""
    print(f"\n🏗️  STRUCTURE FINALE OPTIMISÉE:")
    print("=" * 50)
    
    for root, dirs, files in os.walk('.'):
        if any(ignore in root for ignore in ['.git', '__pycache__']):
            continue
            
        level = root.count(os.sep) - 1
        indent = ' ' * 2 * level
        print(f"{indent}📁 {os.path.basename(root)}/")
        
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if file.endswith('.py') or file in ['requirements.txt', 'humean_data.db']:
                print(f"{subindent}📄 {file}")

if __name__ == "__main__":
    print("🔍 Cette action supprimera les fichiers non essentiels.")
    response = input("❓ Continuer ? (oui/NON): ").strip().lower()
    
    if response in ['oui', 'yes', 'y', 'o']:
        aggressive_cleanup()
        show_final_structure()
        print("\n🎉 NETTOYAGE AGGRESSIF TERMINÉ !")
        print("💡 Le système HUMEAN est maintenant optimisé pour la production")
    else:
        print("🔸 Nettoyage annulé")
