import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

class FirebaseConnector():

    def __init__(self, args):
      self.cred = credentials.Certificate(args['firebase_config'])
      try:
        firebase_admin.get_app()
      except ValueError:
        firebase_admin.initialize_app(self.cred, {
          'projectId': args['firebase_project'],
        })
      
      self.db = firestore.client()

    def get_firestore_client(self):
      return self.db

    




        
        