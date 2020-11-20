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
- I prepared three separate merging scripts: `merge_tsv.py`, `merge_tsv_pandas`, `merge_tsv_low_memory_use.py`. they have few worth pointing out differences. `merge_tsv.py` performes merge using hash-join quick database join algorithm that uses dictionaries and maps to speed things up, It's memory use grows slowly but surely and may end up in memory error if script has not enough memory available. `merge_tsv_pandas` is supposed to be quicker but i have no way of checking it because i couldn't make it not throw a memory error on my PC, it just didn't work on my system but people say that pandas and dask sometimes just refuse to work in standalone scripts (work is still in progress so if you are reading it i might have decided to scrach this one and forgot to delete it from the repo). `merge_tsv_low_memory_use.py` it's slow but it gets the job done by using very little memory and not much cpu so it's most fit as a background process.
- I prefer `merge_tsv_low_memory_use.py` and sugest it as the main course, bon apetit.
- when it comes to using tsv and csv files i tend to use pandas as a solution and so i did in `merge_tsv_pandas.py`, unfortunately it runs out of memory and I am not sure if it's purely memory problem or maybe I have made some mistakes. usually i use it with smaller data sets and in jupyter notepad. I also did a version using cvs library `merge_tsv.py` but it takes an enernity to read all the records, with time it speeds up because it ignores records that were already paired.
- both data sets had some values of tconst that were unique to the file, because of the characteristics that this task presented i decided to ignore records that didn't have matching ratings and prioritise records from the `title.basics.tsv`, because of that some records from `title.ratings.tsv` can completely ignored if they don't have a matching record in `title.basics.tsv` for some reason (this should not be the case, but it is a possibility that needs be considered)
- when making `movie_rating_by_genres.tsv` and `movie_rating_by_year.tsv` i added a num column so it's easier to add records later and to see how biased the resuts can be.
- the charts use matplotlib.
- `all_videos.tsv` is incomplete in order to allow rest of the scripts work faster for the purpose of checking for mistakes but it was checked by me that even if bigger the scripts work fine (although slower of course).
```
 used libraries:
 pip install `pandas`
 pip install `dask`
 pip install `matplotlib`
```
