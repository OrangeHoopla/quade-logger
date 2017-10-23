import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('shen.json',scope)
client = gspread.authorize(creds)

sheet = client.open('The Goods').sheet1
rich = sheet.get_all_records()
print(rich)

sheet.update_cell(4,1,"test")
