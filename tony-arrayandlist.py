'''
# List is mutable and string is a special list which is immutable
# Slicing will start always from 0 and lets say if [:3] that means 0-2 so 3 position element is not included
grades = [65, 70, 60, 46, 56]
a = grades[ :3]
b = grades[-1]
c = grades[::-1]
d = grades[-1:-3:-1] #here -1 is the count to go backwards otherwise 1 is the default count
print (a)
print (b)
print (c)
print (d)

# l.pop(position) uses index to remove an element from the list
# l.remove(element) uses the value itself to identify the element from the list to remove

'''

def main():
	grades = [67, 78, 56, 67, 90]
	result = mysum(grades)
	print(result)
	print (sum(grades))
	multiplier = 10
	multiply(grades,multiplier)
	print(grades)

def mysum(numbers):
	total = 0
	tony = numbers[0:len(numbers):2] #This will pull out the even elements out based on the index
	print (tony)
	for element in numbers:
		total = total+element
	return total

def multiply(values,fact):
	for i in range(0,len(values)):
		values[i] = values[i]*fact
main()





