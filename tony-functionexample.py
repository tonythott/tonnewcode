# "main' is the start of the application 
# "main()" is the end of the application
# This is not working !
from sys import exit
def main():
	b = False
	a = input("Enter the temp in fahrenheit: ")
	if (a.isdigit() == False):
		a = input("Enter a valid temp in fahrenheit: ")
		f = validation(a)
	else :
		f = int(a)

  	if (f>=-273 and f<=273):
    	b = True
	if (b == False):
			for i in range(3):
				f = int(input("Enter a valid temp in fahrenheit: "))
				if (f>=-273 and f<=273):
					b = True
					break
	if (b == False):
		print("You did not enter a valid temp , program terminates !")

	while(f>=-273 and f<=273):
		c = convert(f)
		print ("celsius for ",f,"Fahrenheit is",int(c))
		cont = input("if you want to continue then press y or press any char:")
		if (cont == 'y' or cont == 'Y'):
			f = int(input("Enter a temp in fahrenheit: "))
			f = validation(a)
		if(f<-273 or f>273):
			print("Temperature",f,"Invalid and program terminates !")
			
			b = False
		else:
			b = False
	if (b == False):
		print("thanks and bye !")

def convert(ft): #Header part of the function
	celsius = (ft-32)*5/9
	return celsius

def validation(g):
	if (g.isdigit()):
		print ("Invalid temp !")
		exit()
	else: 
		h == int(g)
	return h
main()


