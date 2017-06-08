class Point(object):
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
  def print_xy(self):
    print('for x:%d and y:%d'%(self.x,self.y))
  def __str__(self):
    return 'the out of __str__ for x:%.2d y:%.2d'%(self.x,self.y)
  def __add__(self,other):
    tot1=self.x+other.x
    tot2=self.y+other.y
    return tot1,tot2

p3=Point(11,22)
p4=Point(2,4)
#p3.print_xy()
print (p3)
print(p3+p4)

