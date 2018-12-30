import Addition
import Subtraction
import AcceptNumber
class Calc:
	s=AcceptNumber.Accept()
	num1=s.acceptNumber("Enter first number")
	num2=s.acceptNumber("Enter 2nd number")
	# print(num1,num2)
	d = Addition.Addition(num1,num2)
	sum=d.allSum()
	print("addition of two numbers",sum)
	
	#Subtraction
	oSubtract=Subtraction.Subtract(num1,num2)
	sub=oSubtract.allSub()
	print("Subtraction of two numbers",sub)
	input()
	