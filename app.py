#Import dependenceies
from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import os
import pymysql
import numpy as np
import numpy as np
from scipy.sparse.linalg import svds
import sqlite3 
from sqlalchemy import create_engine
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import sqlalchemy as db
from splinter import Browser

#Web scrap Function
def scrap_url(imdbid):

    # Set execuatable path and initialize splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    
    #First try with 0 infront of title
    try:
        # IMDB webpage constructor THIS WOULD NEED TO LOOP THROUGH THE MOVIE IDS
        url = "https://www.imdb.com/title/tt0" + str(imdbid) + "/"
        browser.visit(url)

        #Delay for loading the page
        browser.is_element_present_by_css('div.list_text',wait_time=1)

        # Convert the browser html to a soup object and then quit the browser
        html = browser.html
        html_soup = soup(html, 'html.parser')

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
                print(n.get('src')) 

        # First Image is poster image
        images[0]
        
    #Else try without the zero
    except:
        # IMDB webpage constructor THIS WOULD NEED TO LOOP THROUGH THE MOVIE IDS
        url = "https://www.imdb.com/title/tt" + str(imdbid) + "/"
        browser.visit(url)

        #Delay for loading the page
        browser.is_element_present_by_css('div.list_text',wait_time=1)

        # Convert the browser html to a soup object and then quit the browser
        html = browser.html
        html_soup = soup(html, 'html.parser')

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
                print(n.get('src')) 

        # First Image is poster image
        images[0]
    # Return first image
    return[images[0]]


#Recommend_movies function
def recommend_movies(predictions, userID, movies, original_ratings, num_recommendations):
        
        # Get and sort the user's predictions
        user_row_number = userID 
        sorted_user_predictions = predictions.iloc[user_row_number].sort_values(ascending=False) # User ID starts at 1
        
        # Get the user's data and merge in the movie information.
        user_data = original_ratings[original_ratings.userId == (userID)]
        user_full = (user_data.merge(movies, how = 'left', left_on = 'movieId', right_on = 'movieId').
                        sort_values(['rating'], ascending=False)
                    )

        print ('User {0} has already rated {1} movies.'.format(userID, user_full.shape[0]))
        print ('Recommending highest {0} predicted ratings movies not already rated.'.format(num_recommendations))
        
        # Recommend the highest predicted rating movies that the user hasn't seen yet.
        recommendations = (movies[~movies['movieId'].isin(user_full['movieId'])].
            merge(pd.DataFrame(sorted_user_predictions).reset_index(), how = 'left',
                left_on = 'movieId',
                right_on = 'movieId').
            rename(columns = {user_row_number: 'Predictions'}).
            sort_values('Predictions', ascending = False).
                        iloc[:num_recommendations, :-1]
                        )

        return recommendations

#MovieRec Function
def MovieRec(): 
    hostname = "bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com"
    database = 'Bootcamp_Group_3'
    connection_string = f"postgresql://root:Bootcamp_Group_3@{hostname}/{database}"
    engine = create_engine(connection_string)
    print("Getting movies....")
    movies = pd.read_sql('SELECT * from "Movies" ', engine)

    print("Getting ratings.....")
    df_ratings = pd.read_sql('SELECT * from "Model_Refined_Data" ', engine)
    
    print("Sucess! Moving on...")

    #Setup users and movie datasets and count the unique rows
    n_users = df_ratings.userId.unique().shape[0]
    n_movies = df_ratings.movieId.unique().shape[0]
    print ('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_movies))

    # Create ratings matrix, each row is a unique user and each column is a movie
    Ratings = df_ratings.pivot(index = 'userId', columns ='movieId', values = 'rating').fillna(0)
    print("Successfully user/movie matrix")

    R = Ratings.to_numpy()
    user_ratings_mean = np.mean(R, axis = 1)
    Ratings_demeaned = R - user_ratings_mean.reshape(-1, 1)

    # Checking the sparsity of the dataset
    sparsity = round(1.0 - len(df_ratings) / float(n_users * n_movies), 3)
    print ('The sparsity level of MovieLens1M dataset is ' +  str(sparsity * 100) + '%')

    # SVD set up
    U, sigma, Vt = svds(Ratings_demeaned, k = 2)
    print(U, sigma)

    # matrix form of the diagonal
    sigma = np.diag(sigma)
    print(sigma)

    all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
    print(all_user_predicted_ratings)

    preds = pd.DataFrame(all_user_predicted_ratings, columns = Ratings.columns)
    print(preds)

    return preds, movies, df_ratings

##########################
##########################
##########################
##########################


#Initialization of flask app
app = Flask(__name__)

#Define home page
@app.route("/")
def form(): #Home tempalte
    return render_template("index.html")

#Form to get title and send it to ML models
@app.route('/data', methods = ['GET','POST'])
def data():
    if request.method == 'POST':

        #CMD print to check
        print('--------------')
        print(request.form)
        print('--------------')

        #Get user_id from form
        user_id = request.form['user_ids'] #I left it the same just incase we need to change it
        
        print('--------------')
        print(user_id)
        print('--------------')

        #Generate predictions
        preds, movies, df_ratings = MovieRec()
        predictions = recommend_movies(preds, int(user_id), movies, df_ratings, 5)
        
        print('--------------')
        print(predictions)
        print('--------------')
        
        #Create a list of the movie ids
        list = []
        hostname = "bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com"
        database = 'Bootcamp_Group_3'
        connection_string = f"postgresql://root:Bootcamp_Group_3@{hostname}/{database}"
        engine = create_engine(connection_string)

        #Get movie id IMDB links
        for movie_id in predictions['movieId']:
            query = 'SELECT "imdbId" FROM "Links" WHERE "movieId" = %s' % movie_id # x inside single quotes
            temp = pd.read_sql(query, engine)
            list.append(temp['imdbId'][0])
        print(list)

        #Get images of the movie posters
        link_list = []
        for imdbid in list:
            temp = scrap_url(imdbid)[0]
            link_list.append(temp)
        print(link_list)

        #Return template with the values
        return render_template("result.html", movie_names = predictions['title'], movie_images = link_list)

    if request.method == 'GET':
        return render_template("result.html")

#Run app
if __name__ == "__main__":
    app.run()