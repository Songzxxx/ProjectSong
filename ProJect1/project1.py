import pandas as pd

#Load the data
songs_df = pd.read_csv("songs-of-10s.csv", index_col=0)
#print(songs_df.head())

genres_df = pd.read_csv("genres-of-10s.csv", index_col=0)
#print(genres_df.head)

merged_df = pd.merge(songs_df, genres_df, on="artist", how="left")
#print(merged_df)



#Get Familiar with the Data
1
#print(merged_df.shape[0])
2
#print(merged_df.shape[1])
#print(merged_df.dtypes)
3
#print(merged_df.isnull().sum())
4
#print(merged_df["target"].value_counts())
5
#print(merged_df["artist"].value_counts())
