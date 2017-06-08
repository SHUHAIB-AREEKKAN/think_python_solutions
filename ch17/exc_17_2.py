"""Write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes."""

class Point(object):
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
  def print_xy(self):
    print('for x:%d and y:%d'%(self.x,self.y))

p1=Point()
p1.print_xy()
p2=Point(10)
p2.print_xy()
p3=Point(11,22)
p3.print_xy()

