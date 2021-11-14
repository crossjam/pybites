import string


def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
    (1995, 19ab = numbers / Happy, happy4you = strings, hence for
     numbers you only need to check the first char of the word)
    """

    true_words = sorted([w for w in words if w[0] not in string.digits], key=str.lower)
    true_nums = sorted([w for w in words if w[0] in string.digits], key=str.lower)
    return true_words + true_nums
