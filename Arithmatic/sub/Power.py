class Exponantial:
	def __init__(self,fnum,snum):
		self.fnum=fnum
		self.snum=snum
	def powerup(self):
		self.powered=(self.fnum)**(self.snum)
		return (self.powered)
