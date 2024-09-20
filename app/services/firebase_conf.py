
import os
import firebase_admin
from firebase_admin import credentials

class FirebaseConf():
    def __init__(self, firebase_storage_bucket: str):
        self.firebase_storage_bucket = firebase_storage_bucket
        self.init_firebase()

    def init_firebase(self):
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
        cred = credentials.Certificate(f"{os.path.join(project_root, 'firebase_key.json')}")
        firebase_admin.initialize_app(cred, {
            'storageBucket': self.firebase_storage_bucket
        })