class ArticleParser():
  def __init__(self):
    pass
  
  def parse_news_entry(self, news_entry):
    return {
      'title': news_entry['title'],
      'published': news_entry['published'],
      'summary': news_entry['summary'],
      'link': news_entry['link'],
      'source': news_entry['source'],
      'content': None
    }
    