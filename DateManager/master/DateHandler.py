import DateManager.divisional_Operator.DateOperationSelection
class CalendarMaster:
	def operation(self):
		try:
			print("Select operation")
			print("1. Today's Information")
			print("2. Find out age of anything")
			print("3. find out difference between 2 dates")
			print("4. Add days in dates")
			print("5. Remove days from dates")
			selected=input()
			choice=self.chooseoperation(int(selected))
			taskOprator=DateManager.divisional_Operator.DateOperationSelection.Selection()
			taskOprator.selectLabor(choice)
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			#print("Exception occurred in DateHandler exiting a code"+e)
			exit(1)

	def chooseoperation(self,choice):
		try:
			switcher={
				1:'todayInfo',
				2:'ageDefinder',
				3:'dateDifference',
				4:'addDateDay',
				5:'removeDateDay'
			}
			return switcher.get(choice,"Invalid number")
			#return func
			#Tasker.taskChooser(str(func))
		except Exception as e:
			print(str(e))

	# def todayInfo(self):
		# try:
			# """Get today's inormation"""
			# oToday=DateManager.sub.Today.ToDate()
			# todate,today=oToday.getToday()
			# print("Today's date is : ",str(todate) +", "+today)
			# totime=oToday.getTime()
			# print("Current time : ", totime)
		# except Exception as e:
			# print(str(e))

	# def ageDefinder(self):
		# try:
			# """Findout age of anything"""
			# oDayCalculator=DateManager.sub.DayCalculator.Calculate()
			# years,weeks,days=oDayCalculator.CheckAge()
			# print("age of respective object/person is ",years+" years | "+weeks+" weeks | "+days+" days")
		# except Exception as e:
			# print(str(e))

	# def dateDifference(self):
		# try:
			# """Find out difference between two days"""
			# years,weeks,days=oDayCalculator.dateDifference()
			# print("difference in two dates :",years+" years | "+weeks+" weeks | "+days+" days")
		# except Exception as e:
			# print(str(e))

	# def addDateDay(self):
		# try:
			# """After adding days in particular date find out the date"""
			# addit=input("Enter number of days to add :")
			# oDayCalculator.dateAdder(addit)
		# except Exception as e:
			# print(str(e))

	# def removeDateDay(self):
		# try:
			# """After removing the days from particular date find out the date"""
			# removeit=input("Enter no. of days to remove: ")
			# oDayCalculator.dateSubtractor(removeit)
		# except Exception as e:
			# print(str(e))
