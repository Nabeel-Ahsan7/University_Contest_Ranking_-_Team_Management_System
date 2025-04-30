import googlesheet_api_init as sheetapi
current_rank_list = []
indexing = {}
for rank, info in enumerate(sheetapi.records, start=1):
    current_rank_list.append((info['vjudge_id'],rank))