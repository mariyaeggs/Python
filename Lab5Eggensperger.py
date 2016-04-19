#Mariya Eggensperger
#Lab 5 Submission
#CST205-40 SpringB


#Rose colored image 
def roseColoredGlasses(pic1):
 pic1 = makePicture(pickAFile())
 pixels = getPixels(pic1)
 for p in pixels:
   r = getRed(p)
   setRed(p,r*5)
 repaint(pic1)
 return pic1
 
#Negative image
def makeNegative(pic2):
  pic2 = makePicture(pickAFile())
  pixels = getPixels(pic2)
  for p in pixels:
    setRed(p,255-getRed(p))
    setGreen(p,255-getGreen(p))
    setBlue(p,255-getBlue(p))
  repaint(pic2)
  return pic2 
 
#Better black and white 
def betterBnW(pic3):
  pic3 = makePicture(pickAFile())
  pixels = getPixels(pic3)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = (r + b + g)/2
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  repaint(pic3)
  return pic3

#Bottom to top mirror 
def bottomTopMirror(pic4):
  pic4 = makePicture(pickAFile())
  mirror = int(getHeight(pic4)/2.0)
  for x in range(0, getWidth(pic4)):
    for y in range(mirror,2*mirror):
      px = getPixel(pic4, x,2*mirror-1-y)
      setColor(px, getColor(getPixel(pic4, x, y)))
  repaint(pic4)
  return pic4 
  
#Shrink pic
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
  return newPic, pic

#Vertical mirror operations function
def vertMirror(pic5):
  mirror = int(getHeight(pic5)/2.0)
  for x in range(0, getWidth(pic5)):
    for y in range(0,mirror):
      pright = getPixel(pic5, x, y+mirror)
      pleft = getPixel(pic5,x, mirror-y)
      c = getColor(pleft)
      setColor(pright,c)
  return pic5

#More red 
def increaseRed(pic6):
  pic6= makePicture(pickAFile())
  for p in getPixels(pic6):
    value=getRed(p)
    setRed(p,value*2.0)
  return pic6

  
     
def increaseBlue(pic7):
  pic7 = makePicture(pickAFile())
  for p in getPixels(pic7):
    value = getBlue(p)
    setBlue(p,value*2.0)
  return pic7


def BnW(pic8):  
  pic8 = makePicture(pickAFile())
  pixels = getPixels(pic8)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avg = (r + g + b) /3 
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)  
  return(pic8)

#Collage
def collage():
   pic1 = makePicture(pickAFile())
   pic2 = makePicture(pickAFile())
   pic3 = makePicture(pickAFile())
   pic4 = makePicture(pickAFile())
   pic5 = makePicture(pickAFile())
   pic6 = makePicture(pickAFile())
   pic7 = makePicture(pickAFile())
   pic8 = makePicture(pickAFile())
   color = makeColor(255, 255, 255)
   empty = makeEmptyPicture(1100, 850, color)
   copyInto(roseColoredGlasses(pic1), empty, 1, 200 )
   color = makeColor(225, 225, 225)
   copyInto(makeNegative(pic2), empty, 1, 400)
   color = makeColor(255, 255, 255)
   copyInto(betterBnW(pic3), empty, 1, 600)
   color = makeColor(255, 255, 255)
   copyInto(bottomTopMirror(pic4), empty, 600, 1)
   color = makeColor(255, 255, 255)
   copyInto(vertMirror(pic5), empty, 400, 1)
   color = makeColor(255, 255, 255)
   copyInto(increaseRed(pic6), empty, 200, 1)
   color = makeColor(255, 255, 255)
   copyInto(increaseBlue(pic7), empty, 1, 15)
   color = makeColor(255, 255, 255)
   copyInto(BnW(pic8), empty, 200, 200)
   c = makeColor(255, 255, 255)
   s = makeStyle(sansSerif, bold, 5)
   repaint(empty)
   return

  
