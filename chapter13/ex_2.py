#! /usr/bin/python3/
# ex2.py -will be handling the raw book text into words ,remove punctuation
#remove stopwords, producing ranks and frequency for the  words
# and plot zipfs law as frequency vs ranks graph using matplotlib

import sys
import string   #for punctuation remover
import stopword  # to avoid stopwords 
import matplotlib.pyplot as plt  # to draw graph

# to remove punctuation and return lower cased splited words
def trim_1(ls):
  str_for=''
  for i in ls.read():
    if i not in string.punctuation:
      str_for=str_for+i 
  return (str_for.lower().split())

#produce ranks corressponding words and return list with insid tuple    
def procces_words(ws):# input is splited and lower word list
  # for ranks 
  rank_dict={}
  for words in ws:
  # avoid stopword like 'a' 'i' etc..
    if words not in stopword.stopwords:
  #generating rank or updating it
      if words in rank_dict:
        rank_dict[words] = rank_dict[words] + 1
      else:
        rank_dict[words]=0
    
  #sort with respect element values simple rank_dict.values
  word_freq=sorted(rank_dict.items(),key=lambda item:item[1])
  return word_freq  # [(word,rank)] for eg:[('sam',2)]

def freq_rank(wss): # input above list tuple structure
  rs=[]
  count=0
  freq=[x[1] for x in wss] # extract rank only
  freq.sort(reverse=True)  # reverse sort it like 200 ,199,198 ...etc
  for f in freq:
    count=count+1          # increment counter to create frequency 
    rs.append((f,count))   # return a list which contain (f and rank) eg (299,0)
  return rs                # return list of above

def graph_plot(ss):        # inputs above structure   
  scale='log'              
  fs=[x[0] for x in ss]   # extract first elemnt as frequency
  rk=[x[1] for x in ss]   # extract second element as rank
  plt.clf()               # all below rule of matplotlib
  plt.xscale(scale)
  plt.yscale(scale)
  plt.title("zipf's plot")
  plt.xlabel('Rank')
  plt.ylabel('Frequency')
  plt.plot(rk,fs,'r-')
  plt.show()  




# main stars

def main(name,filename='read_text.txt',*args):# u can input a text file
  # open a text file to process
  try:
    f=open(filename)
    for i in range(70):# skipping 70 line to avoid Headers of files
      next(f) 
  except IOError:
    print("File Doesn't exsisit")
    sys.exit(1)
  except StopIteration:
    print(" Files too small for a process input a file which is 80 lines or higher ")
    sys.exit(1)
  proc_words=procces_words(trim_1(f))  #input is output of trim_1 word list
  data_to_plot=freq_rank(proc_words)
  graph_plot(data_to_plot)

if __name__=='__main__':
  main(*sys.argv)

