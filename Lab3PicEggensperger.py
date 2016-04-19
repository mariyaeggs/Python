#Name: Mariya Eggensperger
#CST204-40 SpringB 2016
# Prof. A. Xiong

def pickAndOpenPic():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  return
def halfRed():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for p in pixels:
   r=getRed(p)
   setRed(p,r*0.5)
  repaint(pic)
  return
def noBlue():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for p in pixels:
    b =getBlue(p)
    setBlue(p, b*0.0)
  repaint(pic)
  return
def lessRed(percentLess):
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for p in pixels:
   r=getRed(p)
   setRed(p,r*percentLess)
  repaint(pic)
  return
def newRed():
  lessRed(0.1)
  return
def moreRed():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for p in pixels:
   r=getRed(p)
   setRed(p,r*50000.0)
  repaint(pic)
  return
  #red reaches max saturation at some point
  #JES is limiting the amount of red reduction
  #mitigating the issue could involve if/else loop to check the max pixel setting(s)
def experimentRed():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  pixels = getPixels(pic)
  for p in pixels:
   r=getRed(p)
   setRed(p,20)#max value of 255(?)
  repaint(pic)
  return
  #red reaches max saturation at some point
  #JES is limiting the amount of red reduction
def roseColoredGlasses():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p,r*5)
  repaint(pic)
  return
def lightenUp():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
     setColor(p,makeLighter(getColor(p)))
  repaint(pic)
  return
def makeNegative():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    setRed(p,255-getRed(p))
    setGreen(p,255-getGreen(p))
    setBlue(p,255-getBlue(p))
  repaint(pic)
  return
def BnW():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
     gr = (getRed(p)+getBlue(p)+getGreen(p))/3
     setRed(p,gr)
     setGreen(p,gr)
     setBlue(p,gr)
  repaint(pic)
  return
  #resulting image is grey, but seems a bit off perhaps brownish(?)
def betterBnW():
  filename = pickAFile()
  pic = makePicture(filename)
  pixels = getPixels(pic)
  for p in pixels:
    newGR =(getRed(p)*0.299 + getGreen(p)*0.587 + getBlue(p)*0.114)
    setRed = (p, newGR)
    setGreen = (p, newGR)
    setBlue = (p, newGR)
  repaint(pic)
  return
 
  






