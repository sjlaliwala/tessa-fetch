from dao.articles_dao import ArticlesDao
from parsers.article_parser import ArticleParser
from itertools import islice

class ArticlesPipeline():
    def __init__(self, args, topics):
      self.topics = topics
      self.articles_dao = ArticlesDao(args)
      self.articles_count = {
        'extracted': 0,
        'transformed': 0,
        'loaded': 0
      }
      self.batch_size = 500

    def extract(self):
      topics_to_news_entries = {}
      for topic in self.topics:
        news_entries = self.articles_dao.fetch_articles_by_topic(topic)
        topics_to_news_entries[topic] = news_entries
        self.articles_count['extracted'] += len(news_entries)
      return topics_to_news_entries

    def transform(self, topics_to_news_entries):
      ids_to_news_articles = {}
      article_parser = ArticleParser()
      for topic, news_entries in topics_to_news_entries.items():
        for news_entry in news_entries:
          news_article = article_parser.parse_news_entry(news_entry)
          news_article['topic'] = topic
          ids_to_news_articles[news_entry['id']] = news_article
          
      self.articles_count['transformed'] = len(ids_to_news_articles) 
      return ids_to_news_articles

    def load(self, ids_to_news_articles):
      for news_article_batch in self.chunks(ids_to_news_articles, self.batch_size):
        self.articles_dao.batch_add_new_articles(news_article_batch)
        self.articles_count['loaded'] += len(news_article_batch)

    def chunks(self, data, size):
      chunks = []
      it = iter(data)
      for i in range(0, len(data), size):
        yield {k: data[k] for k in islice(it, size)}

    def run(self):
      topics_to_news_entries = self.extract()
      ids_to_news_articles = self.transform(topics_to_news_entries)
      self.load(ids_to_news_articles)
      print(self.articles_count)