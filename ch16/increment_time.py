#increment time without using loops

class Time(object):
  """ to hold time values"""


def int_to_time(sec):
  added_time=Time()#creating new object for new time value
  mint,added_time.seconds=divmod(sec,60)  #seconds/60 and seconds%60
  added_time.hour,added_time.mint=divmod(mint,60) #minute/60 for hours, minute%60 to get minutes
  return added_time



"""

seconds=4000%60
minute=((4000)/60)%60 
hours=4000/3600  



"""

def time_to_int(time):
  minutes=time.hour*60+time.mint
  seconds=minutes*60+time.seconds
  return seconds

def show(t,sec_to_add):
  print("The Time before add %d:%d:%d"%(t.hour,t.mint,t.seconds))
 # print("now we add 10 sec")
  conv_to_sec=time_to_int(t) + sec_to_add
  print("The after %d  seconds  addition" %sec_to_add)
  obj1=int_to_time(conv_to_sec)
  print("The time after add %d:%d:%d"%(obj1.hour,obj1.mint,obj1.seconds))

  
  
  
  
  
  


t1=Time()
t1.hour=4
t1.mint=30
t1.seconds=10
sec=60

show(t1,sec)
