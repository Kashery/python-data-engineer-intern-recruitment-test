import csv
import os
from collections import defaultdict

def hashJoin(data1, index1, data2, index2):
    h=defaultdict(list)
    for s in data1:
        h[s[index1]].append(s)
    return [(s, r) for r in data2 for s in h[r[index2]]]

with open(os.path.join(os.path.dirname(__file__), 'title.basics.tsv'),encoding='utf8') as basics, open(os.path.join(os.path.dirname(__file__), 'title.ratings.tsv'),encoding='utf8') as ratings:
    table1 = []
    table2 = []
    print("reading ratings")
    for ratings_line in ratings:
        table1.append(([ratings_line.split('\t')[1], ratings_line.split('\t')[2].strip('\n')],ratings_line.split('\t')[0]))
    print("ratings done")
    print("reading basics")
    for basics_line in basics:
        table2.append((basics_line.split('\t')[0],[basics_line.split('\t')[1],basics_line.split('\t')[2],basics_line.split('\t')[3],basics_line.split('\t')[4],basics_line.split('\t')[5],basics_line.split('\t')[6],basics_line.split('\t')[7], basics_line.split('\t')[8].strip('\n')]))
    print("basics done")   
    with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'), 'w', newline='',encoding='utf8') as result:
        writer = csv.writer(result, delimiter ='\t')
        basics.seek(0)
        ratings.seek(0)
        result_row=[]
        print("merging two datasets and writing them to 'all_videos.tsv'")
        for row in hashJoin(table1, 1, table2, 0):
            writer.writerow([row[0][1]]+row[1][1]+row[0][0])
        print("all done")
            