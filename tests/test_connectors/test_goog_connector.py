import pytest
from connectors.goog_connector import GoogConnector

@pytest.fixture
def goog(args):
    return GoogConnector(args)

@pytest.mark.integration
def test_get(goog: GoogConnector):
    q = {'q': 'google', 'num': 1}
    response = goog.get('crawl', q)
    assert 'results' in response
    assert 'html' in response

