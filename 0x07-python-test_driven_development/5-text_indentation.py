#!/usr/bin/python3
"""
module:
This is the fourth task
in Test-Driven-Development
"""


def text_indentation(text):
    """text identation

    Args:
        text: First arg

    Raises:
        TypeError: must be a string
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
