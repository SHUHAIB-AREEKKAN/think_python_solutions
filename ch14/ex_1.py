import os


#def travel_dir(path):
  


def print_dir_files(dirname):
  for f in os.listdir(dirname):
    path=os.path.join(dirname,f)
    if os.path.isdir(path):
      print('D: '+os.path.abspath(f))
      print_dir_files(path)  
    else:
      print(os.path.abspath(f))
      


print_dir_files('/home/shuhaib/Think_python')
