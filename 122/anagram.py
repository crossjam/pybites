from collections import Counter


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
    an anagram of word1, ignore case and spacing.
    About anagrams: https://en.wikipedia.org/wiki/Anagram"""

    chars1 = Counter([c.lower() for c in word1 if c.strip()])
    chars2 = Counter([c.lower() for c in word2 if c.strip()])

    return chars1 == chars2


if __name__ == "__main__":
    print(is_anagram("binary", "brainy"))
    print(is_anagram("anagram", "naga ram"))
    print(is_anagram("Anagram", "Naga Ram"))
    print(is_anagram("anagrams", "naga ram"))
