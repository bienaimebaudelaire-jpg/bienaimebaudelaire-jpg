import os
import re
import glob

def update_imports_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Patterns de correction des imports
        replacements = [
            # Corriger les imports relatifs
            (r'from src.core.humean_', 'from src.core.humean_'),
            (r'from tests.test_', 'from tests.test_'),
            (r'import src.core.humean_', 'import src.core.humean_'),
            (r'from monitoring\.', 'from src.monitoring.'),
            (r'from utils\.', 'from src.utils.'),
            (r'from core\.', 'from src.core.'),
            
            # Imports de données
            (r'from src.core.humean_data_connector', 'from src.core.humean_data_connector'),
            (r'from src.core.humean_data_api', 'from src.core.humean_data_api'),
            
            # Imports de tests
            (r'from tests.test_', 'from tests.test_')
        ]
        
        for pattern, replacement in replacements:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ IMPORT FIXED: {file_path}")
            return True
        
        return False
    
    except Exception as e:
        print(f"❌ ERROR in {file_path}: {e}")
        return False

def main():
    print("🔄 Correction automatique des imports Python...")
    updated_files = 0
    
    # Parcourir tous les fichiers Python
    python_files = glob.glob('**/*.py', recursive=True)
    
    for file_path in python_files:
        # Éviter les fichiers dans __pycache__ et archive
        if '__pycache__' in file_path or 'archive' in file_path:
            continue
            
        if update_imports_in_file(file_path):
            updated_files += 1
    
    print(f"\\n🎉 Correction terminée : {updated_files} fichiers mis à jour")

if __name__ == "__main__":
    main()
