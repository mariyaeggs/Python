#Mariya Eggenpserger 
#Lab4 Modifying pictures 
#CST 205-40 SpringB

#Warmup: function colors right side of otter.jpg pic 
 
def halfBetter(): 
  pic = makePicture(pickAFile())
  w = getWidth(pic)
  for x in range(int(w/2.0),w):
    for y in range(0,getHeight(pic)):
        px = getPixel(pic, x, y)
        setGreen(px, int(getGreen(px) * 0.25))    
  repaint(pic)
  
  
#Problem 1: Four functions that mirror cat.JPG pic

#Horizontal mirror operations function
def horizMirror(pic): 
  mirror = int(getWidth(pic)/2.0)
  for y in range(0,getHeight(pic)):
   for x in range(0,mirror):
      pright = getPixel(pic, x+mirror,y)
      pleft = getPixel(pic, mirror-x,y)
      c = getColor(pleft)
      setColor(pright,c)
  return pic
  
#Horizontal mirror execution function 
def horizExecution():
  pic = makePicture(pickAFile())
  pic = horizMirror(pic)
  repaint(pic)
  return
  
#Vertical mirror operations function
def vertMirror(pic):
  mirror = int(getHeight(pic)/2.0)
  for x in range(0, getWidth(pic)):
    for y in range(0,mirror):
      pright = getPixel(pic, x, y+mirror)
      pleft = getPixel(pic,x, mirror-y)
      c = getColor(pleft)
      setColor(pright,c)
  return pic

#Vertical mirror execution function
def vertExecution():
  pic = makePicture(pickAFile())
  pic = vertMirror(pic)
  repaint(pic)
  return
  
  
#Bottom to top mirror function
def bottomTopMirror(pic):
  pic = makePicture(pickAFile())
  mirror = int(getHeight(pic)/2.0)
  for x in range(0, getWidth(pic)):
    for y in range(mirror,2*mirror):
      px = getPixel(pic, x,2*mirror-1-y)
      setColor(px, getColor(getPixel(pic, x, y)))
  repaint(pic)
  
#Combines vertical and horizontal mirror
def combinedMirrors(pic):
  pic = makePicture(pickAFile())
  pic = horizMirror(pic)
  pic = vertMirror(pic)
  repaint(pic)
  return

#Problem 2:Copy picture

#Part 1: Simple copy of pic w/ color block
def simplePic():
  mypic = makeEmptyPicture(100, 100)
  for x in range (0, getWidth(mypic)):
    for y in range (0, getHeight(mypic)):
      setColor(getPixel(mypic, x, y), blue)
  show(mypic)
  return mypic
  

#Part 2: New pic creates copy of original cat.JPG pic  
def newSimplePic(pic):
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(100,100)
  for x in range(0,getWidth(pic)):
    for y in range(0,getHeight(pic)):
      setColor(getPixel(pic,x,y),white)
  show(pic)
  

#Problem 3: Rotates cat.JPG 90 degrees left 

def rotatePic(pic): 
  pic = makePicture(pickAFile()) 
  h = getHeight(pic)
  w = getWidth(pic)
  newPic = makeEmptyPicture(h, w)
  for x in range(1, w):
    for y in range(1, h):
      pxOrg = getPixel(pic, x, y)
      pcolor = pxOrg.getColor()
      pxNew = getPixel(newPic, h - y, w - x)
      pxNew.setColor(pcolor)
  show(newPic)
  return newPic
  
#Problem 4: Shrinks cat.JPG pic 
def shrinkPic(pic): 
  pic = makePicture(pickAFile())
  w = getWidth(pic)
  h = getHeight(pic)
  newPic = makeEmptyPicture(int(w / 2.0 + 1), int(h / 2.0 + 1))
  for x in range (0, w, 2):
    for y in range (0, h, 2):
      color = getColor(getPixel(pic, x, y))
      setColor(getPixel(newPic, int(x / 2.0), int(y / 2.0)), color)
  show(newPic)
  return newPic   