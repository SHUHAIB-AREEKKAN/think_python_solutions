# 1.multiply a digit with time(converted sec* anyvalue to multiply)
# 2.
class Time(object):
  """ to hold time values"""


def int_to_time(sec):
  added_time=Time()#creating new object for new time value
  mint,added_time.seconds=divmod(sec,60)  #seconds/60 and seconds%60
  added_time.hour,added_time.mint=divmod(mint,60) 
  
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

def mult_time(t,sec_to_mul):
  print("The Time before mul %d:%d:%d"%(t.hour,t.mint,t.seconds))
  conv_to_sec=time_to_int(t) * sec_to_mul  # multipication of time
  print(conv_to_sec)
  print("The after %d  seconds  multipication" %sec_to_mul)
  obj1=int_to_time(conv_to_sec)
  print("The time after multipication %d:%d:%d"%(obj1.hour,obj1.mint,obj1.seconds))

def average_pace(time,dist):
   mult_time(time,(1/dist))
  
  
  
  
  
  


t1=Time()
t1.hour=4
t1.mint=30
t1.seconds=2
sec=2

mult_time(t1,sec)
average_pace(t1,200)

