# A class is a template and a group of objects combine together to form a class
# class is a group of ppl with same behaviour
# Each object is called as instace variable 
# Contruct an object for you - Constructors 
# Encapsulation means - If you dont know what is inside the object then that means its encapsulated. 
# The concept of hidding the details from a user means encapsulation
# Method is another function which resides inside the class and "self" should be used within method()
# Constructor has the same name as the name of the class
# A class name or variable can start with "_"(underscore)

#Ex : tony = BankAccount()
#     print(tony.getBalance())  #Here "tony" is the "self"
#     return self_balance

class BankAccount:
	def __init__(self,n,b):  #-----------------------
		self._name=n         # >>>> Constructor <<<<<
		self._balance=b      #-----------------------

def deposit(self,dep):              #----------------------------------------------------------
	self._balance=self._balance+dep # >>> Method ; This is to add additional business logic <<< Method is also know as Accessor or getter
	                                #----------------------------------------------------------

def getBalance(self):              #----------------------------------------------------------
	return self._balance           # >>> Method ; This is to add additional business logic <<<
	                               #----------------------------------------------------------

def withdraw(self,w):              #----------------------------------------------------------
	self._balance=self._balance-w  # >>> Method ; This is to add additional business logic <<<
	                               #----------------------------------------------------------

def changeName(self,newName):      #----------------------------------------------------------
	self._name=newName             # >>> Method ; This is to add additional business logic <<<
	                               #----------------------------------------------------------

def setBalance(self,b):            #----------------------------------------------------------
	self._balance=b                # >>> Method or it is also called as mutator or setter because this function allows some correction <<<
	                               #----------------------------------------------------------

#===================================Save the below separately as tony.py==============================================
from tony-objandclass import BankAccount
tony=BankAccount("tonztoy",123456) #Here "tony" represents the address space for object and also reresent the "self"
tony.deposit(74574)
print("tonztoy has:",tony.getBalance())
tony.withdraw(23)
print ("tonztoy balance is:",tony.getBalance())
tony.changeName("preetha")
#======================================================================================================================

#we need to run the pgm by "python tony.py"

















