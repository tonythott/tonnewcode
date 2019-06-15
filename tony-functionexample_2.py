'''
def cubevolumn(sidelength):
	volumn = sidelength ** 3 #Here volumn is the local variable
	return volumn #scope of the volumn is the moment it returns the value

result1 = cubevolumn(10)
print (result1)

def cubevolumn(sidelength):
	if (sidelength < 0):
		return 0
	else :
		volumn = sidelength ** 3
		return volumn

result1 = cubevolumn(-10)
result2 = cubevolumn(10)
print (result1)
print (result2)

def boxstring(contents):
	n = len(contents)
	if n == 0:
		return 
	print("_" * (n+2))
	print("!"+contents+"!")
	print("_" * (n+2))

boxstring("tony")


def square(n):
	result = n*n   #result in this function is different from what is defined in main function
	return result

def main():
	result = square (3) + square(4)
	print (result)

square(100)

balance = 10000
def withdraw(amount):
	global balance
	if balance >= amount :
		balance = balance - amount
		return balance

withdraw(100)

def first_digit(number):
	while (number >= 10):
		number = number // 10
	return number

num = int(input("Please Enter any Number: "))
firstDigit = first_digit(num)
print("The First Digit from a Given Number %d = %d"%(num, firstDigit))


def lastDigit(number):
    return number % 10

number = int(input("Please Enter any Number: "))
last_digit = lastDigit(number)
print("The Last Digit in a Given Number %d = %d" %(number, last_digit))

'''
def repeat(string,n,delim):
	s = (string+delim)*(n-1) 
	g = s+string
	return g

repeat("tony",3,"tgt")






































