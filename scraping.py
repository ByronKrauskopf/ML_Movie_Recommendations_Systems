#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''
:Instructions:
Web scrapes the image url for movie titles found in the database.


:Dependencies:
Python 3.4
splinter
bs4
webdriver_manager
pandas


:returns:
movie poster image url 
'''


# In[15]:


# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
#from config import db_password
import sqlalchemy as db 


# In[19]:


def scrap_url(imdbid):
    # Connecting to the database
    #database = f"postgresql://root:{db_password}@bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com:5432/Bootcamp_Group_3"
    #database = f"postgresql://root:Bootcamp_Group_3@bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com:5432/Bootcamp_Group_3"
    
    #Set up engine
    engine = db.create_engine(database)

    # Set execuatable path and initialize splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    # IMDB webpage constructor THIS WOULD NEED TO LOOP THROUGH THE MOVIE IDS
    url = "https://www.imdb.com/title/tt0" + str(imdbid) + "/"
    #url = 'https://www.imdb.com/title/tt0332452/'
    browser.visit(url)

    # Would need to create a funciton and loop through the movie titles wer are looking at 

    #Delay for loading the page
    browser.is_element_present_by_css('div.list_text',wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    html_soup = soup(html, 'html.parser')

    # Slide_elem = news_soup.select('div.list_text') #SAhowing nothing, need to fix. thats why nonetype error presists

    # Get image overlay URL
    image_overlay = html_soup.find('a', class_='ipc-lockup-overlay ipc-focusable')

    # Parse the text to get image overlay URL constructor and go to link
    overlay_url = 'https://www.imdb.com/'+ image_overlay.get('href')
    browser.visit(overlay_url)

    # Creating Soup
    html = browser.html
    html_soup = soup(html, 'html.parser')

    # Get image URL
    image = html_soup.find_all('img')
    test = html_soup.find('class', class_= 'sc-7c0a9e7c-0 hXPlvk')

    #Extract image Src:
    images = []
    for n in html_soup('img'):    
        if(n.get('src').startswith('https://m.media-amazon.com/images/')):
            images.append(n.get('src'))
            print(n.get('src')) #Testing, Its constantly the first image, we can have the second image possibly for somehting else.

    # First Image is poster image
    images[0]

    #Maybe create a tuple of the imasge http and the movie id
    return[images[0]]


# In[23]:


#Test Toy story
#scrap_url(114709)

