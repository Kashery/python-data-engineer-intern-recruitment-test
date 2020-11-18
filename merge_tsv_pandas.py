import pandas as pd
initDF= pd.DataFrame()
for chunks in pd.read_csv("title.basics.tsv", sep="\t", header=0, chunksize=50000,low_memory=False,memory_map=True):
    initDF = pd.concat([initDF,chunks])
    print(chunks)
initDF.to_csv("title.basics.copy.tsv", index=False,sep='\t')
for chunks in pd.read_csv("title.ratings.tsv", sep="\t", chunksize=50000, header=0):
    print(chunks)
    initDF = initDF.merge(chunks,how='left', on='tconst').copy()
    initDF = initDF.loc[:,~initDF.columns.duplicated()]
#initDF = initDF.drop(labels='averageRating_y', axis=1)
#initDF = initDF.drop(labels='numVotes_y', axis=1)
initDF =initDF.rename(columns={'averageRating_x':'averageRating', 'numVotes_x':'numVotes'})
initDF.to_csv("all_videos.tsv", index=False,sep='\t')

#a = pd.read_csv("title.basics.tsv",sep='\t',dtype={'titleType':str,'primaryTitle':str,'originalTitle':str,'isAdult':int,'startYear':str,'endYear':str,'runtimeMinutes':str,'genres':str},low_memory=False,memory_map=True)
#mylist=[]
#for chunk in pd.read_csv("title.basics.tsv",sep='\t',chunksize=20000,low_memory=False,memory_map=True):
#    mylist.append(chunk)
#b = pd.read_csv("title.ratings.tsv",sep='\t',dtype={'averageRating':int,'numVotes':int},low_memory=False,memory_map=True)
#mylist2 = []
#for chunk in pd.read_csv("title.ratings.tsv",sep='\t', chunksize=20000,low_memory=False,memory_map=True):
#    mylist2.append(chunk)
#a=pd.concat(mylist, axis= 0)
#b=pd.concat(mylist2, axis= 0)
#b = b.dropna(axis=1)
#a = readData("title.basics.tsv")
#b = readData("title.ratings.tsv")
#merged = a.merge(b, on='tconst')
#merged.to_csv("all_videos.tsv", index=False,sep='\t')
