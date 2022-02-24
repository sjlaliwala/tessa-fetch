import pytest
from dao.ArticlesDaoImpl import ArticlesDaoImpl

@pytest.fixture
def article_topics_to_fetch():
    return [
      'blockchain'
    ]

@pytest.fixture 
def articles_dao(args, article_topics_to_fetch):
  return ArticlesDaoImpl(args, article_topics_to_fetch)

@pytest.fixture
def mock_articles_dao(mocker, args, article_topics_to_fetch):
  def mock_get(self, endpoint, query):
      return {'feed': {}, 'entries': []}
  mocker.patch(
      'dao.ArticlesDaoImpl.GoogConnector.get',
      mock_get
  )
  return ArticlesDaoImpl(args, article_topics_to_fetch)

@pytest.mark.integration
def test_fetch_articles_schema(articles_dao: ArticlesDaoImpl, article_topics_to_fetch):
  response = articles_dao.fetch_articles(article_topics_to_fetch[0])
  assert 'feed' in response
  assert 'entries' in response

@pytest.mark.unit
def test_fetch_articles_by_topic_mocking_goog_get(mock_articles_dao: ArticlesDaoImpl):
  expected = {'blockchain': {'feed': {}, 'entries': []}}
  actual = mock_articles_dao.fetch_articles_by_topics()
  expected == actual

@pytest.mark.unit
def test_fetch_articles_mocking_goog_get(mock_articles_dao: ArticlesDaoImpl, article_topics_to_fetch):
  expected = {'feed': {}, 'entries': []}
  actual = mock_articles_dao.fetch_articles(article_topics_to_fetch[0])
  expected == actual







