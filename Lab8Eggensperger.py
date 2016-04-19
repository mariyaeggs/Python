#Mariya Eggensperger 
#Lab8 Submittal 
#CST205-40 Spring2016

#Increase volume function 
#Increases sound volume
def increaseVolume(sound1): 
  #Uses rain.wav sound
  sound1 = makeSound(pickAFile())
  for sample in getSamples(sound1): 
    value = getSampleValue(sample)
    setSampleValue(sample,value*2.0)
  return sound1
  
#Decrease volume function
#Decreases sound volume 
def decreaseVolume(sound2): 
  #Uses bird.wav sound
  sound2 = makeSound(pickAFile())
  for sample in getSamples(sound2): 
    value = getSampleValue(sample)
    setSampleValue(sample,value*1.0)
  return sound2
  
#Change volume function
#Increases and decreases volume 
def changeVolume(sound1,sound2): 
  #Uses rain.wav and bird.wav sound(s)
  for sample1 in getSamples(sound1): 
    value1 = getSampleValue(sample1)
    setSampleValue(sample1,value1*0.1)
  for sample2 in getSamples(sound2): 
    value2 = getSampleValue(sample2)
    setSampleValue(sample2,value2*2.0)
  #Combined sound has a rainforest effect
  play(sound1)
  play(sound2)
  return sound1
  return sound2
  
#Max sample function
def maxSample(sound3): 
  #Uses score.wav sound 
  sound3 = makeSound(pickAFile())
  x = 0
  for sample in getSamples(sound3): 
    y = getSampleValue(sample)
    x = max(x,y)
    if y > x: 
      y = x 
  #Returns max value of 32,767
  return x 
  return sound3
  
#Sets value to maximum function
def goToEleven(sound3): 
  largest=0
  for s in getSamples(sound3):
    largest=max(largest,getSampleValue(s))
  multiplier=32767.0/largest
  print "Largest sample value in original sound was", largest
  print "Multiplier is", multiplier
  for s in getSamples(sound3):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s, louder)  
  return sound3

#Function increases and decreases score.wav
def changeVolume(sound3,sound4): 
 #Uses score.wav sound
 #Decreases volume
 for sample1 in getSamples(sound3): 
   value1 = getSampleValue(sample1)
   setSampleValue(sample1,value1*0.1)
 play(sound3)
 #Uses score.wav sound
 #Increases volume
 for sample2 in getSamples(sound4): 
   value2 = getSampleValue(sample2)
   setSampleValue(sample2,value2*6.0)
 play(sound4)
 return sound3
 return sound4


    


  
