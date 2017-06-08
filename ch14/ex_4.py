import os


#def travel_dir(path):
  


def print_dir_files(dirname):
  mp3_list=[]
  for f in os.listdir(dirname):
    path=os.path.join(dirname,f)
    if os.path.isdir(path):
      #print('D: '+os.path.abspath(f))
      print_dir_files(path)  
    else:
      str1=os.path.basename(os.path.abspath(f))
      if str1.endswith('.mp3'):
        mp3_list.append(os.path.abspath(f))        
  return mp3_list 

   
def generate_checksum(list_mp3):
  mdsum={}
  f=open('list.txt','w+')
  for filename in list_mp3:
     f.write(filename+'\n')
   # cmd='md5sum '+filename
   # fp=os.popen(cmd)
   # res=fp.read()
   # print(res)  
   # fp.close()
  f.close()    




sec=print_dir_files('/home/shuhaib/Think_python')
print(sec)
generate_checksum(sec)
