import requests

import constants as c
import api_key as a

class Request:
    '''Requests and parses data from the OpenFoodFact API'''

    def __init__(self, adress):
        self.url = c.url + adress + c.key + a.maps_key
        self.lng = 0
        self.lat = 0

    def request(self):
        try:
            object_json = requests.get(self.url)
            object_json = object_json.json()
            self.lat = object_json['results'][0]['geometry']['location']['lat']
            self.lng = object_json['results'][0]['geometry']['location']['lng']
        except:
            print("Problème d'adresse")
            self.lat = 0
            self.lng = 0
        
        return self.lat, self.lng
