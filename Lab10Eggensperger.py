#Mariya Eggensperger 
#Lab 10 Submittal 
#CST 205-40 SpringB


#The game:
#Hangman is played by guessing letters in a word, before the number of guesses runs out
#the guesses are counted using a drawing of a hanging person
#as letters are guessed which are not a part of the word, the drawing is added to
#when the drawing is complete and the word has not been guessed, the player loses
#the player wins by guessing all the letters in the word before the guesses run out

playing = true
answer = 'irina kay'
guessesRemain = 6
display = []
guessedLetters = []
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

#setup and print initial dashes
for i in answer:
  if (i == ' '):
    display.append(' ')
  else:
    display.append('-')

printNow("*****************************")
printNow("** Let's Play...HANGMAN!!! **")
printNow("*****************************")
printNow("Here are your letters:")  
printNow("".join(display))
printNow("You have " +str(guessesRemain)+" guesses to win the game")


while (playing):
  remainingUnknown = 0
  incorrect = true
  letterGuess = requestString("Please Guess a Letter")
  if(type(letterGuess) != 'str'):
    break
  #check that guess is a letter, not more than 1, and hasn't been guessed
  if(len(letterGuess)>1):
    printNow('one character at a time please')
    continue
  elif(letters.find(letterGuess)==-1):
    printNow('that is not a letter')
    continue
  letterGuess = letterGuess.lower()
  if(letterGuess in guessedLetters):
    printNow('you have already guessed that letter')
    continue
  #step through answer and check if letters match, if so, update display
  for i in range(0,len(answer)):
    if(answer[i] == letterGuess):
      display[i] = letterGuess
      incorrect = false
    elif(display[i] == '-'):
      remainingUnknown = remainingUnknown + 1
  if(incorrect):
    guessedLetters.append(letterGuess)
    guessesRemain = guessesRemain -1
  
  if(remainingUnknown == 0):
    playing = false
    printNow('********************************')
    printNow('*** Congratulations, You Win ***')
    printNow('********************************')
    break
  elif(wrongGuesses<0):
    playing = false
    printNow('you lose')
    
  
  printNow("".join(display))
  printNow("Remaining Guesses: "+str(guessesRemain))
  printNow("Letters Guessed: " +" ".join(guessedLetters))


    
