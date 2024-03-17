import re
# 1. Write a regex(WAR) that matches the word ‘python’ case insensitive.
word="python"
print(re.findall("python","Python is a programming langauge",re.IGNORECASE))

# 2. WAR that matches any string of any length except newlines.
word='''hi 
hello
python
'''
print(re.findall(".",word))
# 3. WAR that matches stings in the format ‘aaaabbbb’, where a denotes digit and b denotes non-digit symbols.
s="2024year 05month 22Date 2023year"
print(re.findall(r'\b\d{4}\D{4}\b',s))
# 4. WAR to match xx_xx_XX, where x = any alphabet; _ = any white space; X = any non-whitespace.
print(re.findall(r'[a-zA-Z]{2}\s[a-zA-Z]{2}\s\S{2}',"ab cd fg"))
# 5. WAR to match strings starting with 3 digit characters.
# print(re.findall(r'\b^\d{3,}',"abc 235fg 56787"))
print(re.findall(r'\b[0-9]{2}.+',"abc 235fg 56787f"))
# 6. WAR to match individual characters which are now vowels.
# 7. WAR that matches any 4 digit number.
print(re.findall(r'[^0-9]{4}',"python released in 1991"))
# 8. WAR to match numbers with 6-10 digits.
print(re.findall(r'[0-9]{6,10}',"abc789564jk 235678 56787900"))
# 9. WAR to match any lower case alphabet.
print(re.findall(r'[a-z]',"abc 235fg 56787f"))
# 10. WAR to match all strings of the form ABBBBBB; where B can repeat 0 or more times.
print(re.findall(r'AB*',"abc 235fg ABBBBBB ABBB"))
# 11. WAR to match all string ending in any of these three characters (., ?, !)
print(re.findall(r'.+[./?/!]$',"uii a77777? b888888."))
# 12. WAR to match and extract values of all 3 digit numbers.
print(re.findall(r'\b\d{3}\b',"abc 235fg 777 888"))
# 13. WAR to check if a string is a negative string i.e. If contains any of the words: not, no,
print(re.findall(r'not|no',"This is not a negative no string"))
# 14. WAR to extract XML tags [use backreference to validate and groups to extract content and the
# tag]
print(re.findall(r'<([a-zA-Z_][a-zA-Z0-9_]*)([^>]*)>(.*?)<\/\1>',"<xml>project1</xml><book>project2</book>"))