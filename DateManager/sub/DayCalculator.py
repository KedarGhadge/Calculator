from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import DateManager.sub.DateAccepter
import DateManager.sub.Today
import DateManager.divisional_Operator.TasksDivision

class Calculate(object):

    def CheckAge(self):
        try:
            oDateAccpter=DateManager.sub.DateAccepter.Accept()
            bDate=oDateAccpter.acceptDate("Please Enter B'date in format DD-mm-YYYY: ")
            now=DateManager.sub.Today.ToDate()
            oTodate,oToday=now.getToday()   #get today's date with Day
            if oTodate<bDate:
                raise Exception("Entered date must be less than today's date")
            birthDate=(oTodate-bDate).days # Subtract Today's date with entered date
            print(birthDate)
            #convert days into year,month and days
            years=int(int(birthDate)/365)
            weeks=int((int(birthDate)%365)/7)-1
            days=int(int(birthDate)%365%7)
            return str(years),str(weeks),str(days)
        except Exception as e:
            print (str(e))

    def dateDifference(self):
        try:
            oDateAccpter=DateManager.sub.DateAccepter.Accept()
            fDate=oDateAccpter.acceptDate("Enter first date(the most recent one): ")
            sDate=oDateAccpter.acceptDate("Enter second date(the least recent one): ")
            if sDate>fDate:
                raise Exception("Please ensure that 1st date is bigger than 2nd date")
            diffDate=(fDate-sDate).days #subtract 2 days
            #convert days into year,month and days
            years=int(int(diffDate)/365)
            weeks=int((int(diffDate)%365)/7)-1
            days=int(int(diffDate)%365%7)
            return str(years),str(weeks),str(days)
        except Exception as e:
                print(str(e))

    def dateAdder(self,addit):
            try:
                choose=input("1. Want to add in today's date \n2. Want to add in seprate date\n")
                operator=DateManager.divisional_Operator.TasksDivision.TaskOperation()
                gdate=operator.chooseLabor("Date"+str(choose))
                afteradded=gdate+timedelta(days=int(addit))
                print(afteradded)
            except Exception as e:
                print(str(e))
