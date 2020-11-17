import csv
import os
with open(os.path.join(os.path.dirname(__file__), 'movies.tsv'), 'w', newline='',encoding='utf8') as result:
    writer = csv.writer(result, delimiter ='\t')
    with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'),encoding='utf8') as videos:
        movie_list = videos.readline().split('\t')
        movie_list[len(movie_list)-1] = movie_list[len(movie_list)-1].replace('\n', '')
        writer.writerow(movie_list)
        print(movie_list)
        
        
        for line_videos in videos:
            if line_videos.split('\t')[1] == 'movie':
                movie_list=line_videos.split('\t')
                movie_list[len(movie_list)-1] = movie_list[len(movie_list)-1].replace('\n', '')
                writer.writerow(movie_list)
