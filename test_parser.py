import script.parser as script
import pytest

class TestParser:
	def test_return_string(user_value):
		file = "stop_words_fr.json"
		user_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		wanted_value = "OpenClassrooms"
		test_value = script.parser(user_value, file)
		assert test_value == wanted_value.lower()