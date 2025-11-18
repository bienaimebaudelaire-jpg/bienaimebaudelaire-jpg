# test_simple.py
import requests

print("🧪 TEST SIMPLE DU SERVEUR HUMEAN")
print("=" * 40)

# Test des endpoints disponibles
endpoints = ["/", "/health", "/status", "/config", "/learning"]

for endpoint in endpoints:
    try:
        response = requests.get(f"http://localhost:5000{endpoint}", timeout=5)
        print(f"\n🔗 {endpoint}:")
        print(f"   Status: {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print(f"   ✅ JSON valide")
                if endpoint == "/status":
                    if 'p3_modelling_engine' in data:
                        print(f"   🚀 Moteur P3: {data['p3_modelling_engine']}")
                    else:
                        print(f"   ❌ Moteur P3: NON TROUVÉ")
            except:
                print(f"   ❌ Réponse non-JSON")
        else:
            print(f"   ❌ Erreur HTTP")
            
    except Exception as e:
        print(f"   💥 Exception: {e}")

print(f"\n🎯 VÉRIFICATION MOTEUR P3:")
try:
    status = requests.get("http://localhost:5000/status").json()
    if 'p3_modelling_engine' in status:
        print(f"   ✅ Moteur P3 présent: {status['p3_modelling_engine']}")
    else:
        print(f"   ❌ Moteur P3 ABSENT du statut")
        print(f"   📋 Clés disponibles: {list(status.keys())}")
except Exception as e:
    print(f"   💥 Erreur: {e}")
