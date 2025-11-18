import requests
import time

print("🧪 Test des routes du serveur HUMEAN...")
base_url = "http://127.0.0.1:5000"

routes = [
    "/",
    "/api/health", 
    "/api/system-status",
    "/api/models",
    "/status"  # Ancienne route peut-être
]

for route in routes:
    try:
        response = requests.get(f"{base_url}{route}", timeout=5)
        print(f"✅ {route}: {response.status_code}")
        if response.status_code == 200:
            print(f"   Contenu: {len(response.text)} caractères")
    except Exception as e:
        print(f"❌ {route}: {e}")
    
    time.sleep(0.5)
