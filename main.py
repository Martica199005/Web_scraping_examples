import pandas as pd
import requests
from bs4 import BeautifulSoup

#Now import the link 
#simple page
#page= requests.get('https://quotesondesign.com/')
#weather page
page= requests.get('https://forecast.weather.gov/MapClick.php?lat=25.77481000000006&lon=-80.19772999999998#.XnDut6hKhPY')

#page= requests.get(' put here your link')

soup= BeautifulSoup(page.content , 'html.parser')
#for the page quote
week=soup.find(id='seven-day-forecast-body')
#print(week)

items=week.find_all(class_='tombstone-container')
#print(items[0])

#print(items[0].find(class_='period-name').get_text())
#print(items[0].find(class_='short-desc').get_text())
##print(items[0].find(class_='temp').get_text())
#print(items[1].find(class_='temp').get_text())

period_names=[item.find(class_='period-name').get_text() for item in items]
short_description=[item.find(class_='short-desc').get_text() for item in items]
temperatures=[item.find(class_='temp').get_text() for item in items]
#print(period_names)
#print(short_description)
#print(temperatures)

#here we use pandas
Weather_stuff= pd.DataFrame({'day': period_names, 'description': short_description, 'temperature': temperatures})

print(Weather_stuff)

#put the information in an csv File

Weather_stuff.to_csv('Weather_Miami.csv')




