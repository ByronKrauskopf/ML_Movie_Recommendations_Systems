# ML_Movie_Recommendations_Systems
<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/ByronKrauskopf/Group_3_Final_Project/Resources/logo.png">
    <img src="https://github.com/ByronKrauskopf/Group_3_Final_Project/blob/main/Resources/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    Movie Recommendation ML Model
    <br />
    <a href="https://github.com/ByronKrauskopf/Group_3_Final_Project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://byronkrauskopf.github.io/ML_Movie_Recommendations_Systems/">View Demo</a>
    ·
    <a href="https://github.com/ByronKrauskopf/Group_3_Final_Project/issues">Report Bug</a>
    ·
    <a href="https://github.com/ByronKrauskopf/Group_3_Final_Project/issues">Request Feature</a>
  </p>
</div>

<!--################TABLE OF CONTENTS################-->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-overview">Project Overview</a>
      <ul>
        <li><a href="#project-inspirations">Project Inspirations</a></li>
        <li><a href="#data-source">Data Source</a></li>
        <li><a href="#targeted-shareholders">Targeted Shareholders</a></li>
        <li><a href="#questions-to-be-answered">Questions to be answered</a></li>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#relational-database-setup">Relational Database Setup</a></li>
        <li><a href="#erd-database-diagram">ERD Database Diagram</a></li>
        <li><a href="#etl-process">ETL Process</a></li>
      </ul>
    </li>
     <li>
      <a href="#machine-learning-models">Machine Learning Models</a></li>
      <ul>
        <li><a href="#data-preprocessing">Data Preprocessing</a></li>
        <li><a href="#1-model-based-collaborative-filtering-using-matrix-factorization">Model Based Collaborative Filtering Using Matrix Factorization</a></li>
        <li><a href="#K-Means Model">K-Means Model</a></li>
      </ul>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#communications-protocol">Communications Protocol</a></li>
    <li><a href="#Acknowledgements">Acknowledgements</a></li>
    <li><a href="#contributing">Contributing</a></li>
  </ol>
</details>

<!--################About################-->
# Project Overview
__Movie Recommendation system from MovieLens dataset__

Welcome to our final data analytics project. This project aims to tell a cohesive story using a dataset. As a small team, we will create an impressive data visualization app, that will be a cumulative display of the skills we acquired throughout the bootcamp. 
Our chosen project will be to build a movie recommendation system. With many streaming services available nowadays, building an efficient movie recommendation system has become more important due to the increase in demand to create customized content for consumers. We will be using the MovieLens dataset to build a movie recommender system. It contains approximately 1,000,209 movie ratings of 3,900 movies made by 6,040 MovieLens users.  The reason we chose this topic is because we have a large dataset to work with and we all enjoy watching movies and are looking for a recommendation on what to watch next. The main questions we want to answer with the dataset is: 

## Project Inspirations
With many streaming services available nowadays, building an efficient movie recommender system has become more important due to the increase in demand to create customized content for consumers. We will be using the MovieLens dataset to build a movie recommender system. It contains approximately __movie ratings__ of movies made by __MovieLens users__. 

## Data Source
MovieLens 25M Dataset: https://grouplens.org/datasets/movielens/25m/

## Targeted Shareholders
The potential customers of our project are mainly movie corporations, directors, and producers. We hope our target customers could use our analysis to refer to the genres that are easiest to score in marketing and take it as a reference to their future filmmaking accordingly.

## Questions to be answered
The principle question we need to address with the dataset is: __Can we accurately predict movie suggestions for users based off their previous ratings?__
 - What genres of movies score high ratings in current market?
 - What genres of movies are likely to win awards?
 - What genres of movies are likely to have a high box office?

### Built With:
- AWS
- Postgres SQL + PgAdmin
- Python 3.4
- Tableau
- HTML
- JS
- Flask
<p align="right">(<a href="#top">back to top</a>)</p>

<!--#############Getting Started################-->
# Getting Started

### Prerequisites
- installation packages and software versions

### Relational Database Setup
Using a database connected with AWS is a convenient way to store different datasets that have relationships with each other.

Additional instructions to set up a PostgreSQL database instance with Amazon Web Services (AWS) can be found in this [link](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.PostgreSQL.html).

*Initial AWS DB setup instructions:*
1. Create and sign into your AWS Management console and open the Amazon RDS Console at https://console.aws.amazon.com/rds/.
2. In the upper-right corner related to the AWS Managment Console, Choose the AWS Region where you will create the DB Instance. 
3. In the Navigation pane, choose **Databases**.
5. Choose **Create Databases.** and select the **Easy create** option.
6. On the **Create database** page, shown following, make sure that the **Standard create** option is chosen, and then choose **PostgreSQL**.
7. Under **Version**, click on the dropdown menu and select PostgreSQL 12.8-R1. This allows us to select the free tier for DB template.
9. For **Templates**, select **Free tier**.
10. Enter a name for the **DB instance identifier**.
11. For **Master username**, enter a name for the master user or leave it to the default name,
12. For **Master password**, enter a password or use an auto generated password by clicking the checkbox, **Auto generate a password**
13. Under the **Connectivity** section, click the **Additional connectivity configuration** drop down to display more options. Under **Publicly accessible** options, select **Yes**.
14. Scroll to the bottom and select **Create database** button. On the main AWS RDS dashboard, you should see your newly created database. It will take some time to be initialized and created. 

*Connecting the DB with pgAdmin:*
1. Navigate to the **Services** drop down tab and select **RDS**.
2. Under the **Resources** section, select **DB Instances** link.
3. Click the DB instance.
4. Copy the **Endpoint** under the **Connectivity & Security** section. This endpoint will be used to connect your pgAdmin to the AWS server. 
5. Navigate to pgAdmin and login.
6. Select **Add New Server** link. On the generated popup, enter a **Name** for the server name.
7. Click on the **Connection** tab and in the **Host name/address** box, paste in the copied endpoint.  
8. **Port** number should be defaulted at 5432, postgres should be the defaulted **Maintenance database** unless you choose a different username during the creation of the AWS DB.  
9. Fill out the **Password** that you used to create the AWS database. 
10. Click the blue **Save** button. You should have now successfully connected your AWS server to your pgAdmin. 

### ERD Database Diagram

![ERD](./Resources/ERD_image.png)

The schema can be viewed [here](https://github.com/ByronKrauskopf/Group_3_Final_Project/blob/main/Resources/ERD_schema.txt)

<p align="right">(<a href="#top">back to top</a>)</p>

### ETL Process

The ETL process was performed using python in jupyter notebooks. The data was then uploaded to PostgresSQL using SQlAlchemy. The code can be reviewed [here](https://github.com/ByronKrauskopf/Group_3_Final_Project/blob/main/ETL_code/ETL%20.ipynb)

Successful upload to the database was confirmed using a series of SQL queries that can be found [here](https://github.com/ByronKrauskopf/Group_3_Final_Project/blob/main/ETL_code/ETL_result_queries.sql)

The ETL process consisted of the following steps:

1) Links table cleaning
  - Load raw data file 'raw_links.csv'
  - Check for null values.
      - 107 null values were found in the tmdbId column. These are acceptable in the data as this column is not intended to be used.
  - Check data types
  - Convert tmbdId data type from float to integer in accordance with ERD.
  - Fill all Nan's in tmdbId column with "0" as placeholder
  - Export cleaned data as 'clean_links.csv' file ready for upload to database.

2) Tags table cleaning
  - Load raw data file 'raw_tags.csv'
  - Check for null values.
      - 16 null values found in tags column. These are acceptable in the data as this column is not intended to be used.
  - Check data types
  - convert timestamp column from Unix to standard format.
  - Export cleaned data as 'clean_tags.csv' file ready for upload to database.

3) Movies table cleaning
  - Load raw data file 'raw_movies.csv'
  - Use regex to separate release year from title column ito it's own year column.
  - Check for null values.
      - 410 null values found in year column. These are acceptable in the data as our primary focus is on the movie title and they constitue only a very samll porpotoin of the total data set. 
  - Check data types
  - Convert year data type from object to integer in accordance with ERD.
  - Fill all Nan's in year column with "0" as placeholder
  - Export cleaned data as 'clean_movies.csv' file ready for upload to database.

4) Ratings table cleaning
  - Load raw data file 'raw_ratings.csv'
  - Check for null values.
  - Check data types
  - Convert timestamp column from Unix to standard format.
  - Export cleaned data as 'clean_ratings.csv' file ready for upload to database.

5) Genome Scores table cleaning
  - Load raw data file 'raw_genome_scores.csv'
  - Check for null values.
  - Check data types
  - Export cleaned data as 'clean_genome_scores.csv' file ready for upload to database.

5) Genome Tags table cleaning
  - Load raw data file 'raw_genome_tags.csv' 
  - Check for null values.
  - Check data types
  - Export cleaned data as 'clean_genome_scores.csv' file ready for upload to database.

6) Load cleaned data csvs into PostgreSQL
  - create database connection string and engine
  - import cleaned csv files and chunk into groups of 100,000
  - export data to PostgreSQL 
  - initiate, run, and print timer during upload to monitor progress

7) Confirm successful upload using SQl queries
  - Query SELECT * from each table to check all columns loaded
  - Query SELECT COUNT * form each table to check that all rows loaded
  - Use ALTER TABLE for each table to drop the unneccessary index column that    uploaded with the data from python.

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################Machine Learning Models #################-->

# Machine Learning Models

### **Data Preprocessing**

In the data preprocessing phase the following steps were taken:

1) The movies and ratings tables form the database were called from the database using SQLAlchemy.
2) A left join on "movieId" was perfromed on the two tables.
3) Using groupby and count functions the number of ratings by userId was calculated.
4) Using groupby and count functions the number of ratings by movieId was calculated.
5) Any userIds that have reviewed less than 100 movies was dropped using filter.
6) Any movieIds that have less then 100 reviews was dropped using filter.
7) Resulting DataFrame contained 7 columns and 19,761,870 rows.
8) The sparcity of the DataFrame was checked and result was 0.9689 indicating that 96.89% of cells have values
9) Unneccessary columns were dropped 
10) Processed DataFrame was uploaded to PostgresSQL under table name Model_Refined_Data

The Model_Refined_Data table created by this process will be the common source loaded into both of the Machine Learning models outlined below. During the preprocessing the decision was made to exclude any userIds and movieIds that had less than 100 reviews. This was done to reduce the overall size of the dataset being used to improve its efficency. The assumption is that excluding these small values will have little to no impact on the overall accuracy of the models. 

**Code:** The code for the data preprocessing can be found [here](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/main/ETL_and_Preprocessing_code/Model_Data_Preprocessing.ipynb)  

### **1 - Model Based Collaborative Filtering Using Matrix Factorization (MF)**

**The Model:** The model is a collaborative filtering method that finds the relationship between items and users’ entities. The model learns the latent preferences of users and the latent attributes of items from known ratings to find similarity and make a recommendation. The model uses low-rank matrix factorization to derive the preferences from the dataset. Matrix factorization is the preferred model for recommender systems since it can deal with scalability and sparsity better than Memory-based collaborative filtering.  

**Why we are using it:** The model can discover hidden correlation/features in the dataset, remove redundant and noisy features, and can access easier data storage and processing. The model is known for its scalability and better handling of sparsity in matrixes. 

**The Math & Decision-making:** The matrix factorization method used for this method is the **Singular value decomposition (SVD)**. The matrix is built using user ids and movies and then SVD is used to create the best lower rank matrix that is the closest approximation to the original matrix. Once the matrix is decomposed, a function is a built to recommend movies for any user. Although movie genres are not used as a feature, the model does pick up on these underlying preferences for users based off the movies they have already rated. Once the model is trained, it can be used to predict the movie rating for a user for any movie in the database. 
Features of the model: Movie ratings

**Features of the model:** User Ids, Movie Ids. The model uses SVD to build a the best lower rank matrix of User Id x Movie Id, with ratings as the values. 

**Predicted Output:** List of recommended movies

**Splitting and Training the data set** : The dataset was split into a much smaller set due to the size of the original dataset. From there 5 splits were made to determine the accuracy of the dataset using the cross-validate function in sci-kit surprise. This gave us the results for RMSE. 

**Code:** The code for this model can be found [here](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/main/ML_code/movierecommendermatrixfactorization.py) 

### **2 - K-Means Clustering**

**The Model:**  K-means is an unsupervised learning algorithm used to identify and solve clustering issues. K represents how many clusters there will be. These clusters are then determined by the means of all the points that will belong to the cluster. The K-means algorithm groups the data into K clusters, where belonging to a cluster is based on some similarity or distance measure to a centroid.  

**Why we are using it:** There are two key differences in unsupervised learning: no paired inputs and outcomes, and the model uses a whole dataset as input. Since we are lacking of user info in our datasets, there are not enough features to set as training input using a supervised machine learning model. Besides, clustering is a good way for us to group our users and come up with a movie recommending predicition as per group movie perference. Thus we choose K-Means Clustering model to use in our project.  

**The Math & Decision-making:** K-means clustering is a method of vector quantization, originally from signal processing, that aims to partition n observations into k clusters in which each observation belongs to the cluster with the nearest mean (cluster centers or cluster centroid), serving as a prototype of the cluster. In this case, we cluster our users as per their average ratings for each movie genre. We believe the users who rated a movie a similar score, they may share a similar movie taste. Thus we group them altogether and if a user in the group has not watched a specific movie, we may use the average ratings from other users in the group to predict whether he/she would like such movie.  

**Features of the model:** Userid, movie ratings, genres.  

**Splitting and Training the data set:** Since we have more than 25 million rows in the original csv file, we combed and filtered the ratings.csv file and saved as the Model_Refined_Data.csv. We removed users who have rated less than 100 movies and also removed movies which have less than 100 ratings. We firstly use genre " Romance", "Scifi" and "ACTION" as a test to see how our K-means clustering model works. However, since we have 20 genres, scartter plot would not suitable for us to virtural the results, thus we use heatmap to show the final results. Besides, Since most users have not rated and watched most movies, we could only get a small number of cells have values. Thus, in order to present a more 'dense' region of this sparse dataset, I chose to sort the most rated movies. We peak at the top of the dataset and see what happens.  

**Predict Outcomes:** The graph filters the data to only show the most rated movies, and then sorts them by average rating. The more similar the ratings in a cluster are, the more vertical lines in similar colors you'll be able to trace in that cluster.  

 - Some clusters are more sparse than others, containing people who probably watch and rate less movies than in other clusters.
 - Some clusters are mostly yellow and bring together people who really love a certain group of movies. Other clusters are mostly green or blue meaning they contain people who agree that a certain set of movies deserves 2-3 stars.
 - The purple cells mean that the user has not watched the movie thus the rating is 0.
 - It's easy to spot horizontal lines with similar colors, these are users without a lot of variety in their ratings. A rating of four stars means different things to different people but shows the same.  
As per this logic, if we calculate the average score in this cluster for every movie, we would have an understanding for how this 'taste cluster' feels about each movie in the dataset. We could input a userid and get his/her cluster and then find out which of the movies the user hasn't watched, and provide he/she a movie recommending list as per the average ratings of other users in the cluster about such movies.  
Here is a sample result:  
![ML_KMEANS_SAMPLE_RESULT](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/a22bba16db1c0e2b23ebd60db6b68b3cecd7cb83/Resources/ML_KMEANS_SAMPLE_RESULT.png)

**Code:** The code for this model can be found [here](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/main/ML_code/notebooks/ML_K-means_Cluster.ipynb)

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################ Dashboard #################-->

# Dashboard

### Description of the tool that will be used to create the final dashboard

After the ETL process, the group will develop a data analysis using Tableau to visualize the data. We will do all the investigation and data analysis to answer all questions related to the project of movie recommendation. Initially, we will create a worksheet with several graphs and specific studies. Soon after, we will be preparing a template for our Dashboard, containing the main analyzes and graphs. Finally, we will organize the story by grouping all the results obtained and presenting the highlights and recommendations to the stakeholders.

Our Group decided to use Tableau and Dashboard to present all relationship, patterns, findings, and highlights from the data analysis process. 

The dashboard blueprint consists of eight graphs, and all elements are connected and interactive using Tableau as a tool for visualization.

### Description of interactive element(s):

* Graph 1:  Numerical overview related to the exploratory data analysis. The objective is to show an overview related to the database analyzed.
* Graph 2:  Top rated movies. The objective is to verify what is the movie (title) with the highest rating among users Top-rated.
* Graph 3: Number of movies by genre. The objective is to show the distribuition of movies by genre in quantity.
* Graph 4: Total users (Id's) per year. The objective is to show the distribution of users who evaluated the films by year.
* Graph 5:  The number of films released per year. The objective is to show the distribution of movies released by year.
* Graph 6: Number of movies rating by genre. The objective is to show the distribution of movies rating by genre.
* Graph 7: The number of ratings. Distribution of all movie ratings in quantity.

Follow below the image of our dashboard:

![](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/Douglas/Dashboard/Capture_%20Dashboard_description%20of%20interactive%20elements.PNG)

Follow below the image of our Heatmpa and movies released racing bar chart:

![](https://github.com/ByronKrauskopf/ML_Movie_Recommendations_Systems/blob/Douglas/Dashboard/Capture_%20Dashboard_Heatmap%20and%20movies%20released%20racing%20bar%20chart%20with%20interactive%20elements.PNG)

### Storyboard on Google Slide(s):

To end, we develop an Storyboard on Google Slide(s) available on following link: https://docs.google.com/presentation/d/1VwYMOzThBx8R92Co6KbsnSdxZkLTR5lw/edit?usp=sharing&ouid=110832098454737220689&rtpof=true&sd=true.

### Tableau Visualization and Storyboard

We are using Tableau as a tool for visualization and to present a storyboard to the stakeholders.

We enhance our visualization by adding some features on the Tableau, such as bar chart race and hyperlink. The bar chart race is a visualization feature to show which genres were released in animation mode. The hyperlink is a feature that creates a link clicking on the movie title and opening a new windows tab on the imdb page showing additional information related to the movie selected, such as movie image, year, and others.

Our tableau file is available on the following links below:

* Tableau Dashboard: https://public.tableau.com/app/profile/douguot/viz/MoviesRecommendations/Story1
* Tableau Heatmap: https://public.tableau.com/app/profile/douguot/viz/MoviesRecommendationsHeatmapandracingbarchart/Dashboard2?publish=yes
* Tableau Story: https://public.tableau.com/app/profile/douguot/viz/MoviesRecommendationsStory/Story1?publish=yes

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################Roadmap################-->
# Roadmap

The roadmap outlines the task's objectives, and expectations are introduced in a timetable structure utilizing an undertaking guide. Thus, the venture guide can be utilized to oversee partner assumptions and convey plans and direction assets.

Follow our roadmap below to implement our project according to the deliverables, named as segments from 1 to 4.

![](https://github.com/ByronKrauskopf/Group_3_Final_Project/blob/main/Resources/Capture2_%20Project%20Roadmap_Group3.PNG)

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################Communication Protocol################-->

# Communications Protocol

**1) General communication:**
For this project all communications will be done via Slack for messaging and Zoom for meetings. Team members should check Slack at least once per day for any critical messages. 

**2) Meetings:**
Team meetings will occur 3 times a week on Tuesdays and Thursdays during class hours, and Saturday afternoons. Additional meetings can be scheduled through Slack as needed. 

**3) Pull Requests:**
When submitting a pull request in GitHub, the user should also post a notice in Slack so that all other team members are aware of the outstanding request in GitHub and can review and approve. All pull requests will require a minimum of 3 reviews and approvals from team members before merging.

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################Acknowledgements################-->

# Acknowledgements

Data source - https://grouplens.org/datasets/movielens/

Machine Learning Article - https://towardsdatascience.com/the-4-recommendation-engines-that-can-predict-your-movie-tastes-109dc4e10c52

Code Example - https://github.com/khanhnamle1994/movielens/blob/master/SVD_Model.ipynb

<p align="right">(<a href="#top">back to top</a>)</p>

<!--################Contributors################-->

# Contributing
<div align="center">
  <a href="https://github.com/ByronKrauskopf/Group_3_Final_Project/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=ByronKrauskopf/Group_3_Final_Project" />
  </a>
</div>

- Douglas Oliveira
- Omar Zu'bi
- Jathuson Jayakumar
- Danni Yang
- Byron Krauskopf


<p align="right">(<a href="#top">back to top</a>)</p>
