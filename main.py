import Addition
import AcceptNumber
class Calc:
	s=AcceptNumber.Accept()
	str1,num1=s.acceptNumber("Enter first number")
	str2,num2=s.acceptNumber("Enter 2nd number")
	# print(num1,num2)
	d = Addition.Addition(num1,num2)
	sum=d.allSum()
	print("addition of two numbers",sum)
	input()
	