x = 40
d = x == 20
c = x >= 20
f = x <= 20
e = x != 20
print (d)
print (c)
print (e)
print (f)

#if elif statement syntax:
import re
ctc = input("Enter your CTC :")
income = re.sub('[\$,]', '', ctc)
print ("your income is :",income)
if float(income) > 150000:
	taxrate = 0.3
elif float(income) > 80000:
	taxrate = 0.25
elif float(income) > 50000:
	taxrate = 0.15
else:
	taxrate = 0.10
income = (1-taxrate)* float(income)
print ("Your gross income is : ", income)


#Calculate percentage 
sub1 = int(input("Enter mark for subject-1 : "))
sub2 = int(input("Enter mark for subject-2 : "))
sub3 = int(input("Enter mark for subject-3 : "))
salary = int(input("Enter your salary :"))
avg = float((sub1*0.25)+(sub2*0.35)+(sub3*0.40))
print ("The average for all the 3 subjects are :",avg)
tution = 14000
incentive = 0
if avg >= 90:
	grade = 'A'
	tution = tution*0.60
	incentive = 0.1
elif avg >= 80:
	grade = 'B'
	tution = tution*0.80
	incentive = 0.05
elif avg >= 70:
	grade = 'C'
	tution = tution*0.90
	incentive = 0.0
elif avg >= 60:
	grade = 'D'
	tution = tution*1.1
	incentive = -0.05
else:
	grade = 'F'
	tution = tution*1.2
	incentive = -0.1
print ("Your grade is : %s and Your tution fee is : %d"%(grade,tution))
print ("Your incentive percentage is :",incentive)
totsal = salary+(salary*incentive)
print ("Teacher salary is :",totsal)

#Relational operators
income = float(input("Enter the income : "))
years =  int(input("Enter the years in this job: "))
debt = float(input("Enter the debt : "))
ratio = income / debt
if (income > 180000 and years > 5) or (income > 250000 and ratio > 1.5):
	qualified = True
	interestrate = 0.03
elif (income > 140000 and years > 6) or (income > 200000 and ratio > 1.8):
	qualified = True
	interestrate = 0.07
elif (income > 100000 and years > 8) or (income > 150000 and ratio > 2.0):
	qualified = True
	interestrate = 0.25
else:
	qualified = False

if qualified :
	print ("Your Are Qualified and Your Interest Rate Is %d :"%(interestrate*100),"%")
else :
	print ("Sorry Not Qualified")











































