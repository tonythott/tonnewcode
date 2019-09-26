# Encapsulate lots of steps into a single entity - Function
# Functions can be resused
# Modularity
def mystdv(num):
	if type(num) != list:
		print ("Not valid , pls enter a list")
		return -1
#compute avg
x_bar = np.average(num)

#Compute squared deviation
ssd = 0
for i in num:
	ssd += (i-x_bar)**2

#compute sd
sd = math.sqrt(ssd/len(num))
return sd


mystdv(10)

#global and local variable

