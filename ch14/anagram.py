# find out anagram experiement 


def init_words(fname): # file name
  words={}    
# with open method f (object of file) will closed with in 'with open' premises
       
  with open(fname) as f: 
    for line in f:    # read line by one by one not entire which is readlinees()
      word=line.strip().lower()# strip every word and put in dict
      words[word]=1
  return words               # return dict {'some':1}


def init_anagram_dict(words): # to generate anagram by words.keys() keys of dict
  anagram_dict={}
  for word in words: #join sorted list 'the list contain a word in stripped mode
# like kids->list['k','i','d','s'] and next we will sort it alphabetically so
# ['d','i','k','s'] and using join we will make it 'diks'
    sorted_word=''.join(sorted(list(word)))# like kids->list['k','i','d','s']
    if sorted_word not in anagram_dict:#check if sorted word is in dict,if not  
      anagram_dict[sorted_word]=[]     # add word as key  and make empty list[]
    anagram_dict[sorted_word].append(word) #else already  anagram then append to
# the list
  return anagram_dict
#check if word user provide is anagram or not
#if its and anagram is lenght 2 or more then print 
def is_anagram(word,anagram_dict): 
  key=''.join(sorted(list(word)))
  if key in anagram_dict:
    values=anagram_dict[key]
  else:
    values=[]
  if len(values)>=2:
    print("Anagram found: ",)
    print("dict keys"+str([x for x,v in anagram_dict.items() if v==values]),)
    print(values)
    print("user input : "+word)
  elif len(values)>1:
    print("This input has no Anagram!")
  else:
    print("word not found! in dictionary sorry")






if __name__=='__main__':
  filename='words'     #filename of file to generate anagrams

  dict_words=init_words(filename)
  proc_anagram=init_anagram_dict(dict_words.keys())
  is_anagram('shuhaib',proc_anagram)
  
