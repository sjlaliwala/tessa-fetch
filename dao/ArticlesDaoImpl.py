from .ArticlesDao import ArticlesDao
from connectors.goog_connector import GoogConnector

class ArticlesDaoImpl(ArticlesDao):
    NEWS = 'news'

    def __init__(self, args, topics):
      self.goog = GoogConnector(args)
      self.topics = topics

    def fetch_articles_by_topics(self):
      news_articles = {}
      for topic in self.topics:
        news_articles[topic] = self.fetch_articles(topic)
      return news_articles

    def fetch_articles(self, topic):
      query = {
        'q': topic,
      }
      news_response = self.goog.get(self.NEWS, query)
      return news_response