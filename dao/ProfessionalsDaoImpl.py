import json
from .ProfessionalsDao import ProfessionalsDao
from connectors.goog_connector import GoogConnector


class ProfessionalsDaoImpl(ProfessionalsDao):
    LINKEDIN_SITE_RESTRICTION = 'site:linkedin.com/in'
    CRAWL = 'crawl'
    SEARCH = 'search'

    def __init__(self, args, career_paths_to_fetch):
      self.goog: GoogConnector = GoogConnector(args)
      self.career_paths_to_fetch = career_paths_to_fetch
      with open('start_indexes.json') as start_indexes_file:
        self.start_indexes = json.load(start_indexes_file)
      with open('career_paths.json') as career_paths_file:
        self.career_paths = json.load(career_paths_file)

    def __del__(self):
      with open('start_indexes.json', 'w') as start_indexes_file:
        json.dump(self.start_indexes, start_indexes_file)

    def fetch_professionals_by_career_path(self):
      responses_by_career_path = {}
      for career_path, info in self.career_paths_to_fetch.items():
        if career_path in self.career_paths:
          limit = info['limit']
          locations = info['locations']
          responses_by_career_path[career_path] = {}
          careers = self.career_paths[career_path]
          for career in careers:
            responses_by_career_path[career_path][career] = {}
            career_weight = self.career_paths[career_path][career]
            career_limit = int(limit * career_weight)
            for location in locations:
              responses_by_career_path[career_path][career][location] = []
              print(f'Fetching {career_limit} {career}s from {location}')
              results = self.fetch_professionals(career_limit, career, location)
              responses_by_career_path[career_path][career][location].extend(results)
      
        return responses_by_career_path   

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

      



