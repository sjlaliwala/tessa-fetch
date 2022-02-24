from dao.professionals_dao import ProfessionalsDao

      # with open('start_indexes.json', 'w') as start_indexes_file:
      #   json.dump(self.start_indexes, start_indexes_file)

class ProfessionalsPipeline():
    def __init__(self, args, career_paths_to_fetch):
      self.career_paths_to_fetch = career_paths_to_fetch
      self.professionals_dao = ProfessionalsDao(args)
      with open('start_indexes.json') as si_file:
        self.start_indexes = json.load(si_file)
      with open('career_paths.json') as cp_file:
        self.career_paths = json.load(cp_file)

    def extract(self):
      responses_by_career_path = {}
      for career_path, info in self.career_paths_to_fetch.items():
        if career_path in self.career_paths:
          careers = self.career_paths[career_path]
          limit = info['limit']
          locations = info['locations']
          responses_by_career_path[career_path] = {}
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

    def transform():
        pass

    def load():
        pass

    def run():
        pass
        