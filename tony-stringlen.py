#To find the length of a string
length = len('world')
print (length)

#For concat the string
a = "Tony"+" "+"is great"
print (a)

#For printing a string to multiple times
print('hello'" "*10)

#Use of str for converting int to string
a = str(1234)
b = str(5678)
c = a + b
print (c)
print (int(c) + 1)
print (int(c) - 3)

#To understand index 
# Method is nothing but changing the behaviour of "a" in this example below
a = "TonyGeorge"
print (a[-3])
print (a[3])
b = a.lower()
g = a.upper()
f = a.replace('y','i')
print (b,g,f)

#Back slash inside string is called scape character , means it will not consider the following character in python
a = 'Alexandia\'s book'
print (a)
b = "Alexandia\'s \"new green deal\" \n \t \s \b"
print (b)






