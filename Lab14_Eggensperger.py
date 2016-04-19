#Mariya Eggensperger 
#Lab 14 Submittal 
#CST 205-40 SpringB
#Adventure Game Extended with Lists

import operator

#Problem 1:

file = open('/Users/scotteggs/Downloads/eggs.txt','r')
file.seek(0)
string = file.read()

string = string.replace("\n"," ")
string = string.lower()
array = string.split(" ")

wordcount = len(array)

wordDict = {}

for word in array:
  if word in wordDict:
    wordDict[word] += 1
  else:
    wordDict[word] = 1
    
sortedArray = []
for key in wordDict:
  sortedArray.append({'word': key, 'count': wordDict[key]})
  
sortedArray.sort(lambda x,y : cmp(x['count'], y['count']))
sortedArray.reverse()

print("total word count is: " + str(len(array)))

for word in sortedArray:
  theWord = word["word"]
  theCount = word["count"]
  print(theWord + " " + str(theCount))
  

firstWord = sortedArray[0]["word"]
firstCount = sortedArray[0]["count"]
print("the most common word:")
print(firstWord + " " + str(firstCount))


#problem 2
page = open('/Users/scotteggs/Downloads/Otter Realm.htm','r')
page.seek(0)
string_page = file.read()



import codecs
page=codecs.open('/Users/scotteggs/Downloads/Otter Realm.htm','r')
pagestr = ( page.read())

page_arr = pagestr.split("<h3>")
headlines = []

for i in page_arr:
  loc = i.find("</h3>")
  if(loc>0):
    headlines.append(i[0:loc])
    printNow(i[0:loc])
  