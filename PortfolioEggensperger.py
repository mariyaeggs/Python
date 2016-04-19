#Mariya Eggensperger
#Image Portfolio
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
      px = getPixel(pic, x,2*mirror-1-y)
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

#snoman
def drawSnowman(pic4):
  pic4 = makePicture(pickAFile())
  addOval(pic4,60,60,60,60,white)
  addOval(pic4,60,120,80,80,white)
  addOval(pic4,60,180,100,100,white)
  repaint(pic4)
  return pic4
  
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
   empty = makeEmptyPicture(900, 900, color)
   copyInto(roseColoredGlasses(pic1), empty, 1, 200 )
   color = makeColor(225, 225, 225)
   copyInto(makeNegative(pic2), empty, 1, 400)
   color = makeColor(255, 255, 255)
   copyInto(betterBnW(pic3), empty, 1, 600)
   color = makeColor(255, 255, 255)
   copyInto(drawSnowman(pic4), empty, 600, 1)
   color = makeColor(255, 255, 255)
   copyInto(vertMirror(pic5), empty, 400, 1)
   color = makeColor(255, 255, 255)
   copyInto(pic6, empty, 200, 1)
   color = makeColor(255, 255, 255)
   copyInto(pic7, empty, 1, 15)
   color = makeColor(255, 255, 255)
   copyInto(pic8, empty, 200, 200)
   c = makeColor(255, 255, 255)
   s = makeStyle(sansSerif, bold, 5)
   #addText(empty,60, 100,"Collage Collage")
   repaint(empty)
   return

  
#Red eye reduction
def removeRedEye(pic, startX, startY, endX, endY, replacementColor):
  red = makeColor(255,0,0)
  for x in range (startX, endX):
    for y in range(startY, endY):
      currentPixel = getPixel(pic,x,y)
      if (distance(red,getColor(currentPixel)) < 165):
        setColor(currentPixel,makeColor(0,0,0))
  repaint(pic)
     
def artify(pic):
  pic = makePicture(pickAFile())
  Pixels = getPixels(pic5)
  for p in Pixels:
      r = getRed(p)
      b = getBlue(p)
      g = getGreen(p)
      if(r < 64):
          setRed(p, 31)
      elif(r>63 and r<128):
          setRed(p, 95)
      elif(r>127 and r < 192):
          setRed(p, 159)
      else:
          setRed(p, 223)
      if(g < 64):
          setGreen(p, 31)
      elif(g>63 and g<128):
          setGreen(p, 95)
      elif(g>127 and g < 192):
          setGreen(p, 159)
      else:
          setGreen(p, 223)
      if(b < 64):
          setBlue(p, 31)
      elif(b>63 and b<128):
          setBlue(p, 95)
      elif(b>127 and b < 192):
          setBlue(p, 159)
      else:
          setBlue(p, 223) 
  repaint(pic)

  
#Green screen 
def greenScreen():
  pic = makePicture(pickAFile())
  background = makePicture(pickAFile())
  Pixels = getPixels(pic)
  for p in Pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    if r < 200 and b < 100 and g > 100:
      continue
    else:
      if getX(p) < getWidth(background) and getY(p) < getHeight(background):
        setColor(getPixel(background, getX(p), getY(p)), getColor(p))
  repaint(background)            
  
def BnW():  
  pic = makePicture(pickAFile())
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    avg = (r + g + b) /3 
    setRed(p, avg)
    setGreen(p, avg)
    setBlue(p, avg)  
  return(pic)

def Line():
  pic = BnW()
  newpic = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range(0, getWidth(pic)):
    for y in range(0, getHeight(pic)):
      if(x == getWidth(pic)-1):
        right = getColor(getPixel(pic, x, y))
      else:
        right = getColor(getPixel(pic, x+1, y))
      if(y == getHeight(pic)-1):
        below = getColor(getPixel(pic, x, y))
      else:
        below = getColor(getPixel(pic, x, y+1))
      p = getColor(getPixel(pic, x, y))

      if(distance(p, right) <= 37 and distance(p, below) <= 37):
        setColor(getPixel(newpic, x, y), white)
      else:
        setColor(getPixel(newpic, x, y), black)
  repaint (newpic)
  outputFilename = pickAFolder() + "line.jpg"
  writePictureTo(newpic, outputFilename)


