from abc import ABC, abstractmethod

class ArticlesDao(ABC):
    
    @abstractmethod
    def fetch_articles_by_topics(self):
        pass
    
    @abstractmethod
    def fetch_articles(topic):
        pass
