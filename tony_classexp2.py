# class fraction

class frac :
	def __init__(self,n,d):
		self._numerator = n
		self._denominator = d
	def setNumerator(self,n):
		self._numerator = n

	def setDenominator(self,d): # Mutator
		self._denominator = d

	def getNumerator(self):     # Accesor
		return self._numerator

	def getDenominator(self):    #Accesor
		return self._denominator

	def fprint(self):
		print("The fraction is %d / %d"%(self._numerator,self._denominator))

	def __repr__(self): #Function overloading
		return "(%d / %d)"%(self._numerator,self._denominator)

	#Here we write a function for the equal
	def equal(self,right):
		a=self._numerator*right._denominator
		b=self._denominator*right._numerator
		return a==b

#Here instead of writing equal function use the function overloading by calling "__eq__"
	def __eq__(self,right):
		a=self._numerator*right._denominator
		b=self._denominator*right._numerator
		return a==b

	def __add__(self,second):
		d = self._denominator*second._denominator
		n = self._numerator*self._denominator+self._denominator*second._numerator
		return frac(n,d)

	def __ne__(self,right):
		return self._numerator*right._denominator!=self._denominator*right._numerator

	def __lt__(self,right):
		a=self._numerator*right._denominator
		b=self._denominator*right._numerator
		if a < b:
			return True
		else: 
			return False

	def __abs__(self):
		n=abs(self._numerator)
		d=abs(self._denominator)
		return frac(n,d)
















