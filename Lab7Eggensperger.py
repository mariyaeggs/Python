#Mariya Eggensperger
#CST205-40 SpringB
#Lab 7: St. Patrick's Card


#Warmup: Draw a snowman

#Warmup: draws snowman on pic
def drawSnowman():
  pic = makePicture(pickAFile())
  addOval(pic,60,60,60,60,white)
  addOval(pic,60,120,80,80,white)
  addOval(pic,60,180,100,100,white)
  repaint(pic)
  return pic


def stPatrickCard():
   pic1 = makePicture(pickAFile())
   pic2 = makePicture(pickAFile())
   pic3 = makePicture(pickAFile())
   color = makeColor(255, 255, 255)
   empty = makeEmptyPicture(400, 400, color)
   copyInto(pic1, empty, 0, 40)
   color = makeColor(225, 225, 225)
   copyInto(pic2, empty, 1, 100)
   color = makeColor(255, 255, 255)
   copyInto(pic3, empty, 1, 225)
   c = makeColor(255, 255, 255)
   s = makeStyle(sansSerif, bold, 5)
   addText(empty,60, 100,"Happy St. Pattys!")
   repaint(empty)
   return

  


  
