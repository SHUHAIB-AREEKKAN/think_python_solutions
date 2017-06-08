#! /usr/bin/python3/

# punct_remover.py will remove punctuation in string
# read from file input and remove punctuation

import string

def punct_rem(file_name):
  trimmed_list=[]
  file_obj1=open(file_name)
  punct_text=file_obj1.read()
  file_obj1.close()
  #file_obj2=open(filename+'removed.txt')
  #file_obj2.close()
  print(punct_text)
  for s in punct_text:
    if s  in string.punctuation or s in string.whitespace:
      print('1')
      
    else:
      trimmed_list.append(s.lower())
      file_obj3=open(file_name+'removed.txt','a+')
      file_obj3.write(s.lower())
      file_obj3.close()
      
  print(trimmed_list)   

  
punct_rem('punct_contain.txt')

