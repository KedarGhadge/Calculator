import DateManager.sub.Today
class CalendarMaster:
	def operation(self):
		try:
			oToday=DateManager.sub.Today.ToDate()
			oToday.getToday()
		except Exception as e:
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Exception occurred in DateHandler exiting a code"+e)
			exit(1)