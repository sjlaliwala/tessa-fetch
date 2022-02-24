from connectors.goog_connector import GoogConnector
from connectors.firebase_connector import FirebaseConnector

class ArticlesDao():
    NEWS = 'news'

    def __init__(self, args):
      self.goog = GoogConnector(args)
      self.db = FirebaseConnector(args).get_firestore_client()
      self.batch = self.db.batch()

    def fetch_articles_by_topic(self, topic):
      query = {
        'q': topic,
      }
      news_response = self.goog.get(self.NEWS, query)
      return news_response['entries']

    def batch_add_new_articles(self, news_article_batch):
      for id, article in news_article_batch.items():
        article_ref = self.db.collection('articles').document(id)
        self.batch.set(article_ref, article)
      self.batch.commit()
      


