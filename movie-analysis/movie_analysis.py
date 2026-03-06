import pandas as pd

data = pd.read_csv("movies.csv")  # Open movie data

print(data.groupby("genre")["rating"].mean())  # Average rating per genre