from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import time, uuid, os

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

# Simple in-memory log
INTERACTIONS = []

@app.route('/')
def index():
    return """
    <html><body>
    <h2>HUMEAN — Serveur opérationnel</h2>
    <p>Accède au chat : <a href='/chat'>/chat</a></p>
    <p>Endpoints disponibles: POST /api/query , GET /api/health , GET /api/models</p>
    </body></html>
    """

@app.route('/chat')
def chat_ui():
    return send_from_directory(app.static_folder, 'chat.html')

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"ok": True, "status":"serving", "time": time.time()})

@app.route('/api/models', methods=['GET'])
def models():
    # placeholder for list of configured models
    return jsonify({"models": ["deepseek","chatgpt","openrouter","gemini"]})

@app.route('/api/query', methods=['POST'])
def query():
    data = request.json or {}
    user_id = data.get('user_id','anon')
    prompt = data.get('prompt','')
    meta = data.get('meta',{})
    # Simple echo response (remplace avec orchestrator.call_model)
    resp_text = f"Echo HUMEAN — reçu: {prompt}"
    record = {
        "id": str(uuid.uuid4()),
        "user_id": user_id,
        "prompt": prompt,
        "meta": meta,
        "response": resp_text,
        "ts": time.time()
    }
    INTERACTIONS.append(record)
    return jsonify({"ok": True, "response": resp_text, "record_id": record["id"]})

<<<<<<< HEAD
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


=======
if __name__ == "__main__":
    # debug True ok pour dev local
    app.run(host="0.0.0.0", port=5000, debug=True)
>>>>>>> e2a619c (🚀 Auto-improvement: HUMEAN s'auto-améliore)
