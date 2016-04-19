#Mariya Eggensperger 
#Lab 12 Submittal 
#CST 205-40 SpringB








# This block sets the current game options based on where a player is
# change a player location, first set 'gameObject['currentNode'] to equal one of the options below
# then invoke this function passing in the gameObject (actully just a dictionary) as the parameter
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
    gameObject['travelOptions'] =  'Paris, New York'
    if(gameObject['foundObjects'].find("Beaded Seat Cover") > -1):
      gameObject['gameOptions'] =  'Help, Exit, Travel, Kiss the Queen, Deliver the Beads'
    else:
      gameObject['gameOptions'] =  'Help, Exit, Travel, Kiss the Queen'
  elif(gameObject['currentNode'] == 'Milan'):
    gameObject['description'] = "A fashion capital in northern Italy"
    gameObject['travelOptions'] =  'Paris, San Francisco'
    if(gameObject['foundObjects'].find("Crystal Wine Goblet") > -1):
      gameObject['gameOptions'] =  'Help, Exit, Travel, Glimpse the Runway, Gift the Goblet'
    else:
      gameObject['gameOptions'] =  'Help, Exit, Travel, Glimpse the Runway'
  elif(gameObject['currentNode'] == 'San Francisco'):
    gameObject['description'] = "Street Cars, sourdough bread, and a progressive city government"
    gameObject['gameOptions'] =  'Help, Exit, Travel, Start a Tech Company'
    gameObject['travelOptions'] =  'New York, Milan'
  elif(gameObject['currentNode'] == 'North Pole'):
    gameObject['description'] = "Ice and Santa's Workshop"
    gameObject['gameOptions'] =  'Help, Exit, Travel, Play with Toys'
    gameObject['travelOptions'] =  'New York, Milan, San Francisco, London, Paris'
  return gameObject

#welcome message...
def welcomeMessage():
  printNow("***************************************")
  printNow("** Welcome to the travel adventure")
  printNow("** You'll be able to traverse the")
  printNow("** globe, at any time type help")
  printNow("** to see your options ")
  printNow("**  ")
  printNow("**  ")
  printNow("** In each city you can fly to different cities ")
  printNow("** There are also unique experiences in each city to try ")
  printNow("** Be careful and choose wisely, these unique experiences ")
  printNow("** could win you the game, could let you discover unknown places ")
  printNow("** but they could also land you in a heap of trouble. ")
  printNow("** Choose wisely ... ")
  printNow("** ")
  printNow("**  ")
  return
  
#when a player selects travel, this brings up the travel options from the current node
#depending on the chosen destination, the gameObject node is set to that option
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
  
def secretTravel(gameObject):
  printNow(" ")
  printNow("The Queen is taken back by your advance, but she is pleased")
  printNow("She opens a key and walks to a secret wardrobe, it's is cold")
  printNow("Stepping into the wardrobe, you're suddently transported to another land")
  printNow(" ")
  gameObject['currentNode'] = 'North Pole'
  return gameObject
  
  

#function used to take actions in the game
def takeAction(gameObject):
  printNow(" ")
  printNow(gameObject['gameOptions'])
  printNow(" ")
  playerAction = requestString("Choose an Action")
  if(playerAction == 'Exit'):
    #setting this property to false will end the while loop
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
  elif(playerAction == 'Kiss the Queen' and gameObject['currentNode'] == 'London'):
    gameObject = secretTravel(gameObject)
  #the next two if conditions uncover hidden objects and add them to the hidden objects property
  elif(playerAction == 'Catch a cab' and gameObject['currentNode'] == 'New York'):
    printNow(" ")
    printNow("While riding in your cab, you've found a secret item")
    printNow("Take this object, The Beaded Seat Cover, to London to be used in the famous Black Taxis")
    gameObject['foundObjects'] = gameObject['foundObjects'] + "Beaded Seat Cover, "
  elif(playerAction == "Drink Some Wine" and gameObject['currentNode'] == 'Paris'):
    printNow(" ")
    printNow("While sampling some fine wines, you've uncovered a secret item!")
    printNow("Take this object, The Crystal Wine Goblet, to Milan to be given to a famous fashion designer")
    gameObject['foundObjects'] = gameObject['foundObjects'] + "Crystal Wine Goblet, "
  #the next two options are only shown to the player if the object has been found and add 1 point each to the victory condition
  elif(playerAction == 'Deliver the Beads' and gameObject['currentNode'] == 'London'):
    printNow(" ")
    printNow("Congratulations, you've delivered the Beaded Seat Cover")
    printNow("A revolution in taxi cab comfort will soon begin!")
    printNow(" ")
    gameObject['victoryPoints'] = gameObject['victoryPoints'] + 1
  elif(playerAction == 'Gift the Goblet' and gameObject['currentNode'] == 'Milan'):
    printNow(" ")
    printNow("Congratulations, you've delivered the Wine Goblet")
    printNow("The designer enjoyed your gift so much, she is designing a clothing line in your image!")
    printNow(" ")
    gameObject['victoryPoints'] = gameObject['victoryPoints'] + 1
  #lose condition
  elif(playerAction == 'Start a Tech Company' and gameObject['currentNode'] == 'San Francisco'):
    printNow(" ")
    printNow("Oooooh, ouch. You were gaining traction in the market but tried to go to big too soon")
    printNow("Your investors went looking for other opportunities and pulled out.")
    printNow(" ")
    printNow("************************************")
    printNow(" ")
    printNow("You've lost the game")
    printNow(" ")
    printNow("************************************")
    gameObject['playing'] = false
  #win condition
  if(gameObject['victoryPoints'] > 1):
    gameObject['playing'] = false
    printNow("************************************")
    printNow(" ")
    printNow("Congratulations, You've won the Game")
    printNow(" ")
    printNow("************************************")
  return gameObject


#game setup, starting place is new york
gameObject = {
  'playing': true,
  'currentNode': 'New York',
  'foundObjects': '',
  'victoryPoints': 0
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
  printNow("Here are your stats:")
  printNow("Found Items: " + gameObject['foundObjects'])
  printNow("Victory Points: " + str(gameObject['victoryPoints']))
  printNow("It's now your turn to play, what would you like to do?")
  takeAction(gameObject)


    
