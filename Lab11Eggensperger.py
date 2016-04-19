#Mariya Eggensperger 
#Lab 11 Submittal 
#CST 205-40 SpringB









def setOptions(gameObject):
  if(gameObject['currentNode'] == 'New York'):
    gameObject['description'] = "The Big Apple, home to the NYSE, the UN, as well as an art, finance, fashion, design, and cutural center of the world"
    gameObject['gameOptions'] =  "Help, Exit, Travel, See the Sights, Catch a cab"
    gameObject['travelOptions'] =  "Paris, London, San Francisco"
    gameObject['sightOptions'] = "Brooklyn Bridge, Empire State Building', Mariya's Apt"
  elif(gameObject['currentNode'] == 'Paris'):
    gameObject['description'] = "The World's most romantic city." 
    gameObject['gameOptions'] =  'Help, Exit, Travel, See the Sights, Drink Some Wine'
    gameObject['travelOptions'] =  'London, Milan, NewYork'
    gameObject['sightOptions'] = "Eiffel Tower, the Louvre', Mariya's Parisian Apt"
  elif(gameObject['currentNode'] == 'London'):
    gameObject['description'] = "Center to the once worldly ubiquitous British Empire"
    gameObject['gameOptions'] =  'Help, Exit, Travel, Kiss the Queen'
    gameObject['travelOptions'] =  'Paris, New York'
  elif(gameObject['currentNode'] == 'Milan'):
    gameObject['description'] = "A fashion capital in northern Italy"
    gameObject['gameOptions'] =  'Help, Exit, Travel, Glimpse the Runway'
    gameObject['travelOptions'] =  'Paris, San Francisco'
  elif(gameObject['currentNode'] == 'San Francisco'):
    gameObject['description'] = "Street Cars, sourdough bread, and a progressive city government"
    gameObject['gameOptions'] =  'Help, Exit, Travel, Start a Tech Company'
    gameObject['travelOptions'] =  'New York, Milan'
  return gameObject


def welcomeMessage():
  printNow("***************************************")
  printNow("** Welcome to the travel adventure")
  printNow("** You'll be able to traverse the")
  printNow("** globe, at any time type help")
  printNow("** to see your options ")
  return
  

def travel(gameObject):
  printNow(" ")
  printNow("Here are your Travel Options")
  printNow(gameObject['travelOptions'])
  destination = requestString("Wher would you like to go?")
  if(destination == 'Paris'):
    gameObject['currentNode'] = 'Paris'
  elif(destination == 'London'):
    gameObject['currentNode'] = 'London'
  elif(destination == 'San Francisco'):
    gameObject['currentNode'] = 'San Francisco'
  elif(destination == 'Milan'):
    gameObject['currentNode'] = 'Milan'
  elif(destination == 'New York'):
    gameObject['currentNode'] = 'New York'
  else:
    printNow("That's not a valid destination")
    travel(gameObject)
  return gameObject
  


def takeAction(gameObject):
  printNow(" ")
  printNow(gameObject['gameOptions'])
  printNow(" ")
  playerAction = requestString("Choose an Action")
  if(playerAction == 'Exit'):
    gameObject['playing'] = false
    printNow('Goodbye')
  elif(playerAction == 'Travel'):
    gameObject = travel(gameObject)
  elif(playerAction == 'See the Sights'):
    printNow(gameObject['sightOptions'])
    sight = requestString("What would you like to see?")
    if(sight == "Mariya's Apt" or sight == "Mariya's Parisian Apt" ):
      printNow("too bad, get outta here")
  elif(playerAction == 'Help'):
    welcomeMessage()  
  return gameObject


#game setup
gameObject = {
  'playing': true,
  'currentNode': 'New York'
  }
welcomeMessage()

#game play loop
while(gameObject['playing'] == true):
  gameObject = setOptions(gameObject)
  printNow(" ")
  printNow("**************************")
  printNow(" ")
  printNow("Welcome to " + gameObject['currentNode'])
  printNow(gameObject['description'])
  printNow(" ")
  printNow("It's now your turn to play, what would you like to do?")
  takeAction(gameObject)


    
