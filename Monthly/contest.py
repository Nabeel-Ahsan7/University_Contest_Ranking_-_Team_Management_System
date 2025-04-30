import codeforces
import googlesheet_api_init as sheetapi
from sheet_column_indexing import * 
announce_contest_id = -1
def get_contest_id():
    upcoming_contest_id_list = []
    sorted_upcoming_id_list=[]
    data = codeforces.get_upcoming_contest()
    for contest in data['result']: 
        if contest['phase'] == 'BEFORE':
            upcoming_contest_id_list.insert(0,str(contest['id']))
            sorted_upcoming_id_list.append((str(contest['id']),contest['relativeTimeSeconds']))
    sorted_upcoming_id_list = sorted(sorted_upcoming_id_list, key=lambda sorted_upcoming_contest_id_list: sorted_upcoming_contest_id_list[1],reverse=True)
    global announce_contest_id
    announce_contest_id = sorted_upcoming_id_list[0][0]
    saved_upcoming_contest_list = []
    with open('upcoming_contest_id.txt', 'r') as file:
        for line in file:
            if line[-1]==' ':
                saved_upcoming_contest_list.append(line[:-1])
            else:
                saved_upcoming_contest_list.append(line[:-1])
    Contest = 0
    for x in saved_upcoming_contest_list:
        if len(saved_upcoming_contest_list)==0:
            break
        if x not in upcoming_contest_id_list:
            saved_upcoming_contest_list.remove(x)
            Contest = int(x)
    upcoming_contest_id_list += saved_upcoming_contest_list
    upcoming_contest_id_list = set(upcoming_contest_id_list)
    with open('upcoming_contest_id.txt', 'w') as file:
        for id in upcoming_contest_id_list:
            file.write(id+"\n")
    return Contest

def update_contest_name(name):
    sheetapi.workbook.worksheet('Team Formation List').update_cell(2,indexing['last_contest_name'],name)
