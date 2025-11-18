#!/usr/bin/env python3
"""
🎛️ HUMEAN Control Server
Serveur léger pour démarrer/arrêter HUMEAN via le panneau de contrôle
"""

import subprocess
import threading
import time
import os
from flask import Flask, jsonify, request
import webbrowser

app = Flask(__name__)
humean_process = None

class HumeanManager:
    def __init__(self):
        self.process = None
        self.script_path = "humean_server.py"
    
    def start_humean(self):
        """Démarrer le serveur HUMEAN"""
        global humean_process
        
        if self.is_humean_running():
            return {"status": "already_running", "message": "HUMEAN est déjà en cours d'exécution"}
        
        try:
            # Démarrer HUMEAN dans un processus séparé
            self.process = subprocess.Popen(
                ["python", self.script_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            # Attendre que le serveur soit prêt
            time.sleep(3)
            
            humean_process = self.process
            return {"status": "success", "message": "HUMEAN démarré avec succès"}
            
        except Exception as e:
            return {"status": "error", "message": f"Erreur: {str(e)}"}
    
    def stop_humean(self):
        """Arrêter le serveur HUMEAN"""
        global humean_process
        
        if humean_process:
            try:
                # Essayer d'arrêter gracieusement d'abord
                import requests
                requests.post("http://localhost:5000/api/shutdown", timeout=2)
                time.sleep(2)
            except:
                # Forcer l'arrêt si nécessaire
                humean_process.terminate()
                humean_process.wait()
            
            humean_process = None
            return {"status": "success", "message": "HUMEAN arrêté"}
        else:
            return {"status": "not_running", "message": "HUMEAN n'est pas en cours d'exécution"}
    
    def is_humean_running(self):
        """Vérifier si HUMEAN est en cours d'exécution"""
        try:
            import requests
            response = requests.get("http://localhost:5000/status", timeout=2)
            return response.status_code == 200
        except:
            return False

# Instance globale
humean_manager = HumeanManager()

@app.route('/')
def control_panel():
    """Servir le panneau de contrôle"""
    return '''
    <html>
        <head>
            <meta http-equiv="refresh" content="0; url=humean_control_panel.html">
        </head>
        <body>
            <p>Redirection vers le panneau de contrôle...</p>
        </body>
    </html>
    '''

@app.route('/api/start-server', methods=['POST'])
def start_server():
    """API pour démarrer HUMEAN"""
    result = humean_manager.start_humean()
    return jsonify(result)

@app.route('/api/stop-server', methods=['POST'])
def stop_server():
    """API pour arrêter HUMEAN"""
    result = humean_manager.stop_humean()
    return jsonify(result)

@app.route('/api/restart-server', methods=['POST'])
def restart_server():
    """API pour redémarrer HUMEAN"""
    humean_manager.stop_humean()
    time.sleep(2)
    result = humean_manager.start_humean()
    return jsonify(result)

@app.route('/api/server-status', methods=['GET'])
def server_status():
    """API pour le statut du serveur"""
    is_running = humean_manager.is_humean_running()
    return jsonify({
        "status": "online" if is_running else "offline",
        "humean_running": is_running,
        "control_server": "online"
    })

@app.route('/api/open-dashboard', methods=['POST'])
def open_dashboard():
    """Ouvrir le dashboard HUMEAN"""
    try:
        webbrowser.open("humean_dashboard.html")
        return jsonify({"status": "success", "message": "Dashboard ouvert"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    print("🎛️  Démarrage du serveur de contrôle HUMEAN...")
    print("📍 Port: 5001")
    print("🌐 Panneau de contrôle: http://localhost:5001")
    print("🚀 Utilisez ce serveur pour contrôler HUMEAN")
    
    # Démarrer sur un port différent pour éviter les conflits
    app.run(host='0.0.0.0', port=5001, debug=False)
