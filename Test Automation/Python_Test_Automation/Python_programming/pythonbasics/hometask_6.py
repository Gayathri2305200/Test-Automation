# WAF: bmi() that takes the weight in kg and height in cm of a person, calculates and returns the
# BMI.
# Write code that calls this function after taking height and weight as inputs and then prints
# underweight, normal, overweight or obese depending on the value of BMI.
# Refer this link for the ranges:
# https://en.wikipedia.org/wiki/Body_mass_index
def get_bmi(w,h):
    bmi=w/pow(h*0.01,2)
    return bmi
bmi=get_bmi(50,167.64)
if (bmi<=18.4):
    print("underweight")
elif (bmi>=18.4 and  bmi <=24.9):
    print("Normal")
elif (bmi>=25.0 and bmi<=29.9):
    print("overweight")
else :
    print("obese")

# 2. Take input of age of 3 people by user and determine oldest and youngest among them.
a=int(input("Enter age of a: "))
b=int(input("Enter age of b: "))
c=int(input("Enter age of c: "))
if(a>b and a>c):
    print("a is older")
    if(b<c):
        print("b is younger")
    else:
        print("c is younger")
elif(b>a and b>c):
    print("b is older")
    if (a < c):
        print("a is younger")
    else:
        print("c is younger")
elif(c>b and c>a):
    print("c is older")
    if (b<a):
        print("b is younger")
    else:
        print("a is younger")
else:
    print("all are belongs to same age")

# 3. WAP to input a number and check if number is divisible by both 5 and 7.
n=int(input("Enter number: "))
if(n%5==0 and  n%7==0):
    print("number is divisible by both 5 and 7")
else:
    print("number is not divisible by both 5 and 7")

# 4. WAF: is_alphabet() that takes a string argument and returns True or False. True if all characters
# in the string are alphabets otherwise False. (write code using for loop and if. Do not use built in
# functions)
def is_alphabet(s):
    alphabets = "abcdefghijklmnopqrstuvwxyzZYXWVUTSRQPONMLKJIHGFEDCBA"
    for i in s:
        if(i  not in alphabets):
           return False
    return True
print("Abc12: ",is_alphabet("Abc12"))
print("Abc: ",is_alphabet("Aabc"))

# 5. WAF: is_leap_year() that takes a year as input and retuns True if year is leap year, otherwise
# false.
def is_leap_year(y):
    if ( y%4==0 and(y%400==0 or y%100!=0)):
        return True
    return False
print(is_leap_year(1900))

# 6. WAF: days_in_month() that take name of month in 3 character format(MMM), and year (YYYY)
# as arguments and returns the number of days in the month.
# Use the function is_leap_year() to check the special case of 29 days in leap year for month of
# FEB. [Use dictionary to store the mapping of month and days.]
def days_in_month(mon,year):
    l=["jan","mar","may","jul","aug","oct","dec"]
    l1=["apr","jun","sep","nov"]
    if (mon=="feb"):
        if(is_leap_year(year)):
            return 29
        return 28
    elif (mon in l):
        return 31
    elif(mon in l1):
        return 30
    return "not a month"
print(days_in_month("feb",2000))

# 7. Update the above program to work with both 3 character month and complete name of month.
def days_in_month(mon,year):
    l=["january","march","may","july","august","october","december"]
    l1=["april","june","september","november"]
    if (mon=="february"):
        if(is_leap_year(year)):
            return 29
        return 28
    elif (mon in l):
        return 31
    elif(mon in l1):
        return 30
    return "not a month"
print(days_in_month("february",2000))
# 8. WAF: uncommon_words() that takes two sentences (strings) as its arguments, and returns the
# common words in both the sentences.
def uncommon_words(s1,s2):
    set1=set(s1.split())
    set2=set(s2.split())
    l=[]
    for i in set1:
        if i in set2:
            l.append(i)
    return l
s1="I like python"
s2="I like java"
print("common words: ", uncommon_words(s1,s2))

# [Hint: store all the in a set. Read the documentation for set.]