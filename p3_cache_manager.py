# p3_cache_manager.py - Généré automatiquement par HUMEAN
import json
import hashlib
from datetime import datetime, timedelta

class P3CacheManager:
    def __init__(self):
        self.cache = {}
        self.cache_ttl = 3600  # 1 hour
    
    def get_cache_key(self, concept, domain):
        """Génère une clé de cache unique"""
        key_string = f"{concept}:{domain}:{datetime.now().strftime('%Y%m%d')}"
        return hashlib.md5(key_string.encode()).hexdigest()
    
    def cache_innovation(self, concept, domain, innovation_data):
        """Cache une innovation générée"""
        cache_key = self.get_cache_key(concept, domain)
        self.cache[cache_key] = {
            "data": innovation_data,
            "timestamp": datetime.now().isoformat(),
            "expires": (datetime.now() + timedelta(seconds=self.cache_ttl)).isoformat()
        }
        return cache_key
    
    def get_cached_innovation(self, concept, domain):
        """Récupère une innovation depuis le cache"""
        cache_key = self.get_cache_key(concept, domain)
        if cache_key in self.cache:
            cached_item = self.cache[cache_key]
            if datetime.fromisoformat(cached_item["expires"]) > datetime.now():
                return cached_item["data"]
            else:
                del self.cache[cache_key]
        return None

# Instance globale
p3_cache = P3CacheManager()
