'''File to parse the value sent by the user.'''
import os
import re
import unidecode
import nltk
from nltk.tag import StanfordPOSTagger

from backend.scripts.resources import constants as c

nltk.internals.config_java("backend/scripts/resources/Java/javapath_target_7607531/java.exe")


def parser(user_value, file):
    '''StanfordPOSTagger for remove verbs, remove, stop words and formate value'''
    i, final_list = 0, []

    # init path for java and StanfordPOSTagger
    os.environ['JAVAHOME'] = c.java_path

    # read stop_word file
    stop_word_file = open(file, "r")
    stop_word = stop_word_file.read()

    # lower case
    user_value = user_value.lower()

    # split words
    user_value = re.sub('[.;,!?]', '', user_value)
    user_value = re.sub('[\']', ' ', user_value)
    user_value = re.split('[ -/]', user_value)

    pos_tagger = StanfordPOSTagger(c.model, c.jar, encoding='utf8')
    user_value = pos_tagger.tag(user_value)

    for i in user_value:
        if i[1] not in ['V', 'VINF', 'ADVWH', 'P', 'ADV', 'C', 'CLS'] and unidecode.unidecode(i[0]) not in stop_word:
            final_list.append(i[0])
    user_value = " ".join(final_list)

    return user_value
