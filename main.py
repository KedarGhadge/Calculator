import Addition
class Calc:
	print("Enter 2 nos.")
	num1=input("First number:")
	num2=input("Second number:")
	d = Addition.Addition(num1,num2)
	sum=d.summation()
	print(sum)
	input()
	