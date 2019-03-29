
import re
import codecs

from collections import Counter


def _words(text):
    return re.findall(r'\w+', text.lower())


WORDS = Counter(_words(codecs.open('check_spell/russian.txt', 'r', 'cp1251').read()))


def _unknown(text):
    return [x for x in text if not WORDS.get(x)]


def check(text):
    """
    :param text: Text for checking
    :return: Return list of words which are wrongly spelled
    """
    return _unknown(_words(text))
