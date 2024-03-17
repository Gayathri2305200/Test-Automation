from my_lib import frequency_of_words
# WAP to create a dictionary of numbers mapped to their negative value for numbers from 1-5.
# The dictionary should contain something like this:
# Do with both with and without range based for loop.
# {1:-1,2:-2,3:-3….}
# with range
d ={i:-i for i in range(1,6)}
print(d)
# without range
d1={}
d1[1]=-1
d1[2]=-2
d1[3]=-3
d1[4]=-4
print(d1)

# 2. Check which of the following declarations will work
#d={1=2,2=3} # wont work
d={1:2,2:3} # works
#d={1,2;2,3} # wont work
d={(1,2),(2,3)} #  works
#d={'a':'A','b':1,c:[1234]} #wont work
d={'a':'A','b':1,'c':[1234]} #works
d=dict([(1,2),(2,3)]) # works
d=dict(((1,2),(2,3))) # works
#d=dict((1,2),(2,3)]) # wont works
#d=dict(x=2,y=3) # wont works
#d=dict('x'=2,'y'=3) # wont works
#d=dict(1=2,2=3) # wont works


# 3. Read help for zip and write a program that has two lists
# l1 = [1,2,3,4]
# l2 = [10,20,30,40]
# And converts them to a dictionary d containing { 1:10,2:20 …….}
l1 = [1,2,3,4]
l2 = [10,20,30,40]
d={}
d=dict(zip(l1,l2))
print(d)
# 4. Use range based for loop to store all upper case alphabets and their corresponding ASCII
# values in the dictionary d.
# The result should be d = {‘A’: 65, ‘B’:66,…..}
d={chr(i):i for i in range(65,91)}
print(d)

# 5. Create a mapping of number to word from 0-9. (0:’zero’……)
# • Ask user for a single digit number and print the corresponding word format.
# • Print all keys of above dictionary
# • Print all Values of a dictionary
# • Print all Key and Value pairs of above dictionary
d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
print("all keys of above dictionary: ",[i for i in d.keys()])
print("all values of above dictionary: ",[i for i in d.values()])
print("all key and value pairs of above dictionary: ",{i for i in d.items()})

# 6. Predict Output of:
l1=['A','B','C','D']
l2=["Apple","Ball","Cat","Dog"]
d1=dict(zip(l1,l2))
print(d1)  # output:{'A': 'Apple', 'B': 'Ball', 'C': 'Cat', 'D': 'Dog'}
d2=dict(list(d1.items())[::2])
print(d2) # output:{'A': 'Apple', 'C': 'Cat'}

# 7. WAF: frequency_of_words() in a script my_lib.py that takes a string as argument and returns a
# dictionary containing count of each word in the string.
# Ex: a call to function with the argument “count the words in the sentence in”
# the returned dictionary should contain:
s="I like python I like java"
print(frequency_of_words(s))


