import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseConnector():

    def __init__(self, args):
      self.cred = credentials.Certificate(args['firebase_config'])
      firebase_admin.initialize_app(self.cred, {
        'projectId': args['firebase_project'],
      })

    def get_firestore_client(self):
      return firestore.client()

    




        
        