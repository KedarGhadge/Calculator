from datetime import date
from datetime import time
from datetime import datetime
class ToDate:
	def getToday(self):
		try:
			today=date.today()
			print("Today's date is",today)
		except Exception as e:
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Exception occurred in Today exiting a code"+e)
			exit(1)