import shelve 
import sys

from anagram_sets import *

def store_anagram(filename,dict1):
  dbs=shelve.open(filename,'c')
  for x,y in dict1.iteritems():
    dbs[x]=y
  dbs.close()

def read_anagram(filename,word):
  dbs=shelve.open(filename)
  res=signature(word)
  try:
    return dbs[res]
  except KeyError:
    return []

def main(name, command='store'):
    if command == 'store':
        ad = all_anagrams('words')
        store_anagram('anagrams.db', ad)
    else:
        print (read_anagram('anagrams.db', command))

if __name__=='__main__':
  main(*sys.argv)



