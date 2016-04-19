#Mariya Eggensperger 
#Lab 13 Submittal 
#CST 205-40 SpringB

s1 = "_ is currently in the Guinness Book of World Records for being the most-watched * TV programme in the &."
s2 = "Thanks to the BBC's * record of shipping its ^ worldwide, it's a show that's watched by 350 million _ in some 214 &."
s3 = "As a brand there's not much |, so the news from _ that _ has secured the rights to Top Gear outside of the & is *."
s4 = "It's yet another step to make sure that its main streaming rival, _ , doesn't | itself in Pole Position with the rival show it's creating with Top Gear alumni Jeremy Clarkson, James May and _."

cs = s1 + s2 + s3 + s4

people = [] # _ 6
locations = [] # & 3
things = [] # ^  1
verbs = [] # |
adjectives = [] # *

countPeople = cs.count('_')
countLocations = cs.count('&')
countThings = cs.count('^')
countVerbs = cs.count('|')
countAdjectives = cs.count('*')

while(len(people)< countPeople):
  people.append(requestString("Please enter a person."))
  
while(len(locations) < countLocations):
  locations.append(requestString("Pleae enter a location."))
 
while(len(things)< countThings):
  things.append(requestString("Please name a thing"))

while(len(verbs)< countVerbs):
  verbs.append(requestString("Please enter a verb"))
  
while(len(adjectives)<countAdjectives):
  adjectives.append(requestString("Please enter an adjective"))

output = cs
      
while(len(people)>0):
  output = output.replace('_',people.pop(),1)
  
while(len(locations)>0):
  output = output.replace('&',locations.pop(),1)
  
while(len(things)>0):
  output = output.replace('^',things.pop(),1)
  
while(len(verbs)>0):
  output = output.replace('|',verbs.pop(),1)
  
while(len(adjectives)>0):
  output = output.replace('*',adjectives.pop(),1)

printNow(output)