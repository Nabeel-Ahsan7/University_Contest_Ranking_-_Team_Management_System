import time
import googlesheet_api_init as sheetapi
from current_rank_list import *
from sheet_column_indexing import *
import codeforces as cf
import elo_rating as elo
import contest
import ranklist_announcement as ranking
import os
contest_id = 10
contest_name = "JKKNIU Monthly Contest - " + str(contest_id)
contest.update_contest_name(contest_name)
def get_ranklist():
    list = []
    print(os.path.exists('F:\Ranking System\Monthly\monthly_rank_list.txt'))
    with open('F:\Ranking System\Monthly\monthly_rank_list.txt', 'r') as file:
        cnt = 1
        for line in file:
            name = line[:-1]
            list.append([name,cnt])
            cnt+=1
    print(list)
    return list

current_rating_list = cf.get_current_rating_list_vjudge()
sorted_rank_list = get_ranklist()
count = 1   
for name, rank in sorted_rank_list: 
    if name in current_rating_list:
        elo.add_coder(name, count, current_rating_list[name])
        count += 1
elo.calculate_new_rating()
# print(elo.coders)
# running_contest = sheetapi.records[0]['Total Rated Contest']+1
# print(running_contest)

# for name in cf.users:  
#     cell_index = cf.find_vjudge(name)
#     sheetapi.targetSheet.update_cell(cell_index, indexing['Total Rated Contest'],running_contest)
#     time.sleep(3)

for coder in elo.coders:  
    name = coder['name']
    new_rating = coder['post_rating']
    rating_change = coder['rating_change']
    cell_index = cf.find_vjudge(name)
    total_contest_participation = sheetapi.records[cell_index - 2]['Number of Participated Contest']
    sheetapi.targetSheet.update_cell(cell_index, indexing['Ratings'], new_rating)
    # sheetapi.targetSheet.update_cell(cell_index, indexing['Total Rated Contest'],running_contest)
    sheetapi.targetSheet.update_cell(cell_index, indexing['Number of Participated Contest'], int(total_contest_participation) + 1)
    sheetapi.targetSheet.update_cell(cell_index, indexing['Last Rating Change'], rating_change)
    print(f'{name} rank is updated. Cell Index = {cell_index}')
    time.sleep(3)

sheetapi.targetSheet.sort((indexing['Ratings'], 'des'))
time.sleep(15)
rank_message = ranking.make_rank(contest_name,contest_id,sorted_rank_list)
cf.update_total_contest()