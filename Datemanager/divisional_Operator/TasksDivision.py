import DateManager.sub.DateAccepter
import DateManager.sub.Today

class TaskOperation(object):
    """docstring fo TaskHandling."""
    def chooseLabor(self,choosen):
        try:
            method_name='labor_'+choosen
            method=getattr(self,method_name,lambda:"***Invalid operation***")
            return method()
        except Exception as e:
            print(str(e))

    def labor_Date1(self):
        try:
            oToday=DateManager.sub.Today.ToDate()
            todate,today=oToday.getToday()
            return todate
        except Exception as e:
            print(str(e))

    def labor_Date2(self):
        try:
            oDateAccpter=DateManager.sub.DateAccepter.Accept()
            aDate=oDateAccpter.acceptDate("Please Enter date in format DD-mm-YYYY: ")
            return aDate
        except Exception as e:
            print(str(e))
			
	
