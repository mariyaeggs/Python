#Mariya Eggensperger 
#Lab 15 Submittal 
#CST 205-40 SpringB
#Python Standard Library

import calendar
import datetime
from datetime import timedelta



showInformation("Tell me about your birthday")
yy = int(requestString("Enter year (YYYY): "))
mm = int(requestString("Enter month (MM): "))
dd = int(requestString("Enter day (DD): "))

printNow("Here's a calendar from the month you were born")
printNow(calendar.month(yy,mm))

today = datetime.date.today()
birthday = datetime.date(yy,mm,dd)
thisYearBirthday = datetime.date(today.year, birthday.month, birthday.day)
nextYearBirthday = datetime.date(today.year + 1, birthday.month, birthday.day)

if(thisYearBirthday>today):
  daysUntil = thisYearBirthday - today
elif(thisYearBirthday<today):
  daysUntil = nextYearBirthday - today
else:
  printNow("Happy Birthday!")

if(daysUntil):
  printNow("It's only " + str(daysUntil) + " until your birthday")

printNow("")


independenceDay = datetime.date(1776,7,4)
independenceDay.weekday()

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

printNow("The declaration of independence was ratified on a " + weekdays[independenceDay.weekday()])