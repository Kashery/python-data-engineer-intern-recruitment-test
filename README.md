# Python Developer / Data Engineer Intern recruitment test
This is test recruitment task for intern candidate for Python Developer or Data Engineer position.

0. Fork this repository.

1. Download from https://www.imdb.com/interfaces/ files:
- `title.basics.tsv.gz`
- `title.ratings.tsv.gz`

2. Implement Python script which merges data about videos from those files using *tconst* column and save it into `all_videos.tsv` file. New file should contain columns from `title.basics.tsv.gz` and `title.ratings.tsv.gz`

3. Implement Python script which extracts from `all_videos.tsv` only these videos with *titleType* "movie" and save them into `movies.tsv` file

4. Implement Python script which calculates average rating for each *genre* save them into `movie_rating_by_genres.tsv` file

5. Repeat point 4. for average rating per *startYear* column and save them into `movie_rating_by_year.tsv` file

6. All scripts and `movie_rating_by_genres.tsv`, `movie_rating_by_year.tsv` files upload to your repository. Separate commits for points 2-5.

7. Optional - visualize on chart `movie_rating_by_genres.tsv` and `movie_rating_by_year.tsv` files using any Python library and upload script and png files to your repository.

# Few words about solutions and choices that were made
- There are two solutions for merging one called `merge_tsv_low_memory_use.py` and a jupyter notebook file called `merge_tsv_dask.ipynb` first one is slow but uses pure python the second on the other hand uses dask (as the name implies) which is waaay faster and more efficient, I imagine it's the best way to do such big data-merge but if you prefer the pure python solution, I can understand that, dask developers did most of the work for me.
- I prefer `merge_tsv_dask.ipynb` and sugest it as the main course, bon apetit.
- both data sets had some values of tconst that were unique to the file, because of the characteristics that this task presented i decided to ignore records that didn't have matching ratings and prioritise records from the `title.basics.tsv`, because of that some records from `title.ratings.tsv` can completely ignored if they don't have a matching record in `title.basics.tsv` for some reason.
- when making `movie_rating_by_genres.tsv` and `movie_rating_by_year.tsv` i added a num column so it's easier to add records later and to see how biased the resuts can be.
- the charts use matplotlib.
- `all_videos.tsv` is incomplete in order to allow rest of the scripts work faster for the purpose of checking for mistakes but it was checked by me that even if bigger the scripts work fine (although slower of course).
- warning `merge_tsv_low_memory_use.py` will be stuck for a while so prepare for 28 minutes of step by step iteration over every element in both lists (the script ignore elements if they already got a pair).
```
 used libraries:
 pip install `pandas`
 pip install `dask`
 pip install `matplotlib`
```
