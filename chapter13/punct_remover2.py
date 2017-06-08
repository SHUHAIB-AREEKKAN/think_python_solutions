import string


def punct_rem(file_name):
  f=open(file_name)
  str1=f.read()
  sp=set(string.whitespace)
  pu=set(string.punctuation)
  str2=''.join(x for x in str1 if x not in pu)
  print(str2)

punct_rem('punct_contain.txt')
