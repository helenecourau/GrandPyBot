'''Requests and parses data from the Google Maps API'''
import requests


class Wikimedia:
    '''Two methods for searching data, by name or by coordinates.'''

    def __init__(self):
        self.data_wiki = {}
        self.data_geo = {}

    def opensearch(self, search):
        '''Search by name'''
        #request = requests.Session()
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "opensearch",
            "namespace": "0",
            "search": search,
            "limit": "1",
            "format": "json"
            }

        result = requests.get(url=url, params=params)
        data = result.json()
        self.data_wiki = {'title': data[1],
                          'description': data[2],
                          'url': data[3]}
        return self.data_wiki

    def geosearch(self, lat, lng):
        '''Search with latitude and longitude'''
        url = "https://fr.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "generator": "geosearch",
            "ggsradius": 10000,
            "ggslimit": 1,
            "ggscoord": str(lat) + "|" + str(lng),
            "format": "json"
            }

        result = requests.get(url=url, params=params)
        data = result.json()
        if 'query' in data:
            for value in data['query']['pages']:
                self.data_geo = {'title': data['query']['pages'][value]['title']}
        return self.data_geo
