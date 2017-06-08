""" Write an add method for Points that works with either a Point object or a    tuple:"""
               

class Point(object):
  def __init__(self,x=0,y=0):
    self.x=x
    self.y=y
  def __str__(self):
    return 'the out of __str__ for x:%.2d y:%.2d'%(self.x,self.y)
  def __add__(self,other):
    new_point=Point()
    if isinstance(other,Point):
      new_point.x=self.x+other.x
      new_point.y=self.y+other.y
      return new_point
    elif type(other) == tuple:
      count=0
      for i in other:
        count += 1
        if count % 2 == 0:
          new_point.y+=self.y+i
        else:
          new_point.x+=self.x+i
      return new_point

  def __radd__(self,other):      
    return self.__add__(other) 
    
  
p3=Point(11,22)
p4=Point(2,4)
point_tuple=(6,8)
print("The addition two objects")
p1=p3+p4
print(p1)
print("After the tuple addition")
p2=p3+point_tuple
print(p2)
