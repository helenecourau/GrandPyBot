import pytest
import requests

import api_wikimedia as script

def test_wikimedia_opensearch(monkeypatch):
    data = ['cité paradis', ['Cité Paradis'], ['La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'], ['https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis']]

    class MockResponse:

        @staticmethod
        def json():
            return data

    def mock_api_wikimedia_opensearch(*args, **kwargs):       
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_api_wikimedia_opensearch)
    wiki = script.Wikimedia()
    wanted_value = {'title': ['Cité Paradis'], 
                    'description': ['La cité Paradis est une voie publique située dans le 10e arrondissement de Paris.'], 
                    'url': ['https://fr.wikipedia.org/wiki/Cit%C3%A9_Paradis']}
    assert wiki.opensearch('search') == wanted_value


def test_wikimedia_geosearch(monkeypatch):
    data = {'batchcomplete': '', 
                  'query': {'pages': {'6029848': 
                  {'pageid': 6029848, 'ns': 0, 'title': 'Hôtel Titon', 'index': -1}}}}

    class MockResponse:

        @staticmethod
        def json():
            return data

    def mock_api_wikimedia_geosearch(*args, **kwargs):       
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_api_wikimedia_geosearch)
    wiki = script.Wikimedia()
    wanted_value = {'title': 'Hôtel Titon'}
    assert wiki.geosearch('lat', 'lng') == wanted_value


def test_wikimedia_opensearch_error(monkeypatch):
    data = ['nothinguseful', [], [], []]

    class MockResponseError:

        @staticmethod
        def json():
            return data

    def mock_api_wikimedia_opensearch_error(*args, **kwargs):       
        return MockResponseError()

    monkeypatch.setattr('requests.get', mock_api_wikimedia_opensearch_error)
    wiki = script.Wikimedia()
    wanted_value = {'title': [], 'description': [], 'url': []}
    assert wiki.opensearch('search') == wanted_value


def test_wikimedia_geosearch_error(monkeypatch):
    data = {'error'}

    class MockResponseError:

        @staticmethod
        def json():
            return data

    def mock_api_wikimedia_geosearch_error(*args, **kwargs):       
        return MockResponseError()

    monkeypatch.setattr('requests.get', mock_api_wikimedia_geosearch_error)
    wiki = script.Wikimedia()
    wanted_value = {}
    assert wiki.geosearch('lat', 'lng') == wanted_value