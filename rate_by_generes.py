import csv
import os
with open(os.path.join(os.path.dirname(__file__), 'movie_rating_by_genres.tsv'), 'w', newline='',encoding='utf8') as result:
    writer = csv.writer(result, delimiter ='\t')
    writer.writerow(['genre', 'averageRating', 'totalCount'])

    with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'),encoding='utf8') as videos:
        videos.readline()
        result_list = []
        for videos_line in videos:
            print(videos_line.split('\t')[8])
            for videos_genre in videos_line.split('\t')[8].split(','):
                found = False
                
                for result_element in range(len(result_list)):
                    if videos_genre == result_list[result_element][0]:
                        result_list[result_element][1]=(float(result_list[result_element][1]) * float(result_list[result_element][2]) + float(videos_line.split('\t')[9]))/(float(result_list[result_element][2])+1.0)
                        result_list[result_element][2] = result_list[result_element][2] + 1
                        found = True
                        
                if not found:
                    result_list.append([videos_genre, videos_line.split('\t')[9], 1])
                    found = True
                    
        for elem in result_list:
            writer.writerow(elem)




