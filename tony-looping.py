##### While loop #####

#while loop for printing 1 to 100
i = 0
while i<=100:
	print (i)
	i +=1

#Print all number while are multiples of 6 within 1 to 100
i = 0
while i<=100:
	if i%6==0:
		print(i)
	i +=1

#How is the maturity for house
i = 1
p = 2500000
while i<=30:
	p = p+p*.04
	i +=1
print (p)

#How to calculate the term for the loan
years = 1
p = 100000
while p<=160000:
	p = p+p*.05
	years +=1
print ("The total number of years :",years)

#How to calculate the EMI for the loan
years = 1
p = 320000
while years<=6:
	p = p+p*.07
	years +=1
print ("EMI :",p/72)

#Add 1 to 100 by one by one(0+1+2+...100)
i=0
sum=0
while i<=100:
	sum = sum + i
	i +=1
print("The sum is :",sum)

#Calculate the projected income from an investment
balance = 100000
target = 2*balance
rate=15
year=0
while balance < target :
	interest = balance * 15/100
	balance += interest 
	year +=1
print("After",year,"years,","Your balance will be twice")

#What is a sentinel (Something to terminate the program)
# Here if the user enters negative value then it will come out from the loop and give average of the salary
sum = 0
salary = 0
count =0
while salary>= 0:
	salary = float(input("Enter the salary : "))
	if salary>0:
		count += 1
		sum += salary
if count!=0:
	avg = sum/count
	print ("The average salary is :",avg)
else:
	print("Enter a valid number !")

#Boolean value can be used to control the loop
done = False

##### For loop #####

#For is an interator

for i in "tony":
	print (i)

string = "tony" #Here "string" is called a container
for i in string:
	print(i)

for i in range(10):
	print (i)

for i in range(1,30,1):
	print (i)

for i in range(30,1,-1):
	print(i)

sum = 0
for i in range(1,101):
	sum = sum+i
	print (sum)

print ("Tony is a nice guy",end="")
print (",and he works hard !")

for i in "tony":
	print(2*i,"	",end="")


#Difference between while and for loop and also the easiness of "for" loop
name = 'Virginia'
print (len(name))
i =0
while i<len(name):
	print (name[i])
	i +=1

for i in name:
	print (i)

sum =0
for i in range(2,101):
        if(i % 2 == 0):
            sum += i
print ("The sum of all even numbers between 2 and 100 is :",sum)

sum =0
for i in range(1,101):
	sum = sum + i*i
print ("The sum of all squares between 1 and 100 is :",sum)

a = int(input("Enter the first number:"))
b = int(input("Enter the first number:"))
sum =0
for i in range(a,b+1):
        if(i % 2 != 0):
            sum += i
print ("The sum of all odd numbers between 2 and 100 is :",sum)

sum =0
n = input("Enter the number:")
for i in n :
	i = int(i)
	if i%2 != 0:
		sum +=i
print (sum)









































