import copy
# Convert a Tuple t = (1,2,3,4,5) to a list
t = (1,2,3,4,5)
print(list(t))

# 2. WAP to join a list and a tuple:
L = [1,3,5,7]
T = (8,6,4,2)
LS=L+list(T)
print(LS)

# Store the result in a list LS
# 3. What is difference between list and tuple.
# 4. Print the list in reverse order
# l = [â€˜aâ€™, â€˜dâ€™, â€˜câ€™, â€˜Aâ€™, â€˜Câ€™]
l=["a","d","c","A","C"]
print("the list in reverse order: ",l[::-1])

# 5. Print Elements at Odd indexes from a list (Do not use loop)
l = [10,11,20, 21,30, 31, 40, 41]
print("Elements at Odd indexes from a list: ",l[1::2])

# 6. How many ways you can copy a list.
l1=[1,2,3]
l2=[]
l2=l1
print(l2)
l3=l1.copy()
print(l3)

# 7. Predict output
n_list = ["Happy",[2,0,1,5]]
print(n_list[0][1]) # a
print(n_list[1][3]) # 5

# 8. Predict output
odd = [2,4,6,8]
odd[0] = 1
print(odd)
odd[1:4] = [3,5,7]
print(odd)

# 9. Write a program to input a string and print if it is palindrome or not.
s="madam"
if s[::-1]==s:
    print(s,"is a palindrome")
else:
    print(s, "is not a palindrome")

# 10. Use the range method and create a tuple containing the following values:
# 	(20, 15, 10, 5)
t=()
for i in range(4,0,-1):
    t=t+(5*i,)
print(t)
# 11. WAP to convert string to list of characters.
s="hello"
l=list(s)
print(l)

