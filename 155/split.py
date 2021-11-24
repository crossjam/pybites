import re


def split_words_and_quoted_text(text):
    """Split string text by space unless it is
    wrapped inside double quotes, returning a list
    of the elements.

    For example
    if text =
    'Should give "3 elements only"'

    the resulting list would be:
    ['Should', 'give', '3 elements only']
    """

    # for some reason, order of capture groups matters, ?!
    words_rgx = re.compile(r'("[^"]+")|(\S+)')
    # words_rgx = re.compile(r'(\S+)|("[^"]+")')
    return [qword[1:-1] if qword else word for qword, word in words_rgx.findall(text)]


if __name__ == "__main__":
    print(split_words_and_quoted_text('Should give "3 elements only"'))
