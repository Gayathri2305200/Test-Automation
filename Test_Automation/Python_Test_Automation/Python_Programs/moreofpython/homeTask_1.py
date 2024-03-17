# Find expected output:
def num_gen(start, end, diff=1):
    while start < end:
        yield start
        start = start + diff


g1 = num_gen(10, 20)
g2 = num_gen(1, 10, 4)
print(next(g1)) #10
print(next(g2)) #1
g3 = iter(g1)
print(next(g3)) #11
print(next(g2)) #5
print(next(g1)) #12


l = [10, 20, 30, 40]
itr = iter(l)
print(next(itr), next(itr)) #10,20
itr = iter(l)
print(next(itr), next(itr)) #10,20

itr = [10,20,30,40].__iter__()
print(itr.__next__(), itr.__next__()) #10,20
itr = reversed([10,20,30,40])
print(itr.__next__(), itr.__next__()) #40 ,30

# itr1 = range(10,20)
# itr2 = range(1,10,4)
# print(next(itr1))
# print(next(itr2))
# itr3 = iter(itr1)
# print(next(itr3))
# print(next(itr2))
# print(next(itr1))

# 2. Which exception is raised upon reaching the last element of on iterable via its iterator. // stop iteration

# 3. Name the two methods that are required for the iterator protocol. iter(),next()

# 4. Write a Function that takes a type or object or variable as argument and returns True or False
# depending on whether the argument is an iterable or not. (Hint: Use the dir method to get a list
# of supported operations)
def is_iterable(in_type):
    if ("__iter__" in dir(in_type)):
        return True
    else:
        return False
print(is_iterable(list))  # should print True
print(is_iterable(int))  # should print False


# 5. Write a generator, that generates Fibonacci numbers. The function takes a number as argument
# and generates numbers less than or equal to that number.
def fibonacci_generator(n):
    a,b=0,1
    while (a < n):
        yield a
        a,b=b,a+b
for i in fibonacci_generator(7):
    print("hjj",i)


# 6. Write a generator that takes a list and a predicate function (or lambda) as arguments and gives
# values after applying the lambda to the elements of the list. (The elements present in the list
# itself should not change)
# Python
def generator(l,func):
    for i in l:
        yield func(int(i))

l=[1,2,3,4,5,6]
func= lambda x : x*2
for i in generator(l,func):
    print(i, end=" ")
