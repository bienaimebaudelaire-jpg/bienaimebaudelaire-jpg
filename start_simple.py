#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
os.environ['PYTHONIOENCODING'] = 'utf-8'

print('🚀 HUMEAN SERVER - Démarrage...')
print('📍 http://127.0.0.1:5000')
print('🛑 Ctrl+C pour arrêter')
print('=' * 40)

try:
    import core.humean_server
    print('✅ Serveur démarré avec succès!')
    
    # Garder le programme en vie
    import time
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print('\n👋 Arrêt du serveur')
except Exception as e:
    print(f'❌ Erreur: {e}')
    input('Appuyez sur Entrée...')
