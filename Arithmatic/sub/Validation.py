class CheckNumber:
	def isNumber(self,aNumber):
		try:
			self.Num=int(aNumber) if aNumber.find(".")==-1 else float(aNumber) 
			#Kedar : validating whether number having "." if count of it is more than throw an exception, if not valid number or enterd a character it will throw an error
			return self.Num
		except Exception as e:
			print("invalid")
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Enter valid number")
			print("Exception occurred in validation exiting a code")
			exit(1)
	

	