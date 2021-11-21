INDENTS = 4

POEM = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
"""


def print_hanging_indents(poem):

    prev_line = ""
    for line in poem.splitlines():
        cur_line = line.strip()
        if not cur_line:
            prev_line = cur_line
            continue
        else:
            indent = " " * (INDENTS if prev_line else 0)
            print(f"{indent}{cur_line}")

        prev_line = cur_line


if __name__ == "__main__":
    print_hanging_indents(POEM)
