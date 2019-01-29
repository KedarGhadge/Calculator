import Operator.TaskMapping
class Calc:
	#choose a operation you have to perform:
	regulator = input("Choose operation\n1. Arithmatic\n2. Date\n:=>")
	oMonitor=Operator.TaskMapping.Perform()
	output=oMonitor.operates(regulator)
	print("you selected :",output)

	