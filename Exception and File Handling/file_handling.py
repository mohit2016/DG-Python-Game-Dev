# -*- coding: utf-8 -*-
"""File Handling

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yfKqaUqFb0mVrqbiPqKAUhJh28aXNaeO
"""

s = "This is a string.. I'm happy"

# Creating a New File
with open("new_file.txt", 'w') as f:
  f.write(s)

# read a file
with open("new_file.txt", 'r') as f:
  print(f.read())

with open("new_file.txt", 'r') as f:
  print(f.tell()) # --> tells the pointer location
  print(f.read(5))# --> reads your data
  print(f.tell())
  print(f.read(10))
  print(f.tell())
  f.seek(0) # ----> jo bhi index daaloge vahan pe pointer chala jaega.
  print(f.tell())
  print(f.read())

#  reading the 10th character

# f.seek(10)
# f.read(1)

new_str = """This is first line.
This is second line.
This is third line"""

print(new_str)

with open("multi_line.txt", 'w') as f:
  f.write(new_str)

with open("multi_line.txt",'r') as f:
  file_data = f.readlines()
  f.seek(0)
  for line in f.readlines():
    print(line)

print(file_data)

# Append MOde...
with open("multi_line.txt", 'a') as f:
  f.write("\nThis will be new content")

