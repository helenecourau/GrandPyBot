import pytest
import requests

import api_maps as script

given_data = {
        "results" : [
            {
                "address_components" : [
                    {
                        "long_name" : "7",
                        "short_name" : "7",
                        "types" : [ "street_number" ]
                    },
                    {
                        "long_name" : "Cité Paradis",
                        "short_name" : "Cité Paradis",
                        "types" : [ "route" ]
                    },
                    {
                        "long_name" : "Paris",
                        "short_name" : "Paris",
                        "types" : [ "locality", "political" ]
                    },
                ],
                "formatted_address" : "7 Cité Paradis, 75010 Paris, France",
                "geometry" : {
                    "location" : {
                        "lat" : 48.8748465,
                        "lng" : 2.3504873
                    },
                },
            }
        ],
        "status" : "OK"
    }

def  test_request(monkeypatch):
    
    class MockResponse:

        @staticmethod
        def json():
            return given_data

    def mock_api_google_maps(*args, **kwargs):       
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_api_google_maps)
    maps = script.Maps()
    assert maps.request('url') == given_data

def  test_return_data():       
    wanted_value = (48.8748465, 2.3504873, "7 Cité Paradis, 75010 Paris, France", "Cité Paradis", "Paris")
    maps = script.Maps()
    maps.object_json = given_data
    test_value = maps.return_data()
    assert test_value == wanted_value

error_data = {'results': [], 'status': 'ZERO_RESULTS'}
def  test_request_error(monkeypatch):
    
    class MockResponseError:

        @staticmethod
        def json():
            return error_data

    def mock_api_google_maps_error(*args, **kwargs):       
        return MockResponseError()

    monkeypatch.setattr('requests.get', mock_api_google_maps_error)
    maps = script.Maps()
    assert maps.request('url') == error_data

def  test_return_data_error():       
    wanted_value = (0, 0, "", "", "")
    maps = script.Maps()
    maps.object_json = error_data
    test_value = maps.return_data()
    assert test_value == wanted_value