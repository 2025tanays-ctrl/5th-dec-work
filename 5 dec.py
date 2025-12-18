"""
class student:

    def display(self):
        print("Name:", self.name) 
        print("Age:", self.age)
        print("roll number:", self.rollnumber)
s1 = student()
s1.name = "Tanay"
s1.age = 20
s1.rollnumber = 123
s1.display()
s2 = student()
s2.name = "Ananya"
s2.age = 21
s2.rollnumber = 456
s2.display()
s3 = student()
s3.name = "Aarav"           
s3.rollnumber = 789
s3.age = 22
s3.display()
"""
"""
class employee:

    def display(self):
        print("Name:", self.name) 
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
e1 = employee()
e1.name = "Tanay"
e1.age = 20 
e1.emp_id = 123
e1.display()
e2 = employee()         
e2.name = "Ananya"
e2.age = 21
e2.emp_id = 456
e2.display()
e3 = employee()
e3.name = "Aarav"
e3.age = 22
e3.emp_id = 789
e3.display()
e4 = employee()
e4.name = "Riya"
e4.age = 23
e4.emp_id = 101
e4.display()
e5 = employee()
e5.name = "Kabir"
e5.age = 24
e5.emp_id = 112
e5.display()
"""
"""
class employee:

    def display(self):
        print("Name:", self.name) 
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)

e1 = employee()
e1.name = input("Enter name of employee 1: ")
e1.age = input("Enter age of employee 1: ")
e1.emp_id = input("Enter employee ID of employee 1: ")
e1.display()
"""
"""
class student:
    def __init__(self):
        self.name = "Tanay"
        self.rollnumber = 123

s1 = student()
s2 = student()

s2.name = "neha"

print(s1.name)
print(s2.name)
"""
"""
class collge: 
    def __init__(self, name, location):
        self.name = name
        self.location = location
"""
"""
# custom exception
class InsufficientbalanceError(Exception):
    def __init__(self):
        super().__init__(
            f"Insufficient Funds!!!"
        )

# ATM Account class
class ATMAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientbalanceError()
        self.balance -= amount
        print(f"${amount} withdrawn successfully.")
        print(f"remaining balance: ${self.balance}")

#------------usage----------------
try:
    account = ATMAccount(500)
    account.withdraw(100)
except Exception as e:
    print(e)
"""
"""

class calculator:
   def add(self, *args):
       if len(args) == 5:
           print("adding 5 numbers:")
           return args[0] + args[1] + args[2] + args[3] + args[4]
       elif len(args) == 4:
           print("adding 4 numbers:")
           return args[0] + args[1] + args[2] + args[3]
       else:
              print("unsupported number of arguments")
              return None
       
calc = calculator()
print(calc.add(1,2,3,4,5))          # Adding 5 numbers
print(calc.add(4,2,5,10))           # Adding 4 numbers
print(calc.add(1,2,3))              # Unsupported number of arguments
"""
""""

class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    # overriding the sound() method
    def sound(self):
        print("Dog barks")

# Creating objects
a = Animal()
d = Dog()

a.sound()   # Output: Animals make sounds
d.sound()   # Output: Dog barks  ← overridden method is used
"""
"""""
class car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

car1= car("BMW", 123456789)

print(car1.brand)
print(car1.price)
"""""
"""
class car:
     def __init__(self):
          self._speed =200

class sportscar(car):
     def show_speed(self):
          print("speed:", self._speed)

car = sportscar()
car.show_speed()
print(car._speed)
"""

"""
class bank:
    def __init__(self, balance):
        self.__balance = balance 

b = bank(5000)
print(b.get_balance())
"""

"""
class bank:
    def __init__(self, balance):
        self.__balance = balance 

    def get_balance(self):
        return self.__balance

b = bank(5000)
print(b.get_balance())
"""


