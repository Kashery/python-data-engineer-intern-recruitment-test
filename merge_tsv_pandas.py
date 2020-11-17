import pandas as pd

#a = pd.read_csv("title.basics.tsv",sep='\t',dtype={'titleType':str,'primaryTitle':str,'originalTitle':str,'isAdult':int,'startYear':str,'endYear':str,'runtimeMinutes':str,'genres':str},low_memory=False,memory_map=True)
mylist=[]
for chunk in pd.read_csv("title.basics.tsv",sep='\t',low_memory=False,memory_map=True,chunksize=20000):
    mylist.append(chunk)
#b = pd.read_csv("title.ratings.tsv",sep='\t',dtype={'averageRating':int,'numVotes':int},low_memory=False,memory_map=True)
mylist2 = []
for chunk in pd.read_csv("title.ratings.tsv",sep='\t',low_memory=False,memory_map=True, chunksize=20000):
    mylist2.append(chunk)
a=pd.concat(mylist, axis= 0)
b=pd.concat(mylist2, axis= 0)
b = b.dropna(axis=1)

merged = a.merge(b, on='tconst')
merged.to_csv("all_videos.tsv", index=False,sep='\t',low_memory=False,memory_map=True)
