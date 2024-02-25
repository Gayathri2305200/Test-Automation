# 1. Guess output of each slice:
s="Python is Object Oriented"
print(s[-1]) #d
print(s[::-1])
print(s[:-1])
print(s[1:1])
print(s[4:10])
# 2. What error do you see for following statements:
# s= ""
# print(s[1])

# 3. Do you get any error for the following code, if not give the output:
S="Landry"
print(S[1])

# 4. Find output of the following:
s="a b cd"
print(len(s))
print(s[::2])
print(len(s[::2]))

s="a#b#c#d#"
print(s.split())
print(s.split("#"))
l=s.split("#")
s="".join(l)
print(s)

S="Landry"
S=S[::-2][::-2]
print(S)

print(1>2)
print(4%2, 5%2, 2%5, sep=",")
s="abcba"
s.upper()
print(s)
print(s.count("A"), end = ",")
print(s.count("", 2,4) , end =",")
print(s.count("", 2,4) , end = ",")

# 5. WAP to input a string and remove all spaces from it.
s="i like python programming"
print(s.replace(" ", ""))

# 6. What does this symbol denote:
# 	[]->list
# 7. WAP to print all methods(functions/operations) available in a string (Hint : dir())
print(dir(str))

# 8. Using the above method, get all methods available for str (strings) and join it into a space
# separated string. (use join and dir methods)
# Python
# Landry Gupta tuteur.py@gmail.com
l=dir(str)
print(" ".join(l))

# 9. Write statement to check if rstrip method is available in the str class.
# (Hint : Use the find function or in)
print("rstrip" in dir(str))

# 10. WAP to input a string and replace all space with new lines (\n) and print again.
s="I like programming"
print(s.replace(" ","\n"))

# 11. WAP to input Complete name and split it into first and last name and print it.
# also print after reversing each.
# Ex: if complete name is "ab cd"
# then print "dc ba"
s="python programming"
print(s[::-1])

# 12. WAP to input a string and split it into 2 halves. The string can be of any length
# Ex-1: Input ="String"
# S1 = Str
# S2 = ing
# Ex-2: Input = "words"
# S1 = wo
# S2 = ds
s="words"
s1=s[:len(s)//2]
if len(s)%2==0:
    s2=s[len(s)//2:]
else:
    s2 = s[len(s)//2+1:]
print(s1,s2)