import googlesheet_api_init as sheetapi
indexing = {}
for index, (key,value) in enumerate(sheetapi.records[0].items(), start=1): 
    indexing[key] = index