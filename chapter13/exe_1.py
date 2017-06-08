#! /usr/bin/python3

# exe_1.py strips whitespace , punctuation and conver into lower case


import string
str1=''
file_obj=open('abc.txt')
for i in file_obj.read():
  if i in  string.whitespace or i in string.punctuation:
    continue
  else:
    str1=str1+i


print(str1)
 
