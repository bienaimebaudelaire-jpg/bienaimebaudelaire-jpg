// FICHIER: humean-unified.js - À ajouter dans toutes les pages
const HUMEAN_API = {
    baseURL: "http://127.0.0.1:5000/api/v1",
    
    async getStatus() {
        const response = await fetch(this.baseURL + "/status");
        return await response.json();
    },
    
    async startLearning() {
        const response = await fetch(this.baseURL + "/start-learning");
        return await response.json();
    },
    
    async analyze() {
        const response = await fetch(this.baseURL + "/analyze");
        return await response.json();
    },
    
    async getInsights() {
        const response = await fetch(this.baseURL + "/insights");
        return await response.json();
    }
};

// Utilisation universelle
window.HumeanAPI = HUMEAN_API;
