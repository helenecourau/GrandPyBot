import re

def parser(user_value, file):
	stop_word_file = open(file, "r")
	stop_word = stop_word_file.read()
	i = 0
	final_list = []
	final_string = ""
	user_value = user_value.lower()
	user_value = re.split('[ -.;/,!\'?]', user_value)
	for i in user_value:
		if i not in stop_word:
			final_list.append(i)
	final_string = " ".join(final_list)
	return final_string