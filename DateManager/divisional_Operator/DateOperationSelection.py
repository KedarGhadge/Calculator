import DateManager.sub.DayCalculator
class Selection(object):
    def selectLabor(self,choosen):
        method_name='labor_'+str(choosen)
        method=getattr(self,method_name,lambda:"***Invalid operation***")
        return method()

    def labor_todayInfo(self):
        try:
            oToday=DateManager.sub.Today.ToDate()
            todate,today=oToday.getToday()
            print("Today's date is : ",str(todate) +", "+today)
            totime=oToday.getTime()
            print("Current time : ", totime)
        except Exception as e:
            print (str(e))

    def labor_ageDefinder(self):
        try:
            """Finding out age of anything"""
            oDayCalculator=DateManager.sub.DayCalculator.Calculate()
            years,weeks,days=oDayCalculator.CheckAge()
            print("age of respective object/person is ",years+" years | "+weeks+" weeks | "+days+" days")
        except Exception as e:
            print (str(e))

    def labor_dateDifference(self):
        try:
            """Find out the difference between 2 days"""
            oDayCalculator=DateManager.sub.DayCalculator.Calculate()
            years,weeks,days=oDayCalculator.dateDifference()
            print("difference in two dates :",years+" years | "+weeks+" weeks | "+days+" days")
        except Exception as e:
            print(str(e))

    def labor_addDateDay(self):
        try:
            """After adding days in particular date find out the date"""
            addit=input("Enter number of days to add :")
            oDayCalculator=DateManager.sub.DayCalculator.Calculate()
            oDayCalculator.dateAdder(addit)
        except Exception as e:
            print(str(e))

    def labor_removeDateDay(self):
        try:
            """After removing the days from particular date find out the date"""
            removeit=input("Enter no. of days to remove: ")
            oDayCalculator=DateManager.sub.DayCalculator.Calculate()
            oDayCalculator.dateSubtractor(removeit)
        except Exception as e:
            print(str(e))
