from datetime import datetime
#b1 young b2 old
def double_day(b1,b2):
  assert b1>b2
  delta=b1-b2
  double_day=b1+delta
  return double_day

b1=datetime(1999,3,13)
b2=datetime(1994,5,1)
print (double_day(b1,b2))





