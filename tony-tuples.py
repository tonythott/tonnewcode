
# tuples are immutable once created and either a () or just a series of numbers are called tuple
# tuple elements can be identified through indexes
A string is also called as tuple

a = (1, 2, 3)
b = 1, 2, 3

def main():
	(px,py) = point()
	print("x value is ",px)
	print("y value is ",py)


def point():
	x = int(input("Enter x value :"))
	y = int(input("Enter y value :"))
	return (x,y)

main()

# immutable property of tuple

a = (3, 5 ,7)
a[1] = 100
print (a)

# immutable property of string

a ='tony'  #same memory locations
b = 'tony' #same memory locations
a[2]='m' # This is not possible






