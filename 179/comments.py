import re

class_three_indents = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''


def strip_comments(code):
    # see Bite description
    code_lines = code.splitlines()

    no_single_comments = [l for l in code_lines if not l.strip().startswith("#")]

    no_multiline_comments = []

    in_multiline = False
    for l in no_single_comments:
        if re.match(r'^\s*""".+"""$', l):
            continue

        if l.strip().startswith('"""') and not in_multiline:
            in_multiline = True
            continue

        if re.match(r'^.*"""$', l) and in_multiline:
            in_multiline = False
            continue

        if in_multiline:
            continue
        no_multiline_comments.append(l)

    final_lines = []
    for line in no_multiline_comments:
        m = re.search(r".*(  #.*)$", line)
        if m:
            line = line[: -len(m.group(1))]
        final_lines.append(line)
    return "\n".join(final_lines)


if __name__ == "__main__":
    print(class_three_indents)
    print("----")
    print(strip_comments(class_three_indents))
    print("----")
    print(code_bite_description)
    print("----")
    print(strip_comments(code_bite_description))
