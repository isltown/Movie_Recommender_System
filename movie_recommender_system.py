import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)
movies = pd.read_csv('/Users/nyaldhirajlalkakadia/Desktop/Project /tmdb_5000_movies.csv')
credits = pd.read_csv('/Users/nyaldhirajlalkakadia/Desktop/Project /tmdb_5000_credits.csv')
movies = movies.merge(credits,on = "title")
print(movies)
