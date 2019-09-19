'''Requests and formates data from the Google Maps API'''
import requests


class Maps:
    '''Two methods, one for requesting data and another to find the good data.'''

    def __init__(self):
        self.lat = 0
        self.lng = 0
        self.street = ''
        self.town = ''
        self.adress = ''
        self.object_json = ''

    def request(self, url):
        '''Requests map with the url'''
        self.object_json = requests.get(url)
        self.object_json = self.object_json.json()

        return self.object_json

    def return_data(self):
        '''Isolates latitude, longitude and adress components'''
        if self.object_json['status'] != 'ZERO_RESULTS':
            self.lat = self.object_json['results'][0]['geometry']['location']['lat']
            self.lng = self.object_json['results'][0]['geometry']['location']['lng']
            self.adress = self.object_json['results'][0]['formatted_address']
            for i in self.object_json['results'][0]['address_components']:
                if i['types'][0] == 'route':
                    self.street = i['long_name']
                elif len(i['types']) >= 2 and i['types'][1] == 'route':
                    self.street = i['long_name']
                else:
                    pass
                if i['types'][0] == 'locality':
                    self.town = i['long_name']
                elif len(i['types']) >= 2 and i['types'][1] == 'locality':
                    self.street = i['long_name']
                else:
                    pass

        return self.lat, self.lng, self.adress, self.street, self.town
