from textwrap import wrap
from itertools import zip_longest

COL_WIDTH = 20

TEXT = """My house is small but cosy.

    It has a white kitchen and an empty fridge.

    I have a very comfortable couch, people love to sit on it."""


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
    newlines (\n\n) in text determines the amount of columns.
    Return a string with the column output like:
    line1\nline2\nline3\n ... etc ...
    See also the tests for more info."""
    chunks = text.split("\n\n")

    cols = [wrap(chunk.strip(), width=COL_WIDTH, initial_indent="") for chunk in chunks]

    rows = zip_longest(*cols, fillvalue="")

    lines = [
        " ".join(
            ["{:<{width}}".format(col_line, width=COL_WIDTH) for col_line in col_lines]
        )
        for col_lines in rows
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    print(text_to_columns(TEXT))
