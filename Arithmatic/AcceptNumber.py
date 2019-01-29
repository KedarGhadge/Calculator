import Arithmatic.Validation
class Accept():
	def acceptNumber(self,str):
		try:
			self.aNumber=input(str)
			objValidation=Arithmatic.Validation.CheckNumber()
			self.Number=objValidation.isNumber(self.aNumber)
			return self.Number
		except Exception as e:
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Exception occurred in AcceptNumber exiting a code")
			exit(1)
			