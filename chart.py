import pandas as pd
import matplotlib.pyplot as plt
import os
a= pd.read_csv(os.path.join(os.path.dirname(__file__), "movie_rating_by_year.tsv"),sep='\t',low_memory=False,memory_map=True)
a.plot.scatter(x='year', y='averageRating')
plt.savefig(os.path.join(os.path.dirname(__file__), 'movie_rating_by_year.png'))
a= pd.read_csv(os.path.join(os.path.dirname(__file__), "movie_rating_by_genres.tsv"),sep='\t',low_memory=False,memory_map=True)
a.plot.scatter(x='genre', y='averageRating').tick_params(axis='x', rotation=-70,direction= 'in')
plt.savefig(os.path.join(os.path.dirname(__file__), 'movie_rating_by_genre.png'))