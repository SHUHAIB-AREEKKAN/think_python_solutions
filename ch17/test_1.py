class Time(object):
  """Represents the time of day."""
  def print_time(self):
    print ('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

start=Time()
start.hour=9
start.minute=10
start.second=20
t1=Time()
t1.hour=2
t1.minute=10
t1.second=22
Time.print_time(t1)
t1.print_time()
