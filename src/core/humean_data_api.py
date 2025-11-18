#!/usr/bin/env python3
"""
EXTENSION API HUMEAN POUR DONNÉES RÉELLES
Nouveaux endpoints pour la connexion aux données externes
"""

from src.core.humean_data_connector import HumeanDataConnector
from flask import Flask, request, jsonify
import json

# Initialisation du connecteur
data_connector = HumeanDataConnector()

def create_data_endpoints(app):
    """Ajoute les endpoints données à l'application Flask"""
    
    @app.route('/data/connect/financial', methods=['POST'])
    def connect_financial_data():
        """Connexion aux données financières"""
        try:
            data = request.get_json()
            symbol = data.get('symbol', 'AAPL')
            days = data.get('days', 30)
            
            financial_data = data_connector.connect_financial_data(symbol, days)
            data_connector.generate_p3_insights()
            
            return jsonify({
                "status": "success",
                "data_type": "financial",
                "symbol": symbol,
                "data": financial_data
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/data/connect/scientific', methods=['POST'])
    def connect_scientific_data():
        """Connexion aux données scientifiques"""
        try:
            data = request.get_json()
            query = data.get('query', 'artificial intelligence')
            
            scientific_data = data_connector.connect_scientific_data(query)
            data_connector.generate_p3_insights()
            
            return jsonify({
                "status": "success", 
                "data_type": "scientific",
                "query": query,
                "data": scientific_data
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/data/connect/social', methods=['POST'])
    def connect_social_data():
        """Connexion aux données sociales"""
        try:
            data = request.get_json()
            topic = data.get('topic', 'AI ethics')
            
            social_data = data_connector.connect_social_data(topic)
            data_connector.generate_p3_insights()
            
            return jsonify({
                "status": "success",
                "data_type": "social", 
                "topic": topic,
                "data": social_data
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/data/insights', methods=['GET'])
    def get_p3_insights():
        """Récupère les insights P3 générés"""
        try:
            stats = data_connector.get_data_stats()
            return jsonify({
                "status": "success",
                "data_stats": stats,
                "available_sources": list(data_connector.data_sources.keys())
            })
            
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    
    @app.route('/data/sources', methods=['GET'])
    def get_data_sources():
        """Liste les sources de données disponibles"""
        return jsonify({
            "status": "success",
            "data_sources": data_connector.data_sources
        })

# Test des nouveaux endpoints
if __name__ == "__main__":
    print("🔌 Test des endpoints données...")
    
    # Simulation des appels
    test_connector = HumeanDataConnector()
    print("✅ Connecteur initialisé")
    
    stats = test_connector.get_data_stats()
    print(f"📊 Stats initiales: {stats}")
