import copy

def move_rectangle(rect,dx,dy):
  print("Befor x:"+str(rect.corner.x))
  print("Befor y:"+str(rect.corner.y))
  rect2=copy.deepcopy(rect)  
  rect2.corner.x+=dx
  rect2.corner.y+=dy
  
  print("corner after x:"+str(rect2.corner.x))
  print("corner after y:"+str(rect2.corner.y))

  return rect2

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

sec=move_rectangle(box,10,20)

