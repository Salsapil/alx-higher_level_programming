## InputOutput   
### 1- How to open a file   
**open() function with two arguments: filename and mode.**   
- my_file = open("data.txt", "r")   
   
### 2- How to write text in a file   
**write() method on the file object.**   
- my_file.write("This is some text!")   
   
### 3- How to read the full content of a file   
**read() method on the file object.**   
- file_content = my_file.read()   
   
### 4- How to read a file line by line   
**for loop with the readline() method.**   
- ```python
for line in my_file:   
    print(line)```   
   
### 5- How to move the cursor in a file   
**seek() method on the file object.**   
- my_file.seek().   
   
### 6- How to make sure a file is closed after using it   
**close() method on the file object.**   
- my_file.close()   
   
### 7- What is and how to use the with statement   
**Automatically opens and closes a file**   
   
### 8- What is JSON   
**Automatically opens and closes a file**   
- Text-based format for storing and transmitting data.   
- Similar to dictionaries in Python, uses key-value pairs.   
- Exchange data between server and web application.   
   
### 9- What is serialization   
- Converting a Python data structure into a JSON string.   
   
### 10- What is deserialization   
- Converting a JSON string back into a Python data structure.   
   
### 11- How to convert a Python data structure to a JSON string   
- json.dumps()   
   
### 12- How to convert a JSON string to a Python data structure   
- json.loads()   
   
****