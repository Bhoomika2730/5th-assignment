# Challenge 2: Implement a Calculator Class

def calculate():
    operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')

    number_1 = int(input('Please enter the first number: '))
    number_2 = int(input('Please enter the second number: '))

    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator, please run the program again.')

# Call calculate() outside of the function
calculate()


# Challenge 1: Square Numbers and Return Their Sum

def square(num):
    sum = 0
    for i in range (0, num + 1):
        sum=sum+(2 * i)*(2 * i)
    return sum
result = square(4)
print (result)


# Challenge 3: Implement the Complete Student Class

class Student:
    # Constructor
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        
         
    # Function to create and append new student   
    def accept(self, Name, Rollno):
        # use 'int(input())'method to take input from user
        ob = Student(Name, Rollno)
        ls.append(ob)
  
    # Function to display student details     
    def display(self, ob):
            print("Name   :", ob.name)
            print("RollNo :", ob.rollno)
      
            print("\n")    
         
    # Search Function    
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
  
    # Delete Function                                  
    def delete(self, rn):
        i = obj.search(rn)  
        del ls[i]
  
    # Update Function   
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll;
         
# Create a list to add Students
ls =[]
# an object of Student class
obj = Student('', 0)
  
print("\nOperations used,")
print("\n1.Accept Student details\n 2.Display Student Details\n"
      "\n3.Search Details of a Student\n4.Delete Details of Student"
      "\n5.Update Student Details\n6.Exit")
  
# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1)
obj.accept("B", 2)
obj.accept("C", 3)
         
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# elif(ch == 3):
print("\n Student Found,")
s = obj.search(2)
obj.display(ls[s])
         
# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             
# else:
print("Thank You !")


# Challenge 4: Implement a Banking Account

class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

class SavingsAccount():

    def __init__(self):
       self.balance=0
       print("hello,this is my savings account")

	
s = Bank_Account()
s = SavingsAccount()

# Challenge 5: Handling a Bank Account


class Bank_Account:
	def __init__(self):
		self.balance=0
		print("Hello!!! Welcome to the Deposit & Withdrawal Machine")

	def deposit(self):
		amount=float(input("Enter amount to be Deposited: "))
		self.balance += amount
		print("\n Amount Deposited:",amount)

	def withdraw(self):
		amount = float(input("Enter amount to be Withdrawn: "))
		if self.balance>=amount:
			self.balance-=amount
			print("\n You Withdrew:", amount)
		else:
			print("\n Insufficient balance ")

	def display(self):
		print("\n Net Available Balance=",self.balance)

# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
