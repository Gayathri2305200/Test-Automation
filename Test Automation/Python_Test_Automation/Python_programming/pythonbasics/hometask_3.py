import math

# Predict Output
S1 = "Hello"
S2 = "This is Python"
print(len(S1), len(S2))  # output : 5 14

# WAP to input a string and print its length.
s = "python"
print(len(s))  # output : 6

# WAP to input 2 numbers and print their sum and difference
a = 10
b = 20
print(a+b, a-b)   # output : 30 -10

# Predict Output
s1 = 'ab'
s2 = 'de'
s3 = s1 + s2
print(s3)   # output : abde

# Predict Output
s1 = 'ab' * 4
print(s1)   # output : abababab

# WAP to input a string s and a number n. Print the string n times on the screen,
# each should appear in a separate line (do not use any kind of loops, use the multiplication operator)
s = "abc"
n = 4
print(s * n)  # output : abcabcabcabc

# Predict Output
s1 = 'Hello'
s2 = 'This is India'
s3 = s1 + '\n' + s2
print(type(s3))  # output : str
print(len(s3))   # output :  19

# Find the name of function to find the square root
# WAP to input a number and print its square root ()
n = 16
print(math.sqrt(n))  # output : 4.0

# WAP to input 4 numbers from user and print their average
n = int(input("enter no of values: "))
s = 0
print("enter values :")
for i in range(0,n):
    q = int(input())
    s = s+q;
print("The average of the numbers: ", s/n)

# Use the help function to check what the abs function in python does
n = -3
print(abs(n))  # output : 3

# What is the output of this code when run from python interpreter
print(__name__) # output:__main__
