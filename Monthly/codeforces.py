import googlesheet_api_init as sheetapi
import requests
from sheet_column_indexing import *
users = []

def get_codeforces_id():
    list=[]
    for info in sheetapi.records:
        list.append(info["codeforces_id"])
    return list



def is_participated(contest, contest_id):
    for individual_contest in contest:
        if individual_contest['contestId'] == contest_id:
            return True
    return False

def get_rank(contest, contest_id):
    for individual_contest in contest:
        if individual_contest['contestId']==contest_id:
            return individual_contest['rank']

def fetch_api(participants, contest_id):
    param = ""
    for name in participants:
        param = param + ";" + name
    url = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&handles={param}&showUnofficial=true"
    response = requests.get(url)
    list_of_contestants = response.json()['result']['rows']
    list=[]
    for data in list_of_contestants:
        if data['party']['participantType'] != "CONTESTANT":
            continue
        username = data['party']['members'][0]['handle']
        rank = data['rank']
        list.append((username,rank))
    return list

def get_contest_info(contest_id):
    link = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&showUnofficial=false"
    response = requests.get(link)
    data = response.json()
    return data

def get_current_rating_list():
    current_rating_list={}
    for info in sheetapi.records:
        current_rating_list[info['codeforces_id']] = int(info['Ratings'])
    return current_rating_list

def get_current_rating_list_vjudge():
    current_rating_list={}
    print(sheetapi.records)
    for info in sheetapi.records:
        current_rating_list[info['vjudge_id']] = int(info['Ratings'])
        users.append(info['vjudge_id'])
    return current_rating_list

def find(username):
    for index, info in enumerate(sheetapi.records, start=1):
        if info['codeforces_id'] == username:
            return index + 1

def find_vjudge(username):
    for index, info in enumerate(sheetapi.records, start=1):
        if info['vjudge_id'] == username:
            return index + 1

def update_total_contest():
    contest = sheetapi.records[0]['Total Rated Contest']
    print(sheetapi.records)
    for index, _ in enumerate(sheetapi.records,start=2):
        sheetapi.workbook.worksheet('Team Formation List').update_cell(index,indexing['Total Rated Contest'],contest+1)

def get_upcoming_contest():
    link = f"https://codeforces.com/api/contest.list?"
    response = requests.get(link)
    data = response.json()
    return data