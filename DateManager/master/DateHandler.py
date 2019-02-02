import DateManager.sub.Today
import DateManager.sub.DayCalculator
class CalendarMaster:
	def operation(self):
		try:
			"""Get today's inormation"""
			oToday=DateManager.sub.Today.ToDate()
			todate,today=oToday.getToday()
			print("Today's date is : ",str(todate) +", "+today)
			totime=oToday.getTime()
			print("Current time : ", totime)

			"""Get Difference between 2 dates"""
			oDayCalculator=DateManager.sub.DayCalculator.Calculate()
			years,weeks,days=oDayCalculator.CheckAge()
			print("age of respective object/person is ",years+" years | "+weeks+" weeks | "+days+" days")
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in DateHandler exiting a code"+e)
			exit(1)
