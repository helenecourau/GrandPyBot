import pytest

import parser_class as script

class TestParser:
	def test_return_string(user_value):
		file = "backend/scripts/resources/stop_words_fr.json"
		user_value = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
		wanted_value = "OpenClassrooms"
		parser = script.ParserUser()
		test_value = parser.parser(user_value, file)
		assert test_value == wanted_value.lower()

	def test_return_string_error_value(user_value):
		file = "backend/scripts/resources/stop_words_fr.json"
		user_value = "Salut GrandPy ! "
		wanted_value = ""
		parser = script.ParserUser()
		test_value = parser.parser(user_value, file)
		assert test_value == wanted_value