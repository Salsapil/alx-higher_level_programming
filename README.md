The output of the print function is send to the standard output stream (sys.stdout) by default. By redefining the keyword parameter "file" we can send the output into a different stream.

fh = open("data.txt","w")
print("42 is the answer, but what is the question?", file=fh)
fh.close()

positional parameters:
"First argument: {0}, second one: {1}".format(47,11)
keyword parameters:
"Art: {a:5d},  Price: {p:8.2f}".format(a=453, p=59.058)
- we can precede the formatting with a "<" (left justify) or ">" (right justify).

print("The capital of {province} is {capital}".format(**data))
The double "*" in front of data turns data automatically by order

S.center(width[, fillchar]) -> str 
S.ljust(width[, fillchar]) -> str 
S.rjust(width[, fillchar]) -> str 

slicing string:
Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
output: orl

- strip() remove the space before and/or after the actual text.

isinstance = bool