import Validation
class Accept():
	def acceptNumber(self,str):
		try:
			self.aNumber=input(str)
			objValidation=Validation.CheckNumber()
			str,self.Number=objValidation.isNumber(self.aNumber)
			return str,self.Number
		except Exception as e:
			# print(e)
			# print(str(e))
			# print(e.args)
			print("Exception occurred in AcceptNumber exiting a code")
			exit(1)
			