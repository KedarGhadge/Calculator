import Arithmatic.Addition
import Arithmatic.Subtraction
import Arithmatic.Multiplication
import Arithmatic.Division
import Arithmatic.AcceptNumber
import Arithmatic.Power
class Calc:
	s=Arithmatic.AcceptNumber.Accept()
	num1=s.acceptNumber("Enter first number : ")
	num2=s.acceptNumber("Enter 2nd number : ")
	# print(num1,num2)
	d = Arithmatic.Addition.Addition(num1,num2)
	sum=d.allSum()
	print("addition of two numbers : ",sum)

	#Subtraction
	oSubtract=Arithmatic.Subtraction.Subtract(num1,num2)
	sub=oSubtract.allSub()
	print("Subtraction of two numbers : ",sub)

	#Multiplicaion
	oMultiply=Arithmatic.Multiplication.Multiply(num1,num2)
	mul=oMultiply.allMul()
	print("Multiplication of two numbers : ",mul)

	#Division
	oDivision=Arithmatic.Division.Division(num1,num2)
	div=oDivision.allDiv()
	print("Division of two numbers : ",div)

	#Exponantial
	oExponantial=Arithmatic.Power.Exponantial(num1,num2)
	power=oExponantial.powerup()
	print(str(num1) + " powered " + str(num2) + " = ",power)
