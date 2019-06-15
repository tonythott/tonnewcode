#String reverse by slicing

a = input("Enter the word : ")
b = a[::-1]
print (b)

#String reverse by using for loop
s = input("Enter the string : ")
l = len(s)
for i in range(l-1,-1,-1):
	print(s[i],end="")

#without ''.join reversed function will return only the memory location of the reversed string
a = ''.join(reversed('jack'))
print (a)

#-------------------------------------------------------------------------------------------------
#Print vowels
name = input('Enter your sentence: ' )
for i in name:
    if i in 'aeiou' or i in 'AEIOU':
        print(i,end="")

s = input("Enter the word:")
sum = 0
for i in s:
	if i =='a' or i =='e' or i =='i' or i =='o' or i =='u' or i =='A' or i =='E' or i =='I' or i =='O' or i =='U':
		sum += 1
print ("The total numnber of vowels are :",sum)

#Print the sub string:
a = input("Enter the word:")
l = len(a)
for i in a:
	print (i)
for i in range(l-1):
	print(a[i],a[i+1])
for i in range(l-2):
	print(a[i],a[i+1],a[i+2])
for i in range(l-3):
	print(a[i],a[i+1],a[i+2],a[i+3])


#Program that reads integer and display *

a = int(input("Enter the number:"))
size = a
for i in range(size):
    print ('*' * size)

inner_size = size - 2
print ('*' * size)
for i in range(inner_size):
    print ('*' + ' ' * inner_size + '*')
print ('*' * size)

a = int(input("Enter the number:"))
size = a
inner_size = size -2
print ('*' * size, '','*' * size)
for i in range(a-2):
	print ('*' * size, '','*' + ' ' * inner_size + '*')
print ('*' * size, '','*' * size)













