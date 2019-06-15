#Read from the file
'''
infile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\input.txt","r")
line = infile.readline()
while line !=   "":   #when it print it always add a new line and when it read it always add a new line so in effect two \n(new line)
	line = line.rstrip()
	print (line)
	line = infile.readline()

#Write from a file. Read from input.txt and write it to output.txt

infile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\input.txt","r")
outfile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\output.txt","w")
line = infile.readline()
while line !=   "":   #when it print it always add a new line and when it read it always add a new line so in effect two \n(new line)
	line = line.rstrip()
	print (line)
	outfile.write("The name of the student is %s\n"%line)
	line = infile.readline()



#By making use of the for loop to do the read and write 

infile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\input.txt","r")
outfile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\output.txt","w")

for line in infile:
	print(line)
	outfile.write(line)

#split function
infile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\input.txt","r")
outfile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\output.txt","w")
s = "Tony :is a :smart :man"
mylist = s.split(":",1) #rsplit and lsplit is possible
s = "Tony \nis a \nsmart \nman"
mylist1 = s.splitlines()
for word in mylist:
	print(word)
for word1 in mylist1:
	print(word1)
'''
infile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\record.txt","r")
#outfile = open("C:\\Users\\tgeorge\\Documents\\Python Scripts\\recordoutput.txt","w")
for line in infile:
	line = line.rstrip()
	#print(line)
	wordlist = line.split(":")
	name = wordlist[0]
	ssn = wordlist[1]
	address = wordlist[2]
	gpa = wordlist[3]
	print("Name is :",name)
	print("ssn is :",ssn)
	print("Address is :",address)
	print("Gpa is :",gpa)
infile.close()























