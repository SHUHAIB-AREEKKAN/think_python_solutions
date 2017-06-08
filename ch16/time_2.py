# 16.2 is_after() argument one is less than arg2 (in terms of time)

class Time(object):
  """ The attributes time h:m:s"""

def is_after(obj1,obj2):
  ts1=convert_to_sec(obj1)
  ts2=convert_to_sec(obj2)
  return ts2>ts1
def convert_to_sec(obj):
  hour=obj.h*3600
  mint=obj.m*60
  return(hour+mint+obj.s)




t1=Time()
t1.h=4
t1.m=50
t1.s=11
t2=Time()
t2.h=5
t2.m=50
t2.s=11

print(is_after(t1,t2))
