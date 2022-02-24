import json
from connectors.goog_connector import GoogConnector

class ProfessionalsDao():
    LINKEDIN_SITE_RESTRICTION = 'site:linkedin.com/in'
    CRAWL = 'crawl'
    SEARCH = 'search'

    def __init__(self, args):
      self.goog: GoogConnector = GoogConnector(args)

    def fetch_professionals(self, limit, career, location=None, company=None):
      num_results = self.decide_num_results(limit)
      q = self.build_q(career, location, company)
      start_index = self.decide_start_index(q)
      query = {
          'q': q,
          'start': 0,
          'num': num_results,
          'hl': 'en',
          'gl': 'us'
      }
      result_counter = 0
      professionals_search_results = []
      while result_counter < limit:
          crawl_results = self.goog.get(self.CRAWL, query)
          professionals_search_results.append(crawl_results)
          result_counter += num_results
          self.start_indexes[q] += num_results

      return professionals_search_results

    def build_q(self, career, location, company):
      if company is None and location is None:
        return f'{self.LINKEDIN_SITE_RESTRICTION} "{career}"'
      elif company is None: 
        return f'{self.LINKEDIN_SITE_RESTRICTION} "{career}" "{location}"'
      elif location is None:
        f'{self.LINKEDIN_SITE_RESTRICTION} "{career}" "{company}"'
      else:
        return f'{self.LINKEDIN_SITE_RESTRICTION} "{career}" "{company}" "{location}"'

    def decide_num_results(self, career_limit):
      return career_limit if career_limit < 100 else 100

    def decide_start_index(self, q):
      if q not in self.start_indexes:
        self.start_indexes[q] = 0
      return self.start_indexes[q]

      



