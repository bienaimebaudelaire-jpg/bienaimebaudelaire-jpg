#!/usr/bin/env python3
"""
HUMEAN DATA CONNECTOR - Version Simplifiée et Corrigée
Connexion aux sources de données externes sans dépendances lourdes
"""

import requests
import json
import sqlite3
from datetime import datetime
import os
import random

class HumeanDataConnector:
    def __init__(self):
        self.data_sources = {
            "financial": {
                "name": "Données Financières",
                "endpoints": ["yahoo_finance", "alpha_vantage", "financial_news"],
                "status": "ready"
            },
            "scientific": {
                "name": "Données Scientifiques", 
                "endpoints": ["arxiv_api", "pubmed_api", "research_papers"],
                "status": "ready"
            },
            "social": {
                "name": "Données Sociales",
                "endpoints": ["twitter_api", "reddit_api", "news_api"],
                "status": "configuring"
            },
            "iot": {
                "name": "Données IoT/Capteurs",
                "endpoints": ["sensor_networks", "weather_api", "environmental"],
                "status": "planned"
            }
        }
        
        # Initialisation base de données locale
        self.init_database()
    
    def init_database(self):
        """Initialise la base de données locale HUMEAN"""
        try:
            conn = sqlite3.connect('humean_data.db')
            cursor = conn.cursor()
            
            # Table données brutes
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS raw_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    source_type TEXT,
                    data_content TEXT,
                    timestamp DATETIME,
                    processed BOOLEAN DEFAULT FALSE,
                    p3_insight_generated BOOLEAN DEFAULT FALSE
                )
            ''')
            
            # Table insights P3
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS p3_insights (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    raw_data_id INTEGER,
                    insight_text TEXT,
                    confidence_score REAL,
                    innovation_level TEXT,
                    generated_at DATETIME,
                    FOREIGN KEY (raw_data_id) REFERENCES raw_data (id)
                )
            ''')
            
            conn.commit()
            conn.close()
            print("✅ Base de données HUMEAN initialisée")
            
        except Exception as e:
            print(f"❌ Erreur initialisation DB: {e}")
    
    def connect_financial_data(self, symbol="AAPL", days=30):
        """Connexion aux données financières (simulation)"""
        print(f"📈 Connexion données financières: {symbol}")
        
        # Simulation de données financières réalistes
        price_change = random.uniform(-0.05, 0.08)  # Variation de -5% à +8%
        trend = "bullish" if price_change > 0 else "bearish"
        
        financial_data = {
            "symbol": symbol,
            "period": f"{days} days",
            "current_price": round(150 * (1 + price_change), 2),
            "price_change_percent": round(price_change * 100, 2),
            "data": {
                "price_trend": trend,
                "volatility": round(random.uniform(0.1, 0.25), 3),
                "volume": random.randint(10000000, 25000000),
                "sentiment": round(random.uniform(0.6, 0.9), 2)
            },
            "timestamp": datetime.now().isoformat()
        }
        
        self.store_raw_data("financial", financial_data)
        return financial_data
    
    def connect_scientific_data(self, query="artificial intelligence"):
        """Connexion aux données scientifiques (simulation)"""
        print(f"🔬 Connexion données scientifiques: {query}")
        
        # Simulation données recherche réalistes
        topics = [
            "LLM optimization", "Neuro-symbolic AI", "AGI safety", 
            "Transformer architectures", "Multimodal learning"
        ]
        
        scientific_data = {
            "query": query,
            "papers_found": random.randint(25, 100),
            "trending_topics": random.sample(topics, 3),
            "innovation_score": round(random.uniform(0.7, 0.95), 2),
            "recent_breakthroughs": [
                "Efficient attention mechanisms",
                "Cross-modal transfer learning",
                "Ethical alignment techniques"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        self.store_raw_data("scientific", scientific_data)
        return scientific_data
    
    def connect_social_data(self, topic="AI ethics"):
        """Connexion aux données sociales (simulation)"""
        print(f"💬 Connexion données sociales: {topic}")
        
        # Simulation données sociales réalistes
        social_data = {
            "topic": topic,
            "sentiment_analysis": {
                "positive": round(random.uniform(0.5, 0.8), 2),
                "negative": round(random.uniform(0.1, 0.3), 2), 
                "neutral": round(random.uniform(0.1, 0.2), 2)
            },
            "key_phrases": ["ethical AI", "governance frameworks", "transparency", "accountability"],
            "engagement_metrics": {
                "mentions": random.randint(500, 2000),
                "reach": random.randint(100000, 1000000),
                "engagement_rate": round(random.uniform(0.02, 0.08), 3)
            },
            "influential_voices": [
                "AI researchers", "Ethicists", "Industry leaders", "Policy makers"
            ],
            "timestamp": datetime.now().isoformat()
        }
        
        self.store_raw_data("social", social_data)
        return social_data
    
    def connect_iot_data(self, sensor_type="environmental"):
        """Connexion aux données IoT (simulation)"""
        print(f"🌡️ Connexion données IoT: {sensor_type}")
        
        iot_data = {
            "sensor_type": sensor_type,
            "readings": {
                "temperature": round(random.uniform(15, 30), 1),
                "humidity": round(random.uniform(40, 80), 1),
                "air_quality": round(random.uniform(80, 99), 1),
                "noise_level": random.randint(40, 70)
            },
            "anomalies_detected": random.randint(0, 3),
            "timestamp": datetime.now().isoformat()
        }
        
        self.store_raw_data("iot", iot_data)
        return iot_data
    
    def store_raw_data(self, source_type, data):
        """Stocke les données brutes en base"""
        try:
            conn = sqlite3.connect('humean_data.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO raw_data (source_type, data_content, timestamp)
                VALUES (?, ?, ?)
            ''', (source_type, json.dumps(data), datetime.now()))
            
            conn.commit()
            conn.close()
            print(f"💾 Données {source_type} stockées")
            
        except Exception as e:
            print(f"❌ Erreur stockage données: {e}")
    
    def generate_p3_insights(self):
        """Génère des insights P3 à partir des données stockées"""
        try:
            conn = sqlite3.connect('humean_data.db')
            cursor = conn.cursor()
            
            # Récupérer données non traitées
            cursor.execute('''
                SELECT id, source_type, data_content 
                FROM raw_data 
                WHERE processed = FALSE
            ''')
            
            unprocessed_data = cursor.fetchall()
            insights_generated = 0
            
            for data_row in unprocessed_data:
                data_id, source_type, data_content = data_row
                data_dict = json.loads(data_content)
                
                # Générer insight P3 basé sur le type de données
                insight = self._generate_insight_from_data(source_type, data_dict)
                
                if insight:
                    cursor.execute('''
                        INSERT INTO p3_insights 
                        (raw_data_id, insight_text, confidence_score, innovation_level, generated_at)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (data_id, insight['text'], insight['confidence'], insight['level'], datetime.now()))
                    
                    # Marquer comme traité
                    cursor.execute('''
                        UPDATE raw_data SET processed = TRUE, p3_insight_generated = TRUE
                        WHERE id = ?
                    ''', (data_id,))
                    
                    insights_generated += 1
                    print(f"🔮 Insight P3 généré: {insight['text'][:80]}...")
            
            conn.commit()
            conn.close()
            print(f"🎯 {insights_generated} insights P3 générés")
            
        except Exception as e:
            print(f"❌ Erreur génération insights: {e}")
    
    def _generate_insight_from_data(self, source_type, data):
        """Génère un insight P3 spécifique au type de données"""
        if source_type == "financial":
            price_change = data.get('data', {}).get('price_change_percent', 0)
            trend = "haussière" if price_change > 0 else "baissière"
            return {
                "text": f"ARBITRAGE P3: {data.get('symbol')} montre tendance {trend} ({price_change}%). Opportunité d'optimisation détectée avec volatilité {data.get('data', {}).get('volatility', 0)}",
                "confidence": round(random.uniform(0.85, 0.95), 2),
                "level": "🚀 AVANCÉ"
            }
        elif source_type == "scientific":
            return {
                "text": f"INNOVATION P3: Analyse de {data.get('papers_found', 0)} publications sur '{data.get('query')}' révèle convergence vers {', '.join(data.get('trending_topics', [])[:2])}",
                "confidence": round(random.uniform(0.88, 0.98), 2),
                "level": "🔬 SCIENTIFIQUE"
            }
        elif source_type == "social":
            sentiment = data.get('sentiment_analysis', {}).get('positive', 0) * 100
            return {
                "text": f"ARBITRAGE SOCIAL P3: Sentiment {sentiment:.1f}% positif sur '{data.get('topic')}'. Engagement élevé ({data.get('engagement_metrics', {}).get('mentions', 0)} mentions) suggère momentum croissant",
                "confidence": round(random.uniform(0.82, 0.92), 2),
                "level": "💬 SOCIAL"
            }
        elif source_type == "iot":
            anomalies = data.get('anomalies_detected', 0)
            return {
                "text": f"P3 IOT: {anomalies} anomalies détectées dans données {data.get('sensor_type')}. Conditions environnementales: {data.get('readings', {})}",
                "confidence": round(random.uniform(0.80, 0.90), 2),
                "level": "🌡️ ENVIRONNEMENTAL"
            }
        return None
    
    def get_data_stats(self):
        """Retourne les statistiques des données"""
        try:
            conn = sqlite3.connect('humean_data.db')
            cursor = conn.cursor()
            
            cursor.execute('SELECT COUNT(*) FROM raw_data')
            total_data = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM raw_data WHERE processed = TRUE')
            processed_data = cursor.fetchone()[0]
            
            cursor.execute('SELECT COUNT(*) FROM p3_insights')
            total_insights = cursor.fetchone()[0]
            
            # Stats par type de données
            cursor.execute('SELECT source_type, COUNT(*) FROM raw_data GROUP BY source_type')
            data_by_type = dict(cursor.fetchall())
            
            conn.close()
            
            return {
                "total_data_points": total_data,
                "processed_data": processed_data,
                "p3_insights_generated": total_insights,
                "data_sources_connected": len(self.data_sources),
                "data_by_type": data_by_type
            }
            
        except Exception as e:
            print(f"❌ Erreur stats: {e}")
            return {}
    
    def get_recent_insights(self, limit=5):
        """Récupère les insights récents"""
        try:
            conn = sqlite3.connect('humean_data.db')
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT i.insight_text, i.confidence_score, i.innovation_level, i.generated_at,
                       r.source_type
                FROM p3_insights i
                JOIN raw_data r ON i.raw_data_id = r.id
                ORDER BY i.generated_at DESC
                LIMIT ?
            ''', (limit,))
            
            insights = []
            for row in cursor.fetchall():
                insights.append({
                    "insight": row[0],
                    "confidence": row[1],
                    "level": row[2],
                    "timestamp": row[3],
                    "source": row[4]
                })
            
            conn.close()
            return insights
            
        except Exception as e:
            print(f"❌ Erreur récupération insights: {e}")
            return []

# Test du connecteur de données
if __name__ == "__main__":
    print("🧠 HUMEAN DATA CONNECTOR - Version Simplifiée")
    print("=" * 50)
    
    connector = HumeanDataConnector()
    
    # Test connexion multiples sources
    print("\n🔌 TEST CONNEXION MULTI-SOURCES:")
    connector.connect_financial_data("TSLA")
    connector.connect_financial_data("GOOGL")
    connector.connect_scientific_data("machine learning ethics")
    connector.connect_social_data("AI safety alignment")
    connector.connect_iot_data("environmental")
    
    # Génération insights P3
    print("\n🔮 GÉNÉRATION INSIGHTS P3:")
    connector.generate_p3_insights()
    
    # Affichage stats complètes
    print("\n📊 STATISTIQUES COMPLÈTES:")
    stats = connector.get_data_stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    # Insights récents
    print("\n💡 INSIGHTS RÉCENTS:")
    recent_insights = connector.get_recent_insights(3)
    for i, insight in enumerate(recent_insights, 1):
        print(f"   {i}. [{insight['source']}] {insight['insight'][:60]}...")
        print(f"      Confiance: {insight['confidence']} | Niveau: {insight['level']}")
    
    print("\n✅ HUMEAN DATA CONNECTOR - PRÊT POUR L'INTÉGRATION")
