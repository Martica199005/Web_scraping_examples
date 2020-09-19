#Name
#Surname
#Date: 17/05/2020


import os
import requests
from bs4 import BeautifulSoup
import re
import sqlite3



# question 1
def PathFile(path):
    for dirname, dirnames, filenames in os.walk(path):
    #print path to all subdirectories first
        for subdirname in dirnames:
            print("This is a directory")
            print(os.path.join(dirname, subdirname))
        # print path to all filenames
        for filename in filenames:
            print("This is a file")
            print(os.path.join(dirname, filename))


#question2 
def get_mod(n1,n2):
    return (n1%n2)

#a%b and a mod b: what if n2 is zero in n1%n2??

#question3 
def movie_scraping():
    page= requests.get('https://www.imdb.com/chart/top')
    soup= BeautifulSoup(page.content , 'html.parser')
    listMovies=soup.find(class_='lister-list')
    #movie details
    items=listMovies.find_all(class_='titleColumn')
    #ratingColumn imdbRating
    rating=listMovies.find_all(class_='ratingColumn imdbRating')
    d={'title':'value','link':'value1','year':2020,'rating':'value3'}
    final_list=[]
    for item,note in zip(items,rating):
        movie_details=item.find('a')
        titleMovie=movie_details.get_text()
        #print(titleMovie)
        movie_Atr_title=movie_details['title']
        link_atr=movie_details['href']
        link="/"+movie_Atr_title+"/"+link_atr.split("title/")[1]
        #print(link)
        year=item.find('span').get_text()
        #print(year)
        #print(note.get_text())
        #dictionary
        d['title']=titleMovie
        d['link']=link
        d['year']=year
        d['rating']=note.get_text()
        d_copy=d.copy()
        final_list.append(d_copy)
    #sort the dictionary by year and print the details on the screen.
    sorted_list=sorted(final_list, key = lambda x: x['year'])
    for x in sorted_list:
        print("Title: "+x['title']+", year: "+x['year']+", rating: "+x['rating']+" and link: "+x['link']+"\n")


#question4

#Stands for "Model-View-Controller." MVC is an application design model comprised of three interconnected parts. 
# They include the model (data), the view (user interface), and the controller (processes that handle input).

#question 5
# with open('file.txt','r') as f: #you don't have to close the file
#     f=open('file.txt','r') # read

#     print(f.username)




#question6
with sqlite3.connect("example.db") as db:
  pass

def create_table(name):
  conn = sqlite3.connect(name)
  curs = conn.cursor()
  curs.execute('CREATE TABLE Users("id" INTEGER PRIMARY KEY AUTOINCREMENT,username text, name text, surname text)')
  conn.commit()
  conn.close()

def display_database(name):
  conn = sqlite3.connect(name)
  curs = conn.cursor()
  curs.execute('SELECT * FROM Users WHERE id=2')
  print(curs.fetchall())
  conn.close()

#question7
#gives all the rows which has a username which contains loic
def display_loic(name,var):
  conn = sqlite3.connect(name)
  curs = conn.cursor()
  curs.execute('SELECT * FROM Users WHERE username LIKE '%loic%'')
  print(curs.fetchall())
  conn.close()


    



