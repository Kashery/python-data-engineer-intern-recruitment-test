import csv
import os
with open(os.path.join(os.path.dirname(__file__), 'all_videos.tsv'), 'w', newline='',encoding='utf8') as result:
    writer = csv.writer(result, delimiter ='\t')
    with open(os.path.join(os.path.dirname(__file__), 'title.basics.tsv'),encoding='utf8') as basics, open(os.path.join(os.path.dirname(__file__), 'title.ratings.tsv'),encoding='utf8') as ratings:
        list = basics.readline().split('\t')
        list[len(list)-1] = list[len(list)-1].replace('\n', '')
        list = list + ratings.readline().split('\t')
        del list[len(list)- len(ratings.readline().split('\t'))]
        list[len(list)-1] = list[len(list)-1].replace('\n', '')
        writer.writerow(list)
        
    with open(os.path.join(os.path.dirname(__file__), 'title.basics.tsv'),encoding='utf8') as basics,  open(os.path.join(os.path.dirname(__file__), 'title.ratings.tsv'),encoding='utf8') as ratings:
        skip_title = True;
        paired = []
        lines_ratings=ratings.readlines()
        for line_basics in basics:
            print(len(lines_ratings))
            for x in range(len(lines_ratings)):
                if line_basics.split('\t')[0] == lines_ratings[x].split('\t')[0] and skip_title == False and line_basics.split('\t')[0]:
                    tmp_list = line_basics.split('\t')
                    tmp_list[len(tmp_list)-1] = tmp_list[len(tmp_list)-1].replace('\n', '')
                    tmp_list = tmp_list + lines_ratings[x].split('\t')
                    del tmp_list[len(tmp_list)- len(lines_ratings[x].split('\t'))]
                    tmp_list[len(tmp_list)-1] = tmp_list[len(tmp_list)-1].replace('\n', '')
                    writer.writerow(tmp_list)
                    del lines_ratings[x]
                    break
                else:
                    skip_title = False
            
            ratings.seek(0)