import Arithmatic.sub.Addition
import Arithmatic.sub.Subtraction
import Arithmatic.sub.Multiplication
import Arithmatic.sub.Division
import Arithmatic.sub.AcceptNumber
import Arithmatic.sub.Power
class Mathematics:
	def operation(self):
		try:
			s=Arithmatic.sub.AcceptNumber.Accept()
			num1=s.acceptNumber("Enter first number : ")
			num2=s.acceptNumber("Enter 2nd number : ")
			# print(num1,num2)
			d = Arithmatic.sub.Addition.Addition(num1,num2)
			sum=d.allSum()
			print("addition of two numbers : ",sum)

			#Subtraction
			oSubtract=Arithmatic.sub.Subtraction.Subtract(num1,num2)
			sub=oSubtract.allSub()
			print("Subtraction of two numbers : ",sub)

			#Multiplicaion
			oMultiply=Arithmatic.sub.Multiplication.Multiply(num1,num2)
			mul=oMultiply.allMul()
			print("Multiplication of two numbers : ",mul)

			#Division
			oDivision=Arithmatic.sub.Division.Division(num1,num2)
			div=oDivision.allDiv()
			print("Division of two numbers : ",div)

			#Exponantial
			oExponantial=Arithmatic.sub.Power.Exponantial(num1,num2)
			power=oExponantial.powerup()
			print(str(num1) + " powered " + str(num2) + " = ",power)
		except Exception as e:
			# print(e)
			print(str(e))
			# print(e.args)
			# print("Exception occurred in AcceptNumber exiting a code")
			exit(1)
		