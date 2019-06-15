class Rectangle:
	def __init__(self,l,w):
		self._length=l
		self._width=w
	
	def setlength(self,l):
		self._length=l

	def setwidth(self,w):
		self._width=w

	def getlength(self):
		return self._length

	def getwidth(self):
		return self._width

	def getarea(self):
		return self._length*self._width

