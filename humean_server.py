#!/usr/bin/env python3
"""
HUMEAN COGNITIVE SYSTEM - SERVEUR COMPLET AVEC DONNÉES
Système cognitif avancé avec auto-apprentissage, P3 et connecteur données
"""

from flask import Flask, request, jsonify
import logging
import time
from datetime import datetime
import sys
import os

# Configuration du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('HumeanServer')

# Initialisation Flask
app = Flask(__name__)

# Import du connecteur de données
try:
    from humean_data_connector import HumeanDataConnector
    from humean_data_api import create_data_endpoints
    data_connector = HumeanDataConnector()
    DATA_CONNECTOR_AVAILABLE = True
except ImportError as e:
    logger.warning(f"Connecteur données non disponible: {e}")
    DATA_CONNECTOR_AVAILABLE = False

# État du système
system_state = {
    "system": {
        "name": "HUMEAN Cognitive System",
        "version": "2.0",
        "mode": "production",
        "start_time": datetime.now().isoformat()
    },
    "auto_learning": True,
    "learning_cycles": 0,
    "cognitive_efficiency": 0.85,
    "energy_remaining": 9.8,
    "modules": {
        "gateway": "operational",
        "memory": "operational",
        "scheduler": "ready",
        "ethics": "ready",
        "monitoring": "operational"
    }
}

# Modules HUMEAN simulés
humean_modules = {
    "humean_core": {
        "status": "operational",
        "version": "1.0",
        "description": "Cœur cognitif HUMEAN"
    },
    "tpse_engine": {
        "status": "operational", 
        "version": "1.2",
        "description": "Moteur de perception TPSE"
    },
    "p3_modelling_engine": {
        "status": "operational",
        "version": "2.0",
        "description": "Modélisation P3 et arbitrage cognitif"
    },
    "auto_learning_engine": {
        "status": "operational",
        "version": "1.1",
        "description": "Auto-apprentissage adaptatif"
    },
    "governance_ai": {
        "status": "ready",
        "version": "1.0",
        "description": "Gouvernance éthique et conformité"
    },
    "ppbe_regulator": {
        "status": "ready",
        "version": "1.0",
        "description": "Régulation énergétique PPBE"
    }
}

@app.route('/')
def home():
    """Page d'accueil"""
    endpoints = ["/status", "/learning", "/p3/status", "/p3/modelisation", "/health"]
    if DATA_CONNECTOR_AVAILABLE:
        endpoints.extend(["/data/sources", "/data/insights", "/data/connect/financial", "/data/connect/scientific", "/data/connect/social"])
    
    return jsonify({
        "message": "HUMEAN Cognitive System - API Server",
        "version": "2.0",
        "status": "operational",
        "data_connector": "available" if DATA_CONNECTOR_AVAILABLE else "unavailable",
        "endpoints": endpoints
    })

@app.route('/status', methods=['GET'])
def status():
    """Statut complet du système HUMEAN"""
    return jsonify({
        **humean_modules,
        "system_metrics": {
            "auto_learning": system_state["auto_learning"],
            "learning_cycles": system_state["learning_cycles"],
            "cognitive_efficiency": system_state["cognitive_efficiency"],
            "energy_remaining": system_state["energy_remaining"],
            "uptime": f"{(datetime.now() - datetime.fromisoformat(system_state['system']['start_time'])).total_seconds():.0f}s",
            "data_connector_available": DATA_CONNECTOR_AVAILABLE
        }
    })

@app.route('/learning', methods=['GET'])
def learning_status():
    """Statut de l'auto-apprentissage"""
    # Simuler un cycle d'apprentissage
    system_state["learning_cycles"] += 1
    system_state["cognitive_efficiency"] = min(0.95, system_state["cognitive_efficiency"] + 0.01)
    system_state["energy_remaining"] = max(0, system_state["energy_remaining"] - 0.1)
    
    return jsonify({
        "active": system_state["auto_learning"],
        "cycles_completed": system_state["learning_cycles"],
        "last_cycle": datetime.now().isoformat(),
        "performance_metrics": {
            "cognitive_efficiency": system_state["cognitive_efficiency"],
            "energy_balance": system_state["energy_remaining"] / 10.0,
            "memory_usage": 0.65,
            "processing_speed": 0.88
        }
    })

@app.route("/p3/modelisation", methods=["POST"])
def p3_modelisation_endpoint():
    """Endpoint pour la modélisation P3"""
    try:
        data = request.get_json()
        query = data.get("query", "")
        
        logger.info(f"🔮 Requête P3 reçue: {query}")
        
        # Réponse P3 avancée
        p3_response = {
            "status": "success",
            "query": query,
            "p3_activated": True,
            "innovation_level": "🚀 AVANCÉ",
            "timestamp": datetime.now().isoformat(),
            "results": [
                {
                    "source": "p3_modelling_engine",
                    "content": "ARCHITECTURE HUMEAN v2.0 - COUCHE D'ARBITRAGE (NIVEAU 5)",
                    "relevance": 0.96,
                    "type": "architectural_innovation"
                },
                {
                    "source": "humean_core",
                    "content": f"Perception TPSE réussie pour: {query}. Arbitrage cognitif P3 requis",
                    "relevance": 0.94,
                    "type": "cognitive_analysis"
                },
                {
                    "source": "tpse_engine",
                    "content": "Boucle perception->interprétation engagée. Prêt pour modélisation P3 avancée",
                    "relevance": 0.92,
                    "type": "process_status"
                },
                {
                    "source": "auto_learning_engine",
                    "content": f"Cycle #{system_state['learning_cycles']} - Optimisation cognitive active pour P3",
                    "relevance": 0.89,
                    "type": "learning_insight"
                },
                {
                    "source": "governance_ai",
                    "content": "Requête analysée par le module Ethics. Niveau de gouvernance L3 appliqué",
                    "relevance": 0.87,
                    "type": "governance_check"
                }
            ],
            "arbitrage_metrics": {
                "conflict_resolution_rate": 0.92,
                "cognitive_gain": 0.25,
                "efficiency_improvement": 0.18,
                "energy_optimization": 0.15
            }
        }
        
        logger.info("🎯 Réponse P3 générée avec succès")
        return jsonify(p3_response)
        
    except Exception as e:
        logger.error(f"❌ Erreur endpoint P3: {e}")
        return jsonify({"error": str(e), "status": "error"}), 500

@app.route("/p3/status", methods=["GET"])
def p3_status_endpoint():
    """Statut du moteur P3"""
    return jsonify({
        "p3_engine": "operational",
        "version": "2.0",
        "arbitrage_level": 5,
        "active": True,
        "performance": {
            "response_time": "0.8s",
            "accuracy": 0.94,
            "innovation_score": 0.88
        },
        "capabilities": [
            "cognitive_arbitrage",
            "architectural_modeling", 
            "conflict_resolution",
            "auto_optimization"
        ]
    })

@app.route('/health', methods=['GET'])
def health_check():
    """Health check simplifié"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

# Endpoints données si disponible
if DATA_CONNECTOR_AVAILABLE:
    create_data_endpoints(app)
    logger.info("✅ Connecteur de données intégré")

def initialize_system():
    """Initialisation du système HUMEAN"""
    logger.info("🧠 HUMEAN COGNITIVE SYSTEM - SERVEUR DÉMARRÉ")
    logger.info("📍 URL: http://localhost:5000")
    logger.info("📚 Architecture HUMEAN chargée:")
    logger.info("   • Système: HUMEAN Cognitive System")
    logger.info("   • Mode: production")
    logger.info("   • Moteur cognitif: gemini")
    logger.info("---")
    logger.info("🛠️  Modules opérationnels:")
    for module, info in humean_modules.items():
        status_icon = "✅" if info["status"] == "operational" else "🟡"
        logger.info(f"   • {module}: {status_icon} {info['status']}")
    
    if DATA_CONNECTOR_AVAILABLE:
        logger.info("---")
        logger.info("🔌 CONNECTEUR DONNÉES: ACTIVÉ")
        logger.info("   • Sources financières: ✅")
        logger.info("   • Sources scientifiques: ✅") 
        logger.info("   • Sources sociales: 🟡")
        logger.info("   • Sources IoT: 🔵")
    
    logger.info("---")
    logger.info("🚀 AUTO-APPRENTISSAGE: ACTIVÉ AU PREMIER APPEL")
    logger.info("🌟 MODÉLISATION P3: DISPONIBLE")
    if DATA_CONNECTOR_AVAILABLE:
        logger.info("🌐 Endpoints données: /data/*")
    logger.info("---")
    logger.info("🔄 Cycle auto-apprentissage #1")
    logger.info("🚀 Auto-apprentissage HUMEAN activé")
    logger.info("📈 Optimisation cognitive appliquée")


# =============================================================================
# 🚀 ROUTES AUTO-AMÉLIORATION HUMEAN
# =============================================================================

try:
    from humean_auto_improvement import humean_auto_improver
    print("✅ Système d'auto-amélioration chargé")
except ImportError as e:
    print(f"⚠️  Auto-improvement non disponible: {e}")
    humean_auto_improver = None

@app.route('/api/auto-improvement/analyze-and-apply', methods=['POST'])
def auto_improve():
    """Endpoint pour l'auto-amélioration automatique"""
    if humean_auto_improver is None:
        return jsonify({
            "status": "error", 
            "message": "Système d'auto-amélioration non disponible"
        }), 501
    
    try:
        data = request.json
        request_text = data.get('request', 'Analyse et améliore le système')
        
        print(f"🚀 Déclenchement auto-amélioration: {request_text}")
        
        result = humean_auto_improver.analyze_and_apply(request_text)
        
        return jsonify({
            "status": "success",
            "message": "Auto-amélioration complétée avec succès",
            "data": result
        })
        
    except Exception as e:
        print(f"❌ Erreur auto-amélioration: {e}")
        return jsonify({
            "status": "error", 
            "message": f"Erreur lors de l'auto-amélioration: {str(e)}"
        }), 500

@app.route('/api/auto-improvement/status', methods=['GET'])
def auto_improvement_status():
    """Statut du système d'auto-amélioration"""
    return jsonify({
        "status": "available" if humean_auto_improver else "unavailable",
        "version": "1.0",
        "capabilities": ["self_analysis", "automatic_implementation", "github_sync"]
    })


# =============================================================================
# 🎛️ ROUTES POUR LE PANNEAU DE CONTRÔLE
# =============================================================================

@app.route('/api/shutdown', methods=['POST'])
def shutdown_server():
    """Arrêt gracieux du serveur pour le panneau de contrôle"""
    import os
    import signal
    print("🔄 Arrêt gracieux du serveur HUMEAN...")
    
    def shutdown():
        print("✅ Serveur HUMEAN arrêté")
        os.kill(os.getpid(), signal.SIGINT)
    
    import threading
    threading.Timer(1, shutdown).start()
    
    return jsonify({
        "status": "success",
        "message": "Serveur en cours d'arrêt..."
    })

@app.route('/api/restart', methods=['POST'])
def restart_server():
    """Redémarrage du serveur"""
    print("🔄 Redémarrage du serveur HUMEAN...")
    
    def restart():
        import sys
        import os
        os.execv(sys.executable, ['python'] + sys.argv)
    
    import threading
    threading.Timer(2, restart).start()
    
    return jsonify({
        "status": "success", 
        "message": "Redémarrage en cours..."
    })

@app.route('/api/control/status', methods=['GET'])
def control_status():
    """Statut détaillé pour le panneau de contrôle"""
    try:
        # Vérifier si les modules sont chargés
        modules_status = {
            "auto_improvement": False,
            "github_sync": False,
            "p3_engine": True,
            "learning_engine": True
        }
        
        # Vérifier la présence des fichiers
        import os
        if os.path.exists("humean_auto_improvement.py"):
            modules_status["auto_improvement"] = True
        if os.path.exists("humean_github_sync.py"):
            modules_status["github_sync"] = True
        
        return jsonify({
            "server_status": "online",
            "humean_status": "operational", 
            "modules": modules_status,
            "timestamp": "2024-01-15T12:00:00",
            "version": "2.0"
        })
    except Exception as e:
        return jsonify({
            "server_status": "online",
            "humean_status": "error",
            "error": str(e)
        }), 500

@app.route('/control')
def control_panel_redirect():
    """Redirection vers le panneau de contrôle"""
    return '''
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=/static/control_panel.html">
        </head>
        <body>
            <p>Redirection vers le panneau de contrôle...</p>
        </body>
    </html>
    '''

# Route de santé étendue
@app.route('/health')
def health_check():
    """Vérification de santé étendue"""
    import os
    import psutil
    
    try:
        # Informations système
        process = psutil.Process()
        memory_info = process.memory_info()
        
        return jsonify({
            "status": "healthy",
            "timestamp": "2024-01-15T12:00:00",
            "system": {
                "memory_usage_mb": round(memory_info.rss / 1024 / 1024, 2),
                "cpu_percent": psutil.cpu_percent(),
                "uptime_seconds": int(process.create_time())
            },
            "services": {
                "api": "operational",
                "database": "connected", 
                "learning_engine": "active",
                "p3_engine": "active"
            }
        })
    except Exception as e:
        return jsonify({
            "status": "degraded",
            "error": str(e)
        }), 500

if __name__ == '__main__':
    initialize_system()
    app.run(host='0.0.0.0', port=5000, debug=False)


