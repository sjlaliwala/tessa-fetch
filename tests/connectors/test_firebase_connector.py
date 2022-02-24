import pytest
from connectors.firebase_connector import FirebaseConnector

@pytest.fixture
def firebase(args):
    fc = FirebaseConnector(args)
    assert fc.cred is not None
    return fc

@pytest.mark.integration
def test_get_firestore_client(firebase: FirebaseConnector):
    db = firebase.get_firestore_client()
    test_doc_ref = db.collection(u'tests').document(u'testConnection')
    test_doc = test_doc_ref.get()
    assert test_doc.exists
    test_doc_data = test_doc.to_dict()
    assert 'hi' in test_doc_data
    assert test_doc_data['hi'] == 'hi'
   


    
    