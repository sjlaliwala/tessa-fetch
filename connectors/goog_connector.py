import urllib
import requests 

class GoogConnector():
  GOOG_BASE_URL = 'https://api.goog.io/v1'
  def __init__(self, args):
    self.headers = {
        'apikey': args['goog_api_key']
    }

  def get(self, endpoint, query):
    url = f'{self.GOOG_BASE_URL}/{endpoint}/{urllib.parse.urlencode(query)}'
    return requests.get(url, headers=self.headers).json()

