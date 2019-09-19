'''Calls parser and requests API'''
import random

from backend.scripts import parser_class as p
from backend.scripts import api_maps as m
from backend.scripts import api_wikimedia as w
from backend.scripts.resources import constants as c
from backend.scripts.resources import api_key as a


class ParseRequest:

    def __init__(self):
        self.lng, self.lat = 0, 0
        self.adress, self.title = '', ''
        self.description, self.url = '', ''
        self.random_sentence = ''
        self.street, self.town = '', ''

    def script(self, user_value):
        '''Calls parser, then google maps API,
        then Wikimedia API and init random sentence for GrandPy.'''

        user_value = p.parser(user_value,
                              'backend/scripts/resources/stop_words_fr.json')

        url = c.url + user_value + c.key + a.maps_key
        url_alt = c.url + user_value + c.key + a.maps_key + '&language=fr-FR'
        maps = m.Maps()
        maps.request(url)
        if maps.object_json['status'] == 'ZERO_RESULTS':
            maps.request(url_alt)

        maps.return_data()
        self.lat, self.lng = maps.lat, maps.lng
        self.adress = maps.adress
        self.street, self.town = maps.street, maps.town

        wikimedia = w.Wikimedia()
        if maps.lat:
            wikimedia.opensearch(maps.street + ' ' + maps.town)
            if not wikimedia.data_wiki['description']:
                wikimedia.opensearch(maps.street)
            if not wikimedia.data_wiki['description']:
                wikimedia.geosearch(maps.lat, maps.lng)
                wikimedia.opensearch(wikimedia.data_geo['title'])
            if not wikimedia.data_wiki['description']:
                wikimedia.opensearch(maps.town)
            if not wikimedia.data_wiki['description']:
                wikimedia.opensearch(user_value)
        else:
            wikimedia.opensearch(user_value)

        self.title = wikimedia.data_wiki['title']
        self.description = wikimedia.data_wiki['description']
        self.url = wikimedia.data_wiki['url']

        number = random.randint(0, len(c.grandPy_sentences)-1)
        self.random_sentence = c.grandPy_sentences[number]

