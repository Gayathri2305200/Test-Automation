# 1. Write a for loop to print numbers from 1 to 10. All numbers should be in separate lines.
import random

for i in range(0,11):
    print(i, end="\n" )

# 2. Write a for loop to print numbers from 10 to 1. All numbers should be in separate lines.
for i in range(10,0,-1):
    print(i, end="\n" )

# 3. Print Elements at Odd indexes from a list (Using for loop)
list=[10,11,20, 21,30, 31, 40, 41]
print("Elements at Odd indexes from a list:")
for x in range(1,len(list),2):
     print(list[x])

# 4. Create a list of 5 random numbers and then print the list, sum of all numbers and average. Use
# a for loop.
n=int(input("enter length of List : "))
l=[]
s=0
for i in range(n):
    l.append(random.randint(0,10))
    s=s+l[i]
print("List: ",l)
print("Sum of all numbers: ",s)
print("The average of all numbers  in list: ",s/n)

# 5. WAP to input a string and print individual characters in the string using for loop.
s=input("EnterString: ")
[print(i) for i in s]

# 6. WAP to input a string and print the ASCII value of each character in the string.
s=input("EnterString: ")
[print("The ascii value of"+ i+"is: ",ord(i)) for i in s]

# 7. WAP to input a string and store ASCII values of all characters in a tuple.
s=input("EnterString: ")
t=tuple(ord(i) for i in s)
print("ASCII values of all characters in a tuple: ",t)

# 8. Write a function that takes a list of numbers from user as argument and returns the sum of only
# odd numbers (Use only for loop. No need to use if statement).
def sum_of_odd_num(l):
    l1=[i for i in l if int(i)%2!=0]
    return sum(l1)
l=[]
print("Enter number in list:")
for i in range(0,5):
    l.append(int(input()))
print("The sum of odd numbers in list: ",sum_of_odd_num(l))

# 9. WAP to input a list of numbers and store in a tuple. Now input another number and print the
# index of this number in the tuple.
l=[1,2,4,5]
t=tuple(l)+(7,)
for i in range(len(t)):
    if(t[i]==7):
        print("index of the number in the tuple", i)

# 10. WAP to input 10 numbers repeatedly (using range based for loop) and store them in a list.
l=[]
print("Enter elements in List: ")
for i in range(10):
    l.append(int(input()))
print(l)

# 11. Update the above program to also print the sum of numbers.
l = []
s=0
print("Enter elements in list: ")
for i in range(10):
    l.append(int(input()))
    s+=l[i]
print(l)
print(s)

# 12. WAP to input a number and print all numbers from 1 till that number
def print_numbers(n):
    return [i for i in range(1,n)]
print("numbers from 1 till that number: ",print_numbers(6))

# 13. WAP to input a number and print its factorial. Factorial is denoted by n!, where n is the number
#     whose factorial is to be found.
#         Ex: if n = 4 output should be 24
#         4! = 1x2x3x4 = 24
def factorial(n):
    if (n==0 or n==1):
        return 1
    return (n * factorial(n-1))
n=4
print("The factorial of 4 is :", factorial(n))
