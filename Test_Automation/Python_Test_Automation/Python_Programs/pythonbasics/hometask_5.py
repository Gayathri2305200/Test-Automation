# 1. WAP to input 2 strings and swap the strings
import random
import sys

x,y="hello", "world"
x,y=y,x
print(x,y)

# 2. WAP to generate 4 random numbers in the range 0-26 and print their average
n=4
s=0
for i in range(n):
    s+=random.randint(0,26)
print("average: ",s/n)

# 3. WAP to generate and print a random capital alphabet.
print("random capital alphabet:", chr(random.randint(65,91)))

# 4. WAF get_si() that takes Principle, Rate and Time as arguments and returns the Simple
# Interest.
def get_si(p,r,t):
    si=(p*r*t)/100
    return si
print("simple interest: ", get_si(1000,2,12))

# 5. WAP get_ci() that takes Principle, Rate and Time as arguments and returns the
# Compound Interest.
def get_ci(p,r,t):
    a=(p*(1+r/100))**t
    ci=a-p
    return ci
print("Compound interest: ", get_ci(1000,10,5))

# 6. WAP get_q_r() taking 2 numbers as parameters and returns the quotient and
# remainder in the form of a tuple.
def get_q_r(a,b):
    q=a%b
    r=a/b
    t=(q,)+(r,)
    return t
print("The quotient and remainder in the form of a tuple:", get_q_r(10,15))

# 7. WAP to find the length of hypotenuse of a right angled triangle, input the height and
# base from user.
def length(b,h):
    l=(1/2)*b*h
    return l
print("the length of hypotenuse of a right angled triangle: ",length(5,2))

# 8. WAP to input number of seconds and print in days, hours, minutes and seconds
# ex: input = 10000
# Output = 0 day 2 hour 46 minute 40 second
def get_d_h_m_s(s):
    day = s // (24 * 3600)
    s = s % (24 * 3600)
    hour = s // 3600
    s %= 3600
    minute = s // 60
    s %= 60
    second = s
    print(day ," day ", hour," hour ",minute ," minute ",second," second")
get_d_h_m_s(10000)

# 9. Check your version of python interpreter without opening the interpreter (Which
# command needs to be used on the command line).
print("version of python interpreter: ",sys.version) #command line :python
# 10. Find Output :
#	X = 2
# 	X *= 3
# 	X = X%4
# 	Y = - X
# 	print(X,Y)
X = 2
X *= 3
X = X%4
Y = - X
print("X,Y=",X,Y) #output:2,-4

# 11. Find Output:
# 	def funct():
# 		pass
# 	print(funct())
def funct():
    pass
print(funct())