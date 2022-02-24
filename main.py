from config import CONFIG

import firebase_admin
from firebase_admin import credentials

from pipelines.articles_pipeline import ArticlesPipeline

def main(args):


  career_paths = {
    'Software Engineering': { 
        'limit': 1000,
        'locations': ['New York', 'San Francisco'] 
    }
  }
  news_topics = {
    'software engineering',
    'blockchain',
    'machine learning',
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
  articles_pipeline = ArticlesPipeline(args, news_topics)
  articles_pipeline.run()

if __name__ == '__main__':
    main(CONFIG)
    