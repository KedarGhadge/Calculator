from datetime import date
from datetime import time
from datetime import datetime
class ToDate:
	def __init__(self):
		self.today=date.today()
		
	def getToday(self):
		try:
			print("Today's date is",self.today)
		except Exception as e:
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Exception occurred in Today exiting a code"+e)
			exit(1)
			
	