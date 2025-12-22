# movie-recommendation
A Complete Content-Based, Rating-Based & Collaborative Filtering Model

This project implements a full movie recommendation system using the Netflix Movies Dataset.
It covers all major recommendation techniques used in real-world systems:

 Rating-Based (Weighted IMDB Score)
 
 Trending Movies (Popularity Based)
 
 Content-Based Filtering
 
 User-Based Collaborative Filtering
 
 Item-Based Collaborative Filtering
 

The notebook loads multiple datasets, cleans and merges them, builds feature vectors, calculates similarity, and generates recommendations.


1. Rating-Based Recommendation
   
Uses IMDB-style weighted rating formula:

       SCORE= V.R/(V+M)+M.C/(V+M)
Where:

V = vote count

M = minimum votes required (99th percentile)

R = average rating

C = mean average rating

Returns Top 10 highest-scored movies.


2. TRENDING MOVIES (Popularity-Based)
 
Movie popularity values are:

Converted to numeric

Cleaned & processed

Top 10 movies visualized using horizontal bar chart


3. CONTENT BASED FILTERING
   
Uses metadata:

Genres

Cast

Crew

Overview

Steps:
 Clean JSON fields using ast.literal_eval
 
 Extract top actors & directors
 
 Build a textual soup
 
 Convert using CountVectorizer (bag-of-words)
 
 Compute similarity with cosine_similarity

Function:

movies_recommendation(movie_title)

Returns 10 similar movies.


4. USER BASED COLLABORATIVE FILTERING
 
Steps:

 Create user–movie matrix

 Fill missing values
 
 Compute similarities between users
 
 Recommend movies liked by similar users but not watched by the target user
 
Function:

user_based_recommend(user_id)


5. ITEM BASED COLLABORATIVE FILTERING

Steps:

 Transpose matrix

 Compute similarity between movies

 Recommend movies similar to ones the user has rated

Function:

item_specific_recommendation(user_id)


HOW TO RUN 

Open Jupyter Notebook or VS Code

Load the .ipynb file

Update dataset paths

Run cells step-by-step

This project successfully builds a multi-level movie recommendation system using both:
Metadata-driven models (content-based)
User behavior–driven models (collaborative filtering)

It demonstrates your understanding of:

Data cleaning

Feature extraction

Natural Language Processing (NLP)

Vectorization

Similarity computation

Recommender system design



📂 DATASET (Important)

The datasets used in this project are too large to upload to GitHub, so they are NOT included in this repository.

You must manually download them before running the notebook.

Download Links

This project uses datasets from:

🔗 MovieLens Dataset

Small ratings dataset (used in this project):
https://grouplens.org/datasets/movielens/latest/

🔗 TMDB Datasets

movies_metadata.csv

credits.csv

links.csv

You can download these from:
https://www.kaggle.com/datasets/rounakbanik/the-movies-dataset
