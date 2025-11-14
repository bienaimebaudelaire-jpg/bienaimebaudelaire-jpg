# test_p3_force.py
import requests
import json

def test_p3_force():
    print("🧠 TEST P3 FORCÉ - Avec contexte explicite")
    print("=" * 60)
    
    payload = {
        "query": "JE VEUX UNE INNOVATION ARCHITECTURALE P3 - Crée une couche d'arbitrage pour conflits PPBE vs Governance avec mécanismes concrets",
        "context": {
            "force_phase_p3": True,
            "architectural_innovation": True,
            "expect_concrete_solution": True,
            "cognitive_depth": "maximum",
            "p3_modelling_required": True
        }
    }
    
    try:
        print("📡 Envoi de la requête P3 forcée...")
        response = requests.post("http://localhost:5000/search", json=payload, timeout=10)
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Réponse obtenue - {len(result.get('results', []))} résultats")
            
            # Vérification détaillée
            all_sources = [r.get('source', '') for r in result.get('results', [])]
            print(f"🔍 Sources détectées: {all_sources}")
            
            # Recherche spécifique de P3
            p3_results = [r for r in result.get('results', []) if 'p3' in r.get('source', '').lower()]
            
            if p3_results:
                print("🎉 MODÉLISATION P3 DÉTECTÉE !")
                for p3 in p3_results:
                    print(f"\n🚀 INNOVATION: {p3.get('title')}")
                    print(f"📝 {p3.get('snippet')}")
            else:
                print("❌ Aucun résultat P3 trouvé")
                print("Le serveur n'a pas la version avec modélisation P3")
                
        else:
            print(f"❌ Erreur HTTP: {response.status_code}")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    test_p3_force()
