#Mariya Eggensperger 
#Lab 16 Submittal 
#CST 205-40 SpringB
#URLs and HTML



import urllib

def makePage(html):
  file = open("/Users/mariyawilson/Desktop/superduperweb.html", "wt")
  file.write(html)
  file.close()
  return
  

url = "https://www.python.org/"
page = urllib.urlopen(url)
htmlSource = page.read()
page.close()

titleStart = htmlSource.find("<title>")
titleEnd = htmlSource.find("</title>")


pageTitle = htmlSource[titleStart+7:titleEnd]
headlinesArr = []
aboutMenuArr = []
downloadsMenuArr = []
documentationArr = []

newsStart = htmlSource.find("</span>Latest News</h2>")
newsStr = htmlSource[newsStart:]
newsEnd = newsStr.find("</ul>")
newsStr = newsStr[:newsEnd]

newsArr = newsStr.split("</a></li>")
for i in newsArr:
  position = (i[::-1].find(">"))
  headlinesArr.append((i[len(i)-position:]))
  
aboutStart = htmlSource.find('<a href="/about/" title="" class="">About</a>')
aboutStr = htmlSource[aboutStart:]
aboutEnd = aboutStr.find("</ul>")
aboutStr = aboutStr[:aboutEnd]

aboutArr = aboutStr.split("</a></li>")
for i in aboutArr:
  position = (i[::-1].find(">"))
  aboutMenuArr.append((i[len(i)-position:]))
  
newsStart = htmlSource.find('<a href="/downloads/" title="" class="">Downloads</a>')
newsStr = htmlSource[newsStart:]
newsEnd = newsStr.find("</ul>")
newsStr = newsStr[:newsEnd]

newsArr = newsStr.split("</a></li>")
for i in newsArr:
  position = (i[::-1].find(">"))
  downloadsMenuArr.append((i[len(i)-position:]))
  
newsStart = htmlSource.find('<a href="/doc/" title="" class="">Documentation</a>')
newsStr = htmlSource[newsStart:]
newsEnd = newsStr.find("</ul>")
newsStr = newsStr[:newsEnd]

newsArr = newsStr.split("</a></li>")
for i in newsArr:
  position = (i[::-1].find(">"))
  documentationArr.append((i[len(i)-position:]))



printNow("Page Title")
printNow(pageTitle)
printNow("")
printNow("Headlines")
printNow(headlinesArr)
printNow("")
printNow("About Menu")
printNow(aboutMenuArr)
printNow("")
printNow("Download Menu")
printNow(downloadsMenuArr)
printNow("")
printNow("Documentation")
printNow(documentationArr)
