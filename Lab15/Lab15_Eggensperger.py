#Mariya Eggensperger 
#Lab 15 Submittal 
#CST 205-40 SpringB
#Python Standard Library

import random

def rollDice(r):
  outputArr = []
  for i in range(0,r):
    num = random.randrange(1,7)
    outputArr.append(num)
  return outputArr
  


def firstTurn(dict):
  showInformation("Are you ready to roll?")
  result = rollDice(2)
  showInformation("Here's your result\n" + str(result))
  sum = result[0]+result[1]
  printNow(sum)
  if(sum in [7,11]):
    showInformation("You win")
    dict['playing'] = false
  elif(sum in [2,3,12]):
    showInformation("You lose")
    dict['playing'] = false
  elif(sum in [4,5,6,8,9,10]):
    dict['point'] = sum
  return dict
  
gameObj = {
  'point': 0,
  'playing': true
}


showInformation("Welcome to the Craps Table")
gameObj = firstTurn(gameObj)
if(gameObj['playing'] == true):
  showInformation("Your current point value is " + str(gameObj['point']))
while(gameObj['playing'] == true):
  showInformation("You roll again")
  result = rollDice(2)
  sum = result[0]+result[1]
  showInformation("Here's your result\n" + str(result))
  if(sum == gameObj['point']):
    showInformation("You Win!")
    gameObj['playing'] = false
  elif(sum == 7):
    showInformation("You Lose!")
    gameObj['playing'] = false
