# 1.	Find Output of following:
# class Student:
#     pass
# s = Student()
# s.name="Guido"
# s.age=62
# print(s.name) # Guido
# print(s.age)  # 62

# 2.	For the Student class in above example, add constructor with 2 arguments for name and age, to set the name and age attributes. Create a student object, initialize it with some values and print its attributes.
class Student:
    pass
s1 = Student()
s1.name="Guido"
s1.age=62
s2 = Student()
s2.name="Bjarne"
s2.age=67
print(s1.name, s1.age) #Guido,62
print(s2.name, s2.age) #Bjarne, 67

# 3.	Find Output Again:

class Test:
    def __init__(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")
        print("1d")
s1 = Test()
s2 = Test()
#output:
# Constructor
# Constructor
# Destructor
# Destructor

class Test:
    def __init__(self):
        print("Constructor")
    def __del__(self):
        print("Destructor")
s1 = Test()
Test()
s2 = Test()
s3 = s1
del(s1)
# output:
# Constructor
# Constructor
# Destructor
# Constructor
# Destructor
# Destructor

# 4.	Add a method set_marks(marks_ list), that takes a list of marks in 5 subjects and stores in a
# new attribute marks. Also add a method print_details(), to student class to print average of marks and all details of student. (Hint : average will be calculated as (total marks)/5 ) Test your class against the following code:
# class Student:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#
#     def set_marks(self, marks_list):
#         sum = 0
#         for i in marks_list:
#             sum += int(i)
#         self.total_marks = sum
#
#     def print_details(self):
#         print("The name, id and average of the student:", self.name, self.id, self.total_marks / 5)
#
#
# if __name__ == "__main__":
#     s = Student("abc", 20)
#     s.set_marks([80, 60, 90, 70, 99])
#     s.print_details()


# 5. Create a class Circle, that stores the radius and contains 2 methods:
# get_area, get_perimeter, which give the area and perimeter respectively of the circle.
class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        print("The area of circle:", self.PI * pow(self.radius, 2))

    def get_perimeter(self):
        print("The perimeter of circle:", 2 * self.PI * self.radius)


c = Circle(14)
c.get_area()
c.get_perimeter()


# 6. Create a class SelfManaged such that it keeps track of the number of objects currently alive.
# Create a class method get_current_count(), that gives the number of objects currently alive in
# memory.
# [Hint: use a class attribute to keep count of number of objects and use __init__ and __del__
# methods to update the value of count count]
class SelfManaged:
    i = 0

    def __init__(self):
        SelfManaged.i = SelfManaged.i + 1

    def get_current_count(self):
        print(SelfManaged.i)

s = SelfManaged()
s1 = SelfManaged()
print(s.i)

# 7. Create a class BankAccount, which contains attributes balance and name, and methods
# deposit() and withdraw(), to add and deposit some money in account.
# the balance should be set to 0 in the constructor, and withdrawal should be allowed only if
# sufficient balance is there. Also overload the str method to allow printing the details directly.
class BankAccount:
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, balance):
        self.balance = self.balance + balance
        print("balance deposited successfully and current balance", self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Amount withdrawn sucessfully and Remaining balance", self.balance)


b = BankAccount("sbi")
b.deposit(40000)
b.withdraw(20000)
b.withdraw(10000)
b.deposit(20000)
