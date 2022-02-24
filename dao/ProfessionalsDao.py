from abc import ABC, abstractmethod

class ProfessionalsDao(ABC):

    @abstractmethod
    def fetch_professionals_by_career_path(self):
        pass

    @abstractmethod
    def fetch_professionals(self, limit, career, location=None, company=None):
        pass
