import copy

def move_rectangle(rect,dx,dy):
  print("Befor x:"+str(rect.corner.x))
  print("Befor y:"+str(rect.corner.y))
  #rect2=copy.deepcopy(rect)  
  rect.corner.x+=dx
  rect.corner.y+=dy
  
  print("corner after x:"+str(rect.corner.x))
  print("corner after y:"+str(rect.corner.y))

  return rect

class Rectangle(object):
  """ width height corner """
class Point(object):
  """ x and y """
box=Rectangle()
box.width=100.0
box.height=200.0
box.corner=Point()
box.corner.x=0
box.corner.y=0

move_rectangle(box,10,20)
