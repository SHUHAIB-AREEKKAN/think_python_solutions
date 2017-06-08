#time to integer conversion and integer to time by methods
class Time(object):
  """ Defined for time objects and its method"""
  def time_to_int(self):
    minutes=self.hour*60+self.minute
    seconds=minutes*60 + self.second
    print('The Intgers or seconds: %d'%(seconds))  
    return seconds
  def int_to_time(self,seconds):
    minutes,self.second=divmod(seconds,60)
    self.hour,self.minute=divmod(minutes,60)
    print('Int to time :  %.2d:%.2d:%.2d' %(self.hour,self.minute,self.second)) 
    #return time
  def is_after(self,other):
    return self.time_to_int() > other.time_to_int()

start=Time()
start.hour=9
start.minute=10
start.second=20
t1=Time()
t1.hour=2
t1.minute=10
t1.second=22
sec=t1.time_to_int()
t1.int_to_time(sec)
sec1=Time.time_to_int(start)
Time.int_to_time(start,sec1)
print(t1.is_after(start))

