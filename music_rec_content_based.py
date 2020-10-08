#importing python libraries
import pandas as pd
import numpy as numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#creating a function to execute the algorithm
def get_Track_Name_from_Sno(Sno):
		return df[df.Sno == Sno]["Track_Name"].values[0]
def get_Sno_from_Track_Name(Track_Name):
		return df[df.Track_Name == Track_Name]["Sno"].values[0]
		

#loading dataset
df = pd.read_csv("Content_based.csv", encoding = 'ANSI')

#for selecting features
df = df.rename(columns = {'Track.Name' : 'Track_Name'})
df = df.rename(columns = {'Unnamed: 0' : 'Sno'})

#changing datatypes
#selecting features
features = ['Track.Name','Artist.Name','Genre']

df = df.dropna(how = 'any')

#create column for selected features
def combined_features(row):

		return row['Track_Name']+ " "+ row['Artist.Name']+ " " + row['Genre']
		print ("Error:", row)	

df['combined_features'] = df.apply(combined_features, axis=1) 

#create count matrix from this combined column

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

#print (count_matrix)
cosine_sim = cosine_similarity(count_matrix)



#song that the user likes
song_user_likes = "Panini"

song_index = get_Sno_from_Track_Name(song_user_likes)


print ("___")
#print ("song_index : "+song_index)

#establishing simalirity between the various songs
similar_songs = list(enumerate(cosine_sim[song_index]))

sorted_similar_songs = sorted(similar_songs, key=lambda x:x[1],reverse=True)

#for loop to print the songs
i=0
for Sno in sorted_similar_songs:
	print (get_Track_Name_from_Sno(Sno[0]))
	i=i+1
	if i>5:
		break  
		
