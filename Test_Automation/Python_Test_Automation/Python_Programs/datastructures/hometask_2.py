import sys
# Predict output of
print([i + j for i in "abc" for j in "def"])
# a) [‘da’, ‘ea’, ‘fa’, ‘db’, ‘eb’, ‘fb’, ‘dc’, ‘ec’, ‘fc’].
# b) [[‘ad’, ‘bd’, ‘cd’], [‘ae’, ‘be’, ‘ce’], [‘af’, ‘bf’, ‘cf’]].
# c) [[‘da’, ‘db’, ‘dc’], [‘ea’, ‘eb’, ‘ec’], [‘fa’, ‘fb’, ‘fc’]].
# d) [‘ad’, ‘ae’, ‘af’, ‘bd’, ‘be’, ‘bf’, ‘cd’, ‘ce’, ‘cf’].
print([i.lower() for i in "HELLO"])
# a) [‘h’, ‘e’, ‘l’, ‘l’, ‘o’].
# b) ‘hello’
# c) [‘hello’].
# d) Hello

text = "Zero One Two Three Four Five Six Seven Eight Nine"
result = [word[0] + word[-1] for word in text.split()]
print(result) # ['Zo', 'Oe', 'To', 'Te', 'Fr', 'Fe', 'Sx', 'Sn', 'Et', 'Ne']

text = "Zero One Two Three Four Five Six Seven Eight Nine"
result = [word[0] + word[-1] for word in text.split() if word[0] > word[-1]]
print(result)

text = "bangalore : city with lakes and punctures"
result = [word for word in text.split() if word.startswith(("a","e","i","o","u"))]
print(result) #['and']

# 3. Consider a list of words:
# Words = [‘Python’, ‘Object’, ‘Oriented’, ‘Language’]
# Write a loop to store the first character of each word in a list from the above list.
# Update the program to use list comprehension instead.
Words = ["Python", "Object", "Oriented", "Language"]
res=[word[0] for word in Words ]
print(res)

# 4. Input a string from user, create a list of only those words whose length is more than 5
# characters.
s ="Python is a Object Oriented Language"
l=list(s.split())
print([word for word in l if len(word)>5])

# 5. WAP to take a string as a command line argument and print whether it is palindrome or not.
s=sys.arg[0]
if s[::-1]==s:
    print(s,"is a palindrome")
else:
    print(s, "is not a palindrome")

# 6. Find Output of:
word='synonymous'
g=['a','o','n']
s=[ch if ch in g else '_' for ch in word]
s=' '.join(s)
print('_' in s,s)

# 7. Write a list comprehension to store the following in a list: [Use nested and simple list
# comprehension both]
# [‘w’, ‘wo’, ‘wor’, ‘word’, ‘words’]
s="words"
print([s[:i+1] for i in range(len(s))])

# 8. WAP to input 2 string from command line and create a list of common words in both the
# strings.
s1=sys.arg[0]
s2=sys.arg[1]
print("list of common words: ",[i for i in s1.split() if i in s2.split()])