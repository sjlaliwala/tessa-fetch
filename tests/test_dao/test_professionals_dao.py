import pytest
from dao.professionals_dao import ProfessionalsDao



@pytest.mark.integration
def test_fetch_professionals_schema(args, career_paths_to_fetch):
    professionals_dao = ProfessionalsDao(args, career_paths_to_fetch)
    response = professionals_dao.fetch_professionals(1, 'software engineer')
    assert 'results' in response[0]
    assert 'html' in response[0]
    

# @pytest.mark.unit
# def test_fetch_professionals_mocking_goog_get(mocker, args, career_paths_to_fetch):
#     expected = [{'results': {'html': ['swe']}}]
#     def mock_get(self, endpoint, query):
#         return {'results': {'html': ['swe']}}
#     mocker.patch(
#         'dao.ProfessionalsDao.GoogConnector.get',
#         mock_get
#     )
#     professionals_dao = ProfessionalsDao(args, career_paths_to_fetch)
#     actual = professionals_dao.fetch_professionals(1, 'software engineer')
#     assert expected == actual

# @pytest.mark.unit
# def test_fetch_professionals_by_career_path_mocking_goog_get(mocker, args, career_paths_to_fetch):
#     expected = {'Software Engineering': {'Software Engineer': {'New York': [{'results': {'html': ['nyc swe', 'nyc swe', 'nyc swe']}}]}, 'Senior Software Engineer': {'New York': [{'results': {'html': ['nyc swe']}}]}, 'Staff Engineer': {'New York': []}, 'Senior Staff Software Engineer': {'New York': []}, 'Principal Engineer': {'New York': []}, 'Engineering Manager': {'New York': [{'results': {'html': ['nyc swe', 'nyc swe']}}]}, 'Senior Engineering Manager': {'New York': []}, 'Distinguished Engineer': {'New York': []}, 'Director of Engineering': {'New York': []}, 'Senior Director of Engineering': {'New York': []}, 'VP of Engineering': {'New York': []}}}
#     def mock_get(self, endpoint, query):
#         return {'results': {'html': ['nyc swe'] * query['num']}}
#     mocker.patch(
#         'dao.ProfessionalsDao.GoogConnector.get',
#         mock_get
#     )
#     professionals_dao = ProfessionalsDao(args, career_paths_to_fetch)
#     actual = professionals_dao.fetch_professionals_by_career_path()
#     assert expected == actual
    
    



