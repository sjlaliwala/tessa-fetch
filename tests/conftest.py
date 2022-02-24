import pytest
from config import CONFIG

@pytest.fixture
def args():
    return CONFIG

