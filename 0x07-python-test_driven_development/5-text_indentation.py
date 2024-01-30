#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError("text must be a string")
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")