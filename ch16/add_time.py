# adding a two given (time quantity) 
class Time(object):
  """ The class H:M:S """


def add_time(t1,t2):
  sum=Time()
  sum.hour=t1.hour+t2.hour
  sum.mint=t1.mint+t2.mint
  sum.sec=t1.sec+t2.sec
  if sum.sec>=60:
    sum.sec-=60
    sum.mint+=1
  if sum.mint>=60:
    sum.mint-=60
    sum.hour+=1
  return sum

t1=Time()
t2=Time()
t1.hour=9
t1.mint=45
t1.sec=0
t2.hour=1
t2.mint=35
t2.sec=0
s1=add_time(t1,t2)
print("h:",s1.hour)
print("m:",s1.mint)
print("s:",s1.sec)
# improved 
  
