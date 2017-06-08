#! /usr/bin/python3

# exc_2.py Designed to number of words and its frequency related problems
import string
import operator
def header_removed(inputs,outputs):
  fi=open(outputs,'w') #for clearing the writing file
  fi.close()
  str1=''
  with open(inputs) as f:
    next(f)
    next(f)
    for line in f:
      
      fi2=open(outputs,'a')
      fi2.write(line)
  fi2.close()    
  f.close()
def puncRemove(filename):
  f=open(filename,'r')
  punc=set(string.punctuation)
  rem=''.join(x for x in f.read() if x not in punc)
  #print(rem)
  return rem

def freq_analysis(str1):
  total=0
  j=0
  wordfreq={}
  str2=str1.split()
  unwanted_chars=".,-_=+{}[]/"
  for ins in str2:
    word=ins.strip(unwanted_chars)
    if word not in wordfreq:
      wordfreq[word]=0
    wordfreq[word]+=1 
  print(wordfreq)
  for i in wordfreq.values():
    total+=i
    j+=1
  print("total words"+str(total))
  print("the diffrent words are"+str(j))
  print("First Largest Twenty word")
  sot=sorted(wordfreq.items(),key=operator.itemgetter(1))
  j=0
  #print(str(j)+'that one j')
  #print(sot)
  for k in sot:
    j+=1
    if j<=20:
      print(k)


  return wordfreq
def dict_sum(dicta,dictb):
  s1=0
  s2=0
  for i in dicta.values():
    s1+=1
  for i in dictb.values():
    s2+=1
  if s1>s2:
    print("The Most extesive is First one")
  else:
    print("The Most extensive is Second one")
  
def cmp_with_list(dicta,lista):
  count=0
  print("The misiing word that are not in list")
  for i in dicta.keys():
    if i not in lista:
      count+=1
      print(i)
  print("the total missing words in it"+str(count))  










header_removed('abc.txt','new.txt')
rem1=puncRemove('new.txt')
mydict1={}
mydict1=freq_analysis(rem1)
mydict2={}
header_removed('abcd.txt','new1.txt')
rem2=puncRemove('new1.txt')
mydict2=freq_analysis(rem2)

dict_sum(mydict1,mydict2)
list_1=['so', 'privide', 'space', 'main', 'aspect', 'all', 'with', 'data']

cmp_with_list(mydict1,list_1)



