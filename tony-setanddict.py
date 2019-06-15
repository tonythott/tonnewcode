'''
#set is a container that stores a collection of unique values
#Union , intersection , substraction for sets 
#Substruction means remove elements from intersection of a and b
list =[] #empty list
setN = {} #error
setN = set() #empty set

cast = {"tony","preetha","luke"}
if luke in cast:

for tony in sorted(cast) :
print (tony)

cast = set(["tony","preetha","luke"])
cast.add("tessa")

#to get to know the hash
print(hash("tony"))


namelist = ["tt","nn","jj","rr","uu"]
names = set(namelist) #copy list and create a new set
names.add("nn") #You cant have same elements in a set so elemensts wont repeat but in a list we can repeat items
names.discard("rr") #we can use "remove" also
for elem in names:
	print(elem)

#To remove everything from the set
names.clear()

namelist1 = ["tt1","nn2","jj3","rr4","uu5"]
namelist2 = ["tt1","nn","jj3","rr4","uu5"]
names1 = set(namelist1)
names2 = set(namelist2)
#nameunion = names1.union(names2)
#nameunion = names1.intersection(names2)
nameunion = names1.difference(names2)
for elem in nameunion:
	print(elem)
if names2.issubset(names1):
	print("True")
else:
	print("False")

'''
#Dictionary or map ; key is unique and value can be anything
d = dict()
d = {}

d = dict()
d["tony"] = 98
print (d)

sd = {"Tony":98,"preetha":99,"pre":99,"etha":99,"tha":99}
print (sd)

td = {}
td["tony"] = 98
print (td)

if "tony" in d:
	print("YES")

td["tony"] = 101
print(td["tony"])

print(len(sd))

l = sd.values()
print (l)

sd.pop("preetha")
print(sd)

print(sd.get("tony","not found"))
print(sd.get("Tony","not found")) #if key doesnt exist then print "not found" as per the given example
for elem in sd:
	print(sd[elem]) # print all the value for the keys exist in the dict

#item() # this will return both key and value ; it will return it as tuple

for item in sd.items():
	print(item[0], "   ",item[1])

for (u,v) in sd.items():
	print(u, "   ",v)






























