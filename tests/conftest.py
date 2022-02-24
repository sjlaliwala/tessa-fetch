import pytest
from config import CONFIG
import firebase_admin


@pytest.fixture
def args():
    return CONFIG

@pytest.fixture
def news_topics():
    return [
      'software engineering',
    ]

@pytest.fixture
def career_paths_to_fetch():
    return { 
      'Software Engineering': { 
        'limit': 10,
        'locations': ['New York'] 
      } 
    }

@pytest.fixture
def initialize_firebase_app(args):
  self.cred = credentials.Certificate(args['firebase_config'])
  firebase_admin.initialize_app(self.cred, {
    'projectId': args['firebase_project'],
  })



