import random
import string

raw_words=''

spset=['?',',','.','!','+','#','$']

def File_Reader(filename):
  cleanstring=[]
  file_obj=open(filename)
  for line in file_obj:
    for word in  line.rstrip().split():
      print("1:"+word.strip('?,.'))
      
  
    






str2=File_Reader('emma.txt')
print(str2)

"""
      
      
def header_end(file_obj):
  for line in file_obj:
    if line.startswith('END'):
      break
"""

