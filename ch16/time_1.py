class Time(object):
  """ hour:min:sec """

time=Time()
time.hour=15
time.min=10
time.sec=23


def print_time(obj):
  print('The time is  %.2d:%.2d:%.2d'%(obj.hour,obj.min,obj.sec))



print_time(time)
