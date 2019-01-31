from datetime import date
from datetime import time
from datetime import datetime
class ToDate:
	def __init__(self):
		self.today=date.today()
		self.cTime=datetime.now()
	def getToday(self):
		try:
			print("Today's date is",str(self.today) +", "+self.today.strftime("%A"))
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in Today exiting a code"+e.tostring())
			exit(1)
	
	def getTime(self):
		try:
			print("Current time is ",self.cTime.strftime("%X"))
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in Today exiting a code"+e.tostring())
			exit(1)
	