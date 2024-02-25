import functools

# Write lambdas to:
# a. Square a number x2
y = lambda x: x**2
print(y(2))

# b. Inverse a number 1/x
y = lambda x: 1/x
print(y(2))

# c. Negate a number
y=lambda x: -x
print(y(2))

i=20

# 2. Use reduce function and an appropriate lambda to find the maximum number in a list.
l=[1,2,4,0,3,7]
print("maximum number in a list",functools.reduce(lambda x,y: x if x>y else y ,l))
# 3. Write a function map_multiple that takes a list of functions/lambdas as first argument and a
# sequence type as second argument.
# The function picks first lambda from list, applies it to first element, then applies the second
# function to the result of first one and ….
# Similarly it does for each element and generates a mapping of input to output
# def map_multiple(functs, sequence):
#  # write definition here
# Ex: let list of lambdas be from question 1 and the list on numbers be [1,2,4]
#  So first function gives [1, 4, 16]
#  Second gives [1, 0.25, 0.0625]
#  Third gives [-1, -0.25, -0.0625]. Which is the final result.
def map_multiple(functs,l):
    ans=[]
    for num in l:
        res=num
        for func in functs:
            res=func(res)
        ans.append(res)
    return ans
functs=[lambda x:x**2 ,lambda x:1/x, lambda x:-(x)]
l=[1,2,4]
print("final result:", map_multiple(functs,l))

# 4. Predict the output of following code:
f=lambda x,y :x if x>y else y
l=[10,30,50,30,10]
num=functools.reduce(f,l)
print(num)  #output :50

# 5. Find output of following:
functs=[lambda x:x**0.5 ,lambda x:1/x]
l=[1,4,16,64]
ans=[]
for num in l:
    res=num
    for func in functs:
        res=func(res)
    ans.append(res)
print(ans)  # output:[1,0.5,0.25,0.125]

# 6.Use filter function to filter a list of numbers and strings such that the result contains only
# numbers. (Hint : Use isinstance method)
def isNumbers(i):
    return isinstance(i,int)
l=["ab",1,3,"cd"]
print(list(filter(isNumbers,l)))

# 7. Assume a list containing heights ft and inches in the form of a list of string
# Example : l = [‘5ft10in’, ‘5ft’, ….]
# Write a function to convert the heights to meter. Use map function along with your function to
# convert everything to m.
def height_to_meters(l):
    l2=[]
    for i in l:
        m = 0
        t = i.split("ft")
        if t[0].isdigit():
            m = m + float(t[0]) * 0.3048
            t.pop(0)
        q = t[0].replace("in", "")
        if q.isdigit():
            m = m + float(q[0]) * 0.0254
        l2.append(m)
    return l2
l=["5ft8in", "50ft1in","50ft1in","5in"]
print(height_to_meters(l))
# 8. Write the implementation for the map function yourself by the name my_map()
def my_map(i):
    return 2*i
l=[6,7,8]
res=map(my_map,l)
print(list(res))