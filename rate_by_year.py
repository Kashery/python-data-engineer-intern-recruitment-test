import csv
import os
with open(os.path.join(os.path.dirname(__file__), 'movie_rating_by_year.tsv'), 'w', newline='',encoding='utf8') as result:
    writer = csv.writer(result, delimiter ='\t')
    writer.writerow(['year', 'averageRating', 'totalCount'])

    with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'),encoding='utf8') as videos:
        videos.readline()
        result_list = []
        for videos_line in videos:
            if videos_line.split('\t')[9]!='' and videos_line.split('\t')[10]!='' :
                found = False
                for result_element in range(len(result_list)):
                    if videos_line.split('\t')[5] == result_list[result_element][0]:
                        print(videos_line.split('\t')[5])
                        result_list[result_element][1]=(float(result_list[result_element][1]) * float(result_list[result_element][2]) + float(videos_line.split('\t')[9]))/(float(result_list[result_element][2])+1.0)
                        result_list[result_element][2] = result_list[result_element][2] + 1
                        found = True
                if not found:
                        result_list.append([videos_line.split('\t')[5], videos_line.split('\t')[9], 1])
                        found = True
        for elem in result_list:
            writer.writerow(elem)