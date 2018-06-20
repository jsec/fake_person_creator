import os
import pytest


@pytest.fixture
def test_file():
    rootdir = os.path.dirname(os.path.abspath(__file__))
    file_location = os.path.join(rootdir, 'fixtures/test_data')

    with open(file_location, 'rb') as file:
        test_data = file.read()
    return test_data


@pytest.fixture
def mock_request(requests_mock):
    requests_mock.get('https://fakepersongenerator.com', text='testdata')
