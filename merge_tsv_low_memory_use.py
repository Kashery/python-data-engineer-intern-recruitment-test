import csv
import os

with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'), 'w', newline='',encoding='utf8') as result:
    writer = csv.writer(result, delimiter ='\t')
    with open(os.path.join(os.path.dirname(__file__), 'title.basics.tsv'),encoding='utf8') as basics, open(os.path.join(os.path.dirname(__file__), 'title.ratings.tsv'),encoding='utf8') as ratings:
        writer.writerow(basics.readline().strip('\n').split('\t')+ratings.readline().strip('\n').split('\t')[1:])
        line = 0
        ratings_list =[]
        for ratings_line in ratings:
            ratings_list.append(ratings_line.strip('\n').split('\t'))
        for basics_line in basics:
            line = line +1
            for ratings_line in range(len(ratings_list)):
                if basics_line.split('\t')[0] == ratings_list[ratings_line][0]:
                    writer.writerow(basics_line.strip('\n').split('\t') + ratings_list[ratings_line][1:])
                    del ratings_list[ratings_line]
                    break

            

            

