#Mariya Eggensperger 
#CST 205-40 SpringB
#Lab6 Submittal 

#Warmup 
 
#Red eye reduction
def redEye():
  pic = makePicture(pickAFile())
  for px in getPixels(pic):
    color = getColor(px)
    if distance(color, red) < 180.0:
      setColor(px, black)
  show(pic)      
  return(pic)

 
#Better black and white 
def betterBnW(pic1):
  pic1 = makePicture(pickAFile())
  pixels = getPixels(pic1)
  for p in pixels:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    average = (r + b + g)/2
    setRed(p, average)
    setBlue(p, average)
    setGreen(p, average)
  repaint(pic1)
  return pic1
    
#Problem 1: Sepia
def sepia(pic1): 
  betterBnW(pic1)
  for p in getPixels(pic1):
    red = getRed(p)
    blue = getBlue(p)
    if (red < 63): 
      red = red * 1.1 
      blue = blue * 0.9 
    if (red > 62 and red < 192):
      red = red * 1.15
      blue = blue * 0.85
    if (red > 191): 
      red = red * 1.08
    if (red > 255): 
      red = 255
      blue = blue * 0.93
    setBlue(p,blue)
    setRed(p,red)
    show(pic1)
    return pic1

    
def artify():
  pic = makePicture(pickAFile())
  Pixels = getPixels(pic)
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

#Greeen Screen 
def chromakey(): 
  pic = makePicture(pickAFile())
  background = makePicture(pickAFile())
  px = getPixels(pic)
  for p in px:
    r = getRed(p)
    b = getBlue(p)
    g = getGreen(p)
    if r < 100 and b < 100 and g > 100:
      continue
    else:
      if getX(p) < getWidth(background) and getY(p) < getHeight(background):
        setColor(getPixel(background, getX(p), getY(p)), getColor(p))
  repaint(background) 
  
  