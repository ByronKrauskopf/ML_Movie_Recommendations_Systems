#!/usr/bin/env python
# coding: utf-8

# In[29]:


# Initial imports.
import pandas as pd


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import os
import pymysql
from sklearn.cluster import KMeans 

import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
import helper
import scraping


# In[13]:


get_ipython().run_line_magic('load_ext', 'sql')


# In[14]:


hostname = "bootcamp-group-3.cn5djhczpkaa.us-east-1.rds.amazonaws.com"
database = 'Bootcamp_Group_3'


# In[15]:


connection_string = f"postgresql://root:Bootcamp_Group_3@{hostname}/{database}"


# In[16]:


get_ipython().run_line_magic('sql', '$connection_string')


# In[17]:


get_ipython().run_cell_magic('sql', '', '\nSELECT * FROM "Model_Refined_Data" LIMIT 10')


# In[18]:


#Load csv files
#Import dependencies
from sqlalchemy import create_engine
engine = create_engine(connection_string)
from sqlalchemy import inspect

insp = inspect(engine)
insp.get_table_names()


# In[19]:


df_movies = pd.read_sql('SELECT * from "Movies" ', engine)


# In[20]:


df_ratings = pd.read_sql('SELECT * from "Model_Refined_Data" ', engine)


# In[43]:


# Merge the two tables then pivot so we have Users X Movies dataframe
ratings_title = pd.merge(df_ratings, df_movies[['movieId', 'title']], on='movieId' )


# In[23]:


user_movie_ratings =  pd.pivot_table(ratings_title, index='userId', columns= 'title', values='rating')
most_rated_movies_1k = helper.get_most_rated_movies(user_movie_ratings, 1000)


# In[24]:


most_rated_movies_1k.fillna(0, inplace = True)


# In[26]:


sp_arr = csr_matrix(most_rated_movies_1k)
sdf = pd.DataFrame.sparse.from_spmatrix(sp_arr)
sparse_ratings = sdf.sparse.to_coo()


# In[30]:


# 20 clusters
predictions = KMeans(n_clusters=20, algorithm='full').fit_predict(sparse_ratings)


# In[31]:


max_users = 70
max_movies = 50

clustered = pd.concat([most_rated_movies_1k.reset_index(), pd.DataFrame({'group':predictions})], axis=1)


# In[40]:


# Pick a cluster ID from the clusters above
cluster_number = 6

# Let's filter to only see the region of the dataset with the most number of values 
n_users = 75
n_movies = 300
cluster = clustered[clustered.group == cluster_number].drop(['index', 'group'], axis=1)

cluster = helper.sort_by_rating_density(cluster, n_movies, n_users)


# In[41]:


# Fill in the name of the column/movie. e.g. 'Forrest Gump'
# Pick a movie from the table above since we're looking at a subset
movie_name = "Forrest Gump "

cluster[movie_name].mean()


# In[42]:


# Pick a user ID from the dataset
# Look at the table above outputted by the command "cluster.fillna('').head()" 
# and pick one of the user ids (the first column in the table)
user_id = 2097

# Get all this user's ratings
user_2_ratings  = cluster.loc[user_id, :]

# Which movies did they not rate? (We don't want to recommend movies they've already rated)
user_2_unrated_movies =  user_2_ratings[user_2_ratings == 0.0]

# What are the ratings of these movies the user did not rate?
avg_ratings = pd.concat([user_2_unrated_movies, cluster.mean()], axis=1, join='inner').loc[:,0]

# Let's sort by rating so the highest rated movies are presented first
avg_ratings.sort_values(ascending=False)[:20]

