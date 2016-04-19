#Mariya Eggensperger 
#Lab 9 Submittal 
#CST 205-40 SpringB

#Problem 1: samples start/stop index into new sound
#Clip function
def clip(sound, start, end):
  newSound = makeEmptySound(end - start)
  newSoundIndex = 0
  for soundIndex in range(start, end):
    soundValue = getSampleValueAt(sound, soundIndex)
    setSampleValueAt(newSound, newSoundIndex, soundValue)
    newSoundIndex = newSoundIndex + 1
  return newSound
  play(newSound)

#Problem 2: copy function
#Copy function
def copy(sound, newSound, start):
  newSoundIndex = start
  for soundIndex in range(0, getLength(sound)):
    soundValue = getSampleValueAt(sound, soundIndex)
    setSampleValueAt(newSound, newSoundIndex,soundValue)
    newSoundIndex = newSoundIndex + 1
  return newSound
 
#Problem 3: merge function
#Merge function
def soundmerge(sound1,sound2,sound3,sound4,sound5):
  length = getLength(sound1) + getLength(sound2) + getLength(sound3) + getLength(sound4) + getLength(sound5)
  newsound = makeEmptySound(length)
  copy(sound1,newsound,0)
  copy(sound2,newsound,getLength(sound1))
  copy(sound3,newsound,getLength(sound1) + getLength(sound2))
  copy(sound4,newsound,getLength(sound1) + getLength(sound2) + getLength(sound3))
  copy(sound5,newsound,getLength(sound1) + getLength(sound2) + getLength(sound3) + getLength(sound4))
  play(newsound)
  return newsound


#Problem 4: reverse function
#Reverse function
def reverse(sound):
  length = getLength(sound)
  soundIndex = length-1
  newsound = makeEmptySound(length)
  for i in range(0,length):
    soundValue = getSampleValueAt(sound,soundIndex)
    setSampleValueAt(newsound,i,soundValue)
    soundIndex = soundIndex - 1
  play(newsound)
  return newsound


#Merge copy/clip functions
def merge(I,Love,Programming):
   lenI = getLength(I)
   print(lenI)
   lenLove = getLength(Love)
   print(lenLove)
   lenProgramming = getLength(Programming)
   print(lenProgramming)
   address = makeEmptySound(lenI+lenLove+lenProgramming)
   print(address)
   index = 0
   index = index +1
   #copy "I"
   for i in range(0,lenI):
     val = getSampleValue(I,i)
     print(val)
  
  