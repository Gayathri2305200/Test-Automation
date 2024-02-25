from my_lib import *
# 1. WAF: reverse_list() that takes a list as argument and reverses the elements of the list in
# place (use indexing operations, not any function or slicing)
# Logic: if l = [1,2,3,4,5] ; result = [5,4,3,2,1]
# 1 2 3 4 5 # string
# 0 1 2 3 4 # indexes
# start index = 0, end index = 4; swap the elements at index 0,4
# [5,2,3,4,1]
# start index = 1, end index = 3; swap the elements at index 1,3
# [5,4,3,2,1]
l = [1,4,3,2,5]
try:
    print("reverses the elements of the list :", reverse_list(l))
except (TypeError, ValueError) as err:
    print(err)

# Index start index 2 is not less than end index 2. Hence no need to go forward
# 2. WAF: count_even_odd() that counts and returns how many numbers are even and how
# many are odd in a list of numbers passed as argument.
try:
    count=count_even_odd(l)
    print("No of even numbers: ",count)
    print("No of even numbers: ",len(l)-count)
except(TypeError, ValueError) as err:
    print(err)


# 3. WAF: maximum() to return the largest number in a list of numbers (do not use max
# function). Function takes a list or tuple of numbers as argument.
try:
    print("largest number in a list:", maximum(l))
except(TypeError, ValueError) as err:
    print(err)

# 4. WAF: second_maximum() Create a new version of above code to return the second largest
# number.
try:
    print("second largest number:",second_maximum(l))
except(TypeError, ValueError) as err:
    print(err)

# 5. WAF: mean() that returns the mean of list of numbers passed to the function as argument.
try:
    print("the mean of list of numbers:",mean(l))
except(TypeError, ValueError) as err:
    print(err)

# 6. WAF: find_in_range() that takes a three arguments:
# a list of numbers, start, end
# The function returns a list of numbers from the original list, which lie between start and
# end.
# Ex: find_in_range([3,10, 5, 8, 2, 7], 5, 9)
# List of numbers = [3,10, 5, 8, 2, 7]
# start = 5
# end = 9
# list returned should be [5, 8, 7]
try:
    print("numbers lie between start and end: ",find_in_range(l,2,7))
except(TypeError, ValueError) as err:
    print(err)

