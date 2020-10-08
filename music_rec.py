import pandas as pd
import numpy as numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_Track_Name_from_Sno(Sno):
    return df[df.Sno == Sno]["Track_Name"].values[0]


def get_Sno_from_Track_Name(Track_Name):
    #	print ("test 1 : "+df[df.Track_Name == Track_Name]['index'].values[0])
    return df[df.Track_Name == Track_Name]["Sno"].values[0]
    return NaN


# reading csv data set
df = pd.read_csv("top50.csv", encoding='ANSI')

# for selecting features
df = df.rename(columns={'Track.Name': 'Track_Name'})
df = df.rename(columns={'Unnamed: 0': 'Sno'})
# print (df.columns)


# changing datatypes
# df['SNo'] = df.SNo.astype(object)
# df['year'] = df.year.astype(object)
# print (df.dtypes)

# selecting features
features = ['Track.Name', 'Artist.Name', 'Genre']

# print (df.isnull().sum())
df = df.dropna(how='any')


# df.drop([df.index[1001], df.index[999979]], axis = 0, inplace=True)
# print (df.tail())


# create column for selected features
def combined_features(row):
    # try:
    return row['Track_Name'] + " " + row['Artist.Name'] + " " + row['Genre']
    # except:
    print("Error:", row)


df['combined_features'] = df.apply(combined_features, axis=1)

# print ("Combinedd features:", df["combined_features"].head())

# create count matrix from this combined column

cv = CountVectorizer()

count_matrix = cv.fit_transform(df["combined_features"])

# print (count_matrix)
cosine_sim = cosine_similarity(count_matrix)

# song that the user likes
song_user_likes = "No Me Conoce - Remix"

song_index = get_Sno_from_Track_Name(song_user_likes)

print("___")
# print ("song_index : "+song_index)


similar_songs = list(enumerate(cosine_sim[song_index]))

sorted_similar_songs = sorted(similar_songs, key=lambda x: x[1], reverse=True)

i = 0
for Sno in sorted_similar_songs:
    print(get_Track_Name_from_Sno(Sno[0]))
    i = i + 1
    if i > 1:
        break
