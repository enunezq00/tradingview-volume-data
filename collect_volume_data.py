import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

def collect_volume_data():
    url = "https://api.tradingview.com/volume_data_endpoint"  # Replace with actual endpoint
    response = requests.get(url)
    data = response.json()
    save_volume_data(data)

def save_volume_data(data):
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    doc_ref = db.collection("volume_data").document("15_sec_data")
    doc_ref.set(data)

if __name__ == "__main__":
    collect_volume_data()
