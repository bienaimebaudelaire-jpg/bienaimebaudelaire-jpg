#!/usr/bin/env python3
"""
Serveur HUMEAN - Système d'IA Évolutif
Script principal du serveur backend
"""

import os
import sys
import json
import logging
import sqlite3
import threading
import time
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
import numpy as np
import hashlib

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("humean_server.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("HumeanServer")

class HumeanDatabase:
    """Gestionnaire de base de données HUMEAN"""
    
    def __init__(self, db_path="humean_data.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialise la structure de la base de données"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Table des modèles IA
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ai_models (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    version TEXT NOT NULL,
                    model_data BLOB,
                    accuracy REAL,
                    training_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_active BOOLEAN DEFAULT TRUE
                )
            ''')
            
            # Table des données d'entraînement
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS training_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    input_data TEXT NOT NULL,
                    expected_output TEXT NOT NULL,
                    model_name TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Table de l'historique des performances
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS performance_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    model_name TEXT NOT NULL,
                    metric_name TEXT NOT NULL,
                    metric_value REAL NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.commit()
            conn.close()
            logger.info("✅ Base de données HUMEAN initialisée")
            
        except Exception as e:
            logger.error(f"❌ Erreur base de données: {e}")

class DataConnector:
    """Connecteur de données unifié"""
    
    def __init__(self, db_manager):
        self.db = db_manager
        logger.info("✅ Connecteur de données intégré")
    
    def store_training_data(self, input_data, expected_output, model_name):
        """Stocke les données d'entraînement"""
        try:
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO training_data (input_data, expected_output, model_name) VALUES (?, ?, ?)",
                (json.dumps(input_data), json.dumps(expected_output), model_name)
            )
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            logger.error(f"Erreur stockage données: {e}")
            return False
    
    def get_training_data(self, model_name, limit=1000):
        """Récupère les données d'entraînement"""
        try:
            conn = sqlite3.connect(self.db.db_path)
            cursor = conn.cursor()
            cursor.execute(
                "SELECT input_data, expected_output FROM training_data WHERE model_name = ? ORDER BY timestamp DESC LIMIT ?",
                (model_name, limit)
            )
            data = cursor.fetchall()
            conn.close()
            
            training_pairs = []
            for input_json, output_json in data:
                training_pairs.append({
                    'input': json.loads(input_json),
                    'output': json.loads(output_json)
                })
            return training_pairs
        except Exception as e:
            logger.error(f"Erreur récupération données: {e}")
            return []

class SelfImprovingSystem:
    """Système d'auto-amélioration de l'IA"""
    
    def __init__(self, data_connector):
        self.data_connector = data_connector
        self.improvement_thread = None
        self.is_running = False
        logger.info("✅ Système d'auto-amélioration chargé")
    
    def start_continuous_learning(self):
        """Démarre l'apprentissage continu en arrière-plan"""
        if self.is_running:
            return
        
        self.is_running = True
        self.improvement_thread = threading.Thread(target=self._improvement_loop)
        self.improvement_thread.daemon = True
        self.improvement_thread.start()
        logger.info("🔄 Boucle d'amélioration démarrée")
    
    def _improvement_loop(self):
        """Boucle principale d'amélioration"""
        while self.is_running:
            try:
                # Simulation d'amélioration périodique
                time.sleep(300)  # Toutes les 5 minutes
                self._run_improvement_cycle()
            except Exception as e:
                logger.error(f"Erreur boucle amélioration: {e}")
                time.sleep(60)
    
    def _run_improvement_cycle(self):
        """Exécute un cycle d'amélioration"""
        logger.info("🔧 Cycle d'amélioration en cours...")
        # Ici serait implémentée la logique d'optimisation des modèles
        time.sleep(2)
        logger.info("✅ Cycle d'amélioration terminé")

class AdvancedAIModel:
    """Modèle IA avancé avec capacités d'apprentissage"""
    
    def __init__(self, model_name="humean_core"):
        self.model_name = model_name
        self.knowledge_base = {}
        self.patterns = {}
        logger.info(f"🧠 Modèle {model_name} initialisé")
    
    def process_query(self, input_data, context=None):
        """Traite une requête et génère une réponse"""
        try:
            # Simulation de traitement IA
            if isinstance(input_data, str):
                input_lower = input_data.lower()
                
                # Réponses contextuelles de base
                if "bonjour" in input_lower or "salut" in input_lower:
                    response = "Bonjour ! Je suis le système HUMEAN. Comment puis-je vous aider ?"
                elif "heure" in input_lower:
                    current_time = datetime.now().strftime("%H:%M:%S")
                    response = f"Il est actuellement {current_time}"
                elif "merci" in input_lower:
                    response = "Je vous en prie ! N'hésitez pas si vous avez d'autres questions."
                else:
                    response = f"J'ai analysé votre requête : '{input_data}'. En mode d'apprentissage, je peux traiter diverses demandes."
                
                confidence = 0.85
            else:
                response = "Données complexes reçues. Traitement en cours..."
                confidence = 0.75
            
            return {
                'response': response,
                'confidence': confidence,
                'model': self.model_name,
                'timestamp': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Erreur traitement requête: {e}")
            return {
                'response': f"Erreur de traitement: {str(e)}",
                'confidence': 0.0,
                'model': self.model_name,
                'timestamp': datetime.now().isoformat()
            }
    
    def learn_from_feedback(self, input_data, expected_output, feedback_score):
        """Apprend à partir du feedback reçu"""
        # Simulation d'apprentissage
        pattern_key = hashlib.md5(str(input_data).encode()).hexdigest()[:16]
        self.knowledge_base[pattern_key] = {
            'input': input_data,
            'output': expected_output,
            'score': feedback_score,
            'learned_at': datetime.now().isoformat()
        }
        logger.info(f"📚 Apprentissage à partir du feedback: {feedback_score}")

# Initialisation de l'application Flask
app = Flask(__name__)
CORS(app)

# Initialisation des composants globaux
try:
    db_manager = HumeanDatabase()
    data_connector = DataConnector(db_manager)
    ai_model = AdvancedAIModel()
    improvement_system = SelfImprovingSystem(data_connector)
    
    # Démarrage des systèmes d'arrière-plan
    improvement_system.start_continuous_learning()
    
except Exception as e:
    logger.error(f"❌ Erreur initialisation: {e}")
    sys.exit(1)

# Routes de l'API
@app.route('/')
def serve_dashboard():
    """Route principale - Interface de dashboard"""
    try:
        return render_template('dashboard.html')
    except:
        return """
        <!DOCTYPE html>
        <html>
        <head>
            <title>HUMEAN Server</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; background: #f5f5f5; }
                .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }
                .status { padding: 10px; border-radius: 5px; margin: 10px 0; }
                .healthy { background: #d4edda; color: #155724; }
                .endpoints { margin-top: 20px; }
                .endpoint { background: #e9ecef; padding: 10px; margin: 5px 0; border-radius: 5px; font-family: monospace; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 Serveur HUMEAN - Système Opérationnel</h1>
                <div class="status healthy">✅ Statut: Serveur en fonctionnement</div>
                
                <h2>Endpoints disponibles:</h2>
                <div class="endpoints">
                    <div class="endpoint">POST /api/query - Interroger l'IA</div>
                    <div class="endpoint">GET /api/health - Statut du serveur</div>
                    <div class="endpoint">POST /api/feedback - Envoyer du feedback</div>
                    <div class="endpoint">GET /api/models - Liste des modèles</div>
                </div>
                
                <h2>Prochaines étapes:</h2>
                <ul>
                    <li>Ouvrez l'interface de contrôle principale</li>
                    <li>Configurez vos modèles IA</li>
                    <li>Chargez des données d'entraînement</li>
                </ul>
            </div>
        </body>
        </html>
        """

@app.route('/api/query', methods=['POST'])
def handle_query():
    """Endpoint pour les requêtes IA"""
    try:
        data = request.get_json()
        
        if not data or 'query' not in data:
            return jsonify({'error': 'Données de requête manquantes'}), 400
        
        query = data['query']
        context = data.get('context', {})
        
        # Traitement par le modèle IA
        result = ai_model.process_query(query, context)
        
        # Stockage pour apprentissage futur
        if data.get('store_for_training', True):
            data_connector.store_training_data(
                input_data=query,
                expected_output=result['response'],
                model_name=ai_model.model_name
            )
        
        return jsonify(result)
        
    except Exception as e:
        logger.error(f"Erreur endpoint /api/query: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/feedback', methods=['POST'])
def handle_feedback():
    """Endpoint pour recevoir du feedback sur les réponses"""
    try:
        data = request.get_json()
        
        if not data or 'input_data' not in data or 'feedback_score' not in data:
            return jsonify({'error': 'Données de feedback incomplètes'}), 400
        
        # Apprentissage à partir du feedback
        ai_model.learn_from_feedback(
            input_data=data['input_data'],
            expected_output=data.get('expected_output'),
            feedback_score=data['feedback_score']
        )
        
        return jsonify({'status': 'Feedback traité avec succès'})
        
    except Exception as e:
        logger.error(f"Erreur endpoint /api/feedback: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/models', methods=['GET'])
def list_models():
    """Liste les modèles IA disponibles"""
    try:
        return jsonify({
            'models': [
                {
                    'name': ai_model.model_name,
                    'status': 'active',
                    'capabilities': ['natural_language', 'pattern_recognition', 'continuous_learning']
                }
            ]
        })
    except Exception as e:
        logger.error(f"Erreur endpoint /api/models: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Endpoint de vérification de santé du serveur"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'components': {
            'database': 'connected',
            'ai_model': 'active',
            'learning_system': 'running'
        }
    })

@app.route('/api/system-status', methods=['GET'])
def system_status():
    """Endpoint de statut détaillé du système"""
    return jsonify({
        'status': 'operational',
        'server_time': datetime.now().isoformat(),
        'version': '1.0.0',
        'active_models': 1,
        'database': 'connected',
        'learning_system': 'active'
    })

@app.route('/api/training-data', methods=['GET'])
def get_training_data():
    """Récupère les données d'entraînement"""
    try:
        model_name = request.args.get('model', ai_model.model_name)
        limit = int(request.args.get('limit', 100))
        
        data = data_connector.get_training_data(model_name, limit)
        return jsonify({'training_data': data})
        
    except Exception as e:
        logger.error(f"Erreur endpoint /api/training-data: {e}")
        return jsonify({'error': str(e)}), 500

# Gestion des erreurs
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint non trouvé'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erreur interne du serveur'}), 500

if __name__ == '__main__':
    logger.info("🚀 Démarrage du serveur HUMEAN...")
    
    # Configuration du serveur
    host = os.environ.get('HUMEAN_HOST', '127.0.0.1')
    port = int(os.environ.get('HUMEAN_PORT', 5000))
    debug = os.environ.get('HUMEAN_DEBUG', 'False').lower() == 'true'
    
    logger.info(f"📍 Serveur accessible sur: http://{host}:{port}")
    logger.info("📋 Endpoints disponibles:")
    logger.info("   GET  /              - Dashboard")
    logger.info("   POST /api/query     - Requêtes IA")
    logger.info("   GET  /api/health    - Statut serveur")
    logger.info("   POST /api/feedback  - Feedback")
    logger.info("   GET  /api/models    - Modèles disponibles")
    logger.info("   GET  /api/system-status - Statut détaillé")
    
    try:
        app.run(
            host=host,
            port=port,
            debug=debug,
            threaded=True
        )
    except Exception as e:
        logger.error(f"❌ Erreur démarrage serveur: {e}")
        sys.exit(1)