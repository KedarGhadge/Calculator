import DateManager.sub.Today
import DateManager.sub.DayCalculator
class CalendarMaster:
	def operation(self):
		try:
			oToday=DateManager.sub.Today.ToDate()
			oToday.getToday()
			oToday.getTime()
			oDayCalculator=DateManager.sub.DayCalculator.Calculate()
			oDayCalculator.CheckAge()
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in DateHandler exiting a code"+e)
			exit(1)
