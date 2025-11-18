import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def start_server():
    '''Wrapper pour démarrer le serveur HUMEAN'''
    from core.humean_server import app
    import logging
    
    # Configurer le logging pour éviter les erreurs d'encodage
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('humean_server.log', encoding='utf-8'),
            logging.StreamHandler()
        ]
    )
    
    print('🚀 Démarrage du serveur HUMEAN...')
    print('📍 Accessible sur: http://127.0.0.1:5000')
    print('📝 Logs enregistrés dans: humean_server.log')
    print('🛑 Appuyez sur Ctrl+C pour arrêter')
    
    app.run(host='127.0.0.1', port=5000, debug=False)

if __name__ == '__main__':
    start_server()
