from config import CONFIG
from dao.ProfessionalsDaoImpl import ProfessionalsDaoImpl
from dao.ProfessionalsDao import ProfessionalsDao

def main(args):
  career_paths_to_fetch = {
    'Software Engineering': { 
        'limit': 1000,
        'locations': ['New York', 'San Francisco'] 
    }
  }
  article_topics_to_fetch = {
    'software engineering',
    'machine learning',
    'blockchain',
    'quantum computing',
    'artificial intelligence',
    'data mining',
    'big data',
    'virtual reality',
    'augmented reality',
    'metaverse',
    'web3',
    'cloud computing',
    'crypto',
    'devops',
    'ui ux',
    'fintech',
    'internet of things',
    'natural language processing',
    'robotics'
  }

if __name__ == '__main__':
    main(CONFIG)
    