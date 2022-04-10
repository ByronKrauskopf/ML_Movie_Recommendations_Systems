#Import dependenceies
from flask import Flask, render_template, redirect, url_for, request
import sqlalchemy as db 
import pandas as pd
#from kmeans import ml_method

#Functions
'''
:Extract_userids:

:Description:
Gets a random user id that has rated the movie from form 5 stars.

:Returns:
returns userid for ML method
'''

# Initial imports
import pandas as pd

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import os
import pymysql
from sklearn.cluster import KMeans 

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
#import helper
import scraping

def get_most_rated_movies(user_movie_ratings, max_number_of_movies):
    # 1- Count
    user_movie_ratings = user_movie_ratings.append(user_movie_ratings.count(), ignore_index=True)
    # 2- sort
    user_movie_ratings_sorted = user_movie_ratings.sort_values(len(user_movie_ratings)-1, axis=1, ascending=False)
    user_movie_ratings_sorted = user_movie_ratings_sorted.drop(user_movie_ratings_sorted.tail(1).index)
    # 3- slice
    most_rated_movies = user_movie_ratings_sorted.iloc[:, :max_number_of_movies]
    return most_rated_movies

def sort_by_rating_density(user_movie_ratings, n_movies, n_users):
    most_rated_movies = get_most_rated_movies(user_movie_ratings, n_movies)
    most_rated_movies = get_users_who_rate_the_most(most_rated_movies, n_users)
    return most_rated_movies

def ml_method(user_id):
    
    #Setting up sql connection
    hostname = "bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com"
    database = 'Bootcamp_Group_3'
    connection_string = f"postgresql://root:Bootcamp_Group_3@{hostname}/{database}"

    #Load csv files
    #Import dependencies
    from sqlalchemy import create_engine
    engine = create_engine(connection_string)
    from sqlalchemy import inspect

    insp = inspect(engine)
    insp.get_table_names()
    
    try:
        print("Getting movies....")
        df_movies = pd.read_sql('SELECT * from "Movies" ', engine)
    
        print("Getting ratings.....")
        df_ratings = pd.read_sql('SELECT * from "Model_Refined_Data" LIMIT 100000', engine)
        
        print("Sucess! Moving on...")
    except:
        print("ERROR! SQL STATEMENTS!")
    
    try:
        print("Merging!")
        # Merge the two tables then pivot so we have Users X Movies dataframe
        ratings_title = pd.merge(df_ratings, df_movies[['movieId', 'title']], on='movieId' )

        user_movie_ratings =  pd.pivot_table(ratings_title, index='userId', columns= 'title', values='rating')
        most_rated_movies_1k = get_most_rated_movies(user_movie_ratings, 1000)

        most_rated_movies_1k.fillna(0, inplace = True)

        sp_arr = csr_matrix(most_rated_movies_1k)
        sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)
        sparse_ratings = sdf.sparse.to_coo()
        print("Sucess!")
    except:
        print("Failed merging!")
        
        
    # 20 clusters
    predictions = KMeans(n_clusters=20, algorithm='full').fit_predict(sparse_ratings)
    
    max_users = 70
    max_movies = 50

    clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':predictions})], axis=1)
    
    # Pick a cluster ID from the clusters above
    cluster_number = 6

    # Let's filter to only see the region of the dataset with the most number of values 
    n_users = 75
    n_movies = 300
    
    try:
        print("Creating clusters")
        cluster = clustered[clustered.group == cluster_number].drop(['index', 'group'], axis=1)

        cluster = sort_by_rating_density(cluster, n_movies, n_users)
        print("Sucess!")
    except:
        print("Failed creating clusters!")

    # Pick a user ID from the dataset
    # Look at the table above outputted by the command "cluster.fillna('').head()" 
    # and pick one of the user ids (the first column in the table)

    try:
        print("Getting user ratings")
        # Get all this user's ratings
        user_2_ratings  = cluster.loc[user_id, :]
        print("Sucess!")
    except:
        print("ERROR WITH USER RATINGS!")

    try:
        print("Movies not rated") 
        # Which movies did they not rate? (We don't want to recommend movies they've already rated)
        user_2_unrated_movies =  user_2_ratings[user_2_ratings == 0.0]
        print("Done!")
    except:
        print("ERROR with movies not rated")
    
    # What are the ratings of these movies the user did not rate?
    avg_ratings = pd.concat([user_2_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]

    # Let's sort by rating so the highest rated movies are presented first
    avg_ratings = avg_ratings.sort_values(ascending=False)[:20]
    
    #for movie in avg_ratings
    
    print("Completed ML Method!")
    return(avg_ratings)






# #### POSSIBLE ISSUE WITH THE SQL STATEMENTS!!!!
# def extract_userids(movie_title):
#     print("Finding user_id...")
#     try:
#         #Connect to db
#         database = f"postgresql://root:Bootcamp_Group_3@bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com:5432/Bootcamp_Group_3"
#         engine = db.create_engine(database)
        
#         #SQL Statements to get movie id 
#         movie_id = pd.read_sql('SELECT movieId FROM "Movies" WHERE title = {movie_title}', engine)
#         df = pd.read_sql('SELECT * FROM "Model_Refined_Data" WHERE movieId = {movie_id}',engine)
        
#         #Get user id
#         highest_ratings = df[df["rating"] == 5]
#         user_id = highest_ratings(n=1, random_state=1111)
#         return(user_id)
#     except:
#         val = "ERROR"
#         return(val)

#Initialization of flask app
app = Flask(__name__)

#Define home page
@app.route("/")
def form(): #Home tempalte
    return render_template("index.html")

#Form to get title and send it to ML models
@app.route('/data', methods = ['GET','POST'])
def data():
    request_method = request.method
    if request.method == 'POST':
        #CMD print to check
        print('--------------')
        print(request.form)
        print('--------------')

        #Get movie title from form
        #movie_title = request.form['movie_title']
        user_id = request.form['movie_title'] #I left it the same just incase we need to change it
        try:
            result = ml_method(user_id)
            print(result)
        except:
            print("ERROR WITH ML METHOD!")

        #Get a random user_id that rated the movie 5 stars
        try:
            #user_id = extract_userids(movie_title)
            if user_id == "ERROR":
                print("User id is !ERROR!")
            else:
                print(str(user_id))
        except:
            print('--------------')
            print("!ERROR! with the extract_userids function")
            print('--------------')

        #Pass user_id to the ML methods
        #title, image_url = ```NAME OF METHOD```(user_id)

        #Return template with the values
        return render_template("index.html")

    if request.method == 'GET':
        return render_template("index.html")

#Run app
if __name__ == "__main__":
    app.run()