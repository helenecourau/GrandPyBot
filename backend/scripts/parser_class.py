'''File to parse the value sent by the user.'''
import os
import re
import unidecode

from backend.scripts.resources import constants as c

def parser(user_value, file):

    i, final_list = 0, []

    # read stop_word file
    stop_word_file = open(file, "r")
    stop_word = stop_word_file.read()
    stop_word = stop_word.split(",")

    # lower case
    user_value = user_value.lower()

    # split words
    user_value = re.sub('[.;,!?]', '', user_value)
    user_value = re.sub('[\']', ' ', user_value)
    user_value = re.split('[ -/]', user_value)

    for i in user_value:
        if unidecode.unidecode(i) not in stop_word:
            final_list.append(i)
    user_value = " ".join(final_list)

    return user_value
