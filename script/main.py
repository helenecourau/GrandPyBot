import parser_class as p
import api_maps as a

user_value = "Salut GrandPy ! Est-ce que tu connais le 2 avenue florentine à colombes ?"
string = p.parser(user_value, "stop_words_fr.json")

REQUEST = a.Request(string)
REQUEST.request()
print(REQUEST.lat, REQUEST.lng)