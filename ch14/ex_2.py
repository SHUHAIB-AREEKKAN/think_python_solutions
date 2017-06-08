def sed(pattern,replace,file_1,file_2):
  try:
    f1=open(file_1,'r')
    f2=open(file_2,'w')
    for s in f1:
      s=s.replace(pattern,replace)
      f2.write(s)
    f1.close()
    f2.close()
  except IOError:
    print(' File Not found')
  except:
    print('something went wrong')    
  

sed('perfect','best','a.txt','b.txt')
