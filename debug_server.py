# debug_server.py
import requests
import json

def debug_server():
    print("🐛 DEBUG SERVEUR HUMEAN")
    print("=" * 50)
    
    # Test des endpoints de base
    endpoints = [
        ("GET", "/", "Accueil"),
        ("GET", "/health", "Santé"),
        ("GET", "/status", "Statut"),
        ("GET", "/config", "Configuration"),
        ("GET", "/learning", "Apprentissage")
    ]
    
    for method, endpoint, description in endpoints:
        try:
            url = f"http://localhost:5000{endpoint}"
            if method == "GET":
                response = requests.get(url, timeout=5)
            else:
                response = requests.post(url, timeout=5)
            
            print(f"\n{description} ({endpoint}):")
            print(f"  Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(f"  ✅ JSON valide - Keys: {list(data.keys())}")
                except:
                    print(f"  ❌ JSON invalide - Content: {response.text[:100]}")
            else:
                print(f"  ❌ Erreur HTTP")
                
        except Exception as e:
            print(f"  💥 Exception: {e}")
    
    # Test spécifique search
    print(f"\n🔍 TEST ENDPOINT /search:")
    try:
        payload = {"query": "test debug", "context": {}}
        response = requests.post("http://localhost:5000/search", json=payload, timeout=5)
        print(f"  Status: {response.status_code}")
        print(f"  Content-Type: {response.headers.get('content-type')}")
        print(f"  Content: {response.text[:500]}")
    except Exception as e:
        print(f"  💥 Exception: {e}")

if __name__ == "__main__":
    debug_server()
