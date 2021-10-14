"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

import string

TMP = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(TMP, "dictionary_m_words.txt")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/dictionary_m_words.txt", DICTIONARY
)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
    Case insensitive, so Madam is valid too.
    It should work for phrases too so strip all but alphanumeric chars.
    So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    word_chars = [c for c in word.lower() if c in string.ascii_lowercase]
    word_chars_reversed = word_chars[:]
    word_chars_reversed.reverse()
    return all([c1 == c2 for c1, c2 in zip(word_chars, word_chars_reversed)])


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
    If called without argument use the load_dictionary helper
    to populate the words list"""

    words = words if words else load_dictionary()

    palindromes = [word for word in words if is_palindrome(word)]
    palindromes.sort(key=len, reverse=True)
    return palindromes[0]
