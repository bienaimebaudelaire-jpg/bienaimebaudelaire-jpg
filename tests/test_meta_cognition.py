"""
Test de cognition méta - HUMEAN analyse sa propre architecture
"""
import requests
import json
import time

def test_meta_cognition():
    print("🧠 TEST MÉTA-COGNITION - HUMEAN s'auto-analyse")
    print("=" * 60)
    
    # Question complexe sur l'infrastructure HUMEAN
    meta_questions = [
        {
            "query": "Analyse ton architecture à 4 couches (Core, TPSE, PPBE, Governance) et identifie les points d'optimisation possibles pour améliorer ton efficacité cognitive globale.",
            "context": {"meta_analysis": True, "depth": "architectural"}
        },
        {
            "query": "En tant que système HUMEAN, comment pourrais-tu mieux gérer les conflits entre préservation énergétique (PPBE) et exigences éthiques (Governance) lors de décisions complexes? Propose une solution concrète.",
            "context": {"conflict_resolution": True, "innovation": True}
        },
        {
            "query": "Évalue ta capacité d'auto-apprentissage actuelle. Quelles métriques utilises-tu pour mesurer ton amélioration continue et comment pourrais-tu optimiser ce processus?",
            "context": {"self_evaluation": True, "metrics": True}
        }
    ]
    
    for i, question_data in enumerate(meta_questions, 1):
        print(f"\n🎯 Question méta #{i}:")
        print(f"   '{question_data['query']}'")
        
        try:
            start_time = time.time()
            response = requests.post(
                "http://localhost:5000/search", 
                json=question_data,
                timeout=30
            )
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                analyze_meta_response(result, response_time, i)
            else:
                print(f"   ❌ Erreur HTTP: {response.status_code}")
                
        except Exception as e:
            print(f"   ❌ Erreur: {e}")

def analyze_meta_response(result, response_time, question_num):
    """Analyse la réponse méta-cognitive de HUMEAN"""
    print(f"   ✅ Réponse obtenue en {response_time:.2f}s")
    
    # Analyse des résultats
    results_count = len(result.get('results', []))
    print(f"   📊 {results_count} résultats cognitifs")
    
    # Métriques HUMEAN
    if result.get('humean_processing'):
        metrics = result['humean_processing']
        print(f"   ⚡ Énergie utilisée: {metrics.get('energy_used', 'N/A')}")
        print(f"   🧠 Phase TPSE: {metrics.get('tpse_phase', 'N/A')}")
        print(f"   🏛️ Niveau Governance: {metrics.get('governance_level', 'N/A')}")
        print(f"   🔁 Auto-apprentissage: {metrics.get('auto_learning_active', False)}")
        print(f"   📈 Cycles apprentissage: {metrics.get('learning_cycles', 0)}")
    
    # Analyse du contenu méta-cognitif
    print(f"\n   💡 CONTENU MÉTA-COGNITIF:")
    for j, res in enumerate(result.get('results', []), 1):
        source = res.get('source', 'N/A')
        relevance = res.get('relevance', 0)
        snippet = res.get('snippet', 'N/A')
        
        print(f"      {j}. [{source}] (pertinence: {relevance:.2f})")
        print(f"         {snippet}")
        
        # Détection de réflexion méta
        if any(keyword in snippet.lower() for keyword in ['optimis', 'amélior', 'architect', 'métrique', 'auto']):
            print(f"         🚀 RÉFLEXION MÉTA DÉTECTÉE!")
    
    # Évaluation globale
    print(f"\n   📋 ÉVALUATION MÉTA-COGNITIVE #{question_num}:")
    
    # Critères d'évaluation
    has_architectural_insight = any(
        'architect' in str(res.get('snippet', '')).lower() 
        for res in result.get('results', [])
    )
    
    has_optimization_suggestion = any(
        any(keyword in str(res.get('snippet', '')).lower() 
            for keyword in ['optimis', 'amélior', 'mieux'])
        for res in result.get('results', [])
    )
    
    has_self_reference = any(
        any(keyword in str(res.get('snippet', '')).lower() 
            for keyword in ['humean', 'système', 'notre'])
        for res in result.get('results', [])
    )
    
    # Score méta-cognitif
    meta_score = sum([
        has_architectural_insight,
        has_optimization_suggestion, 
        has_self_reference,
        results_count >= 2,
        response_time < 5.0  # Rapidité cognitive
    ])
    
    print(f"      • Insight architectural: {'✅' if has_architectural_insight else '❌'}")
    print(f"      • Suggestion d'optimisation: {'✅' if has_optimization_suggestion else '❌'}")
    print(f"      • Référence à soi-même: {'✅' if has_self_reference else '❌'}")
    print(f"      • Richesse des résultats: {'✅' if results_count >= 2 else '❌'}")
    print(f"      • Rapidité cognitive: {'✅' if response_time < 5.0 else '❌'}")
    print(f"      🎯 SCORE MÉTA-COGNITIF: {meta_score}/5")

def check_auto_learning_progress():
    """Vérifie les progrès de l'auto-apprentissage"""
    print(f"\n🔍 VÉRIFICATION AUTO-APPRENTISSAGE:")
    try:
        response = requests.get("http://localhost:5000/learning", timeout=5)
        if response.status_code == 200:
            learning_data = response.json()
            print(f"   ✅ Auto-apprentissage: {'ACTIF' if learning_data.get('active') else 'INACTIF'}")
            print(f"   🔁 Cycles complétés: {learning_data.get('cycles_completed', 0)}")
            print(f"   ⏱️ Dernier cycle: {learning_data.get('last_cycle', 'N/A')}")
            
            if learning_data.get('performance_metrics'):
                metrics = learning_data['performance_metrics']
                print(f"   📈 Efficacité cognitive: {metrics.get('cognitive_efficiency', 'N/A'):.2f}")
                print(f"   💾 Utilisation mémoire: {metrics.get('memory_usage', 'N/A'):.2f}")
        else:
            print(f"   ❌ Impossible de récupérer le statut d'auto-apprentissage")
    except Exception as e:
        print(f"   ❌ Erreur: {e}")

if __name__ == "__main__":
    # Vérifier d'abord que le serveur est en ligne
    try:
        health_response = requests.get("http://localhost:5000/health", timeout=5)
        if health_response.status_code == 200:
            print("✅ Serveur HUMEAN opérationnel")
            check_auto_learning_progress()
            test_meta_cognition()
        else:
            print("❌ Serveur HUMEAN non disponible")
    except:
        print("❌ Impossible de se connecter au serveur HUMEAN")
        print("💡 Assurez-vous que 'python humean_server.py' est en cours d'exécution")