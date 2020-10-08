#importing libraries
import pandas as pd
import numpy as numpy
from scipy import sparse
from sklearn.metrics.pairwise import cosine_similarity

#loading the dataset
ratings = pd.read_csv("Collaborative_based.csv",encoding = 'ANSI', index_col = 0)

#print (ratings.head())
#print (ratings.columns)
#function to execute the algorithm

def standardize(row):
	new_row = (row - row.mean())/(row.max() - row.min())
	return new_row

ratings_std = ratings.apply(standardize)
#print (ratings_std)

item_similarity = cosine_similarity(ratings_std.T)
#print (item_similarity)

item_similarity_df = pd.DataFrame(item_similarity,index= ratings.columns,columns=ratings.columns)
#print (item_similarity_df)

similarity_score = pd.DataFrame()

def get_similar_songs(song_name, rating):
	simalarity_score = pd.DataFrame()
	similarity_score = item_similarity_df[song_name]*(rating-2.5)
#print (similarity_score)
	similarity_score = similarity_score.sort_values(ascending=False)
	return similarity_score

result = pd.DataFrame()
result = get_similar_songs("Lalala",5)

print(result)

print("|")
print("|")
print("|")
print("|")

#collective dataset
unsorted_popularity = pd.DataFrame()
popularity = pd.DataFrame()
unsorted_popularity = ratings.sum(axis = 0, skipna = True,)
popularity = unsorted_popularity.sort_values(ascending=False)


print("****************Popular Songs*****************")
print (popularity)


