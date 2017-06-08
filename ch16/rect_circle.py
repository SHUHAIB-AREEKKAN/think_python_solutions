#! /usr/bin/python

from swampy.World import World

class Rectangle(object):
  """  """
class Build_can(object):
  """  """ 
   
def draw_rectangle(canvas,rect,name):
#  world_1=World()
  rect.name=name
  canvas.rectangle(rect.box,outline=rect.outline,width=rect.width,fill=rect.name)

def draw_point(canvas,point):
  world_1.clear()
  canvas.line()
  



rect=Rectangle()
rect.box=[[-150,-100],[150,100]]
rect.outline='black'
rect.width='2'
cnn=Build_can()
cnn.width=500
cnn.height=500
cnn.background='white'
world_1=World()
set1=world_1.ca( width=canvas.width , height=canvas.height , background=canvas.background )
#world_1.mainloop()
draw_rectangle(cnn,rect,'black')a

