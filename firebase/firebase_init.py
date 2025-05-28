import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase/firebase_config.json")

# Check if app already initialized
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
