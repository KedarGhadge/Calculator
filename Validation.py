class CheckNumber:
	def isNumber(self,aNumber):
		try:
			self.Num=int(aNumber) if aNumber.find(".")==-1 else float(aNumber) 
			#Keda : validating whether number having "." if count of it is more than throw an exception
			if (self.Num*10)%10==0:	#Kedar : multiply number by 10 and devide it again by 10 if remainder is 0 means its an integer
				print(aNumber)
				return "Int",self.Num
			else:
				print(aNumber)
				return "Float",self.Num
		except Exception as e:
			print("invalid")
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Enter valid number")
			print("Exception occurred in validation exiting a code")
			exit(1)
	

	