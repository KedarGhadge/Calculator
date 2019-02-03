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

			"""Findout age of anything"""
			oDayCalculator=DateManager.sub.DayCalculator.Calculate()
			years,weeks,days=oDayCalculator.CheckAge()
			print("age of respective object/person is ",years+" years | "+weeks+" weeks | "+days+" days")

			"""Find out difference between two days"""
			years,weeks,days=oDayCalculator.dateDifference()
			print("difference in two dates :",years+" years | "+weeks+" weeks | "+days+" days")

			"""After adding days in particular date find out the date"""
			addit=input("Enter number of days to add :")
			oDayCalculator.dateAdder(addit)

			"""After removing the days from particular date find out the date"""
			removeit=input("Enter no. of days to remove: ")
			oDayCalculator.dateSubtractor(removeit)
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in DateHandler exiting a code"+e)
			exit(1)
