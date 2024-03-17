from diff import diff
# 1. Write a program in python that stores alphabets from a to z in a text file.
alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\alphabets.txt", "w")
for i in range(97,123):
    alphabets.writelines(chr(i))

# 2. Write a program to read itself and print on the screen (Use Command Line Arguments).
alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\alphabets.txt", "r")
f1=alphabets.read()
print(f1)

# 3. Predict output of the following piece of code:
alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\alphabets.txt", "w")
alphabets.write("line with some characters")
alphabets.close()

alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\alphabets.txt", "r")
print(alphabets.tell())
print(alphabets.read(4))
print(alphabets.tell())

# 4. Write a program to read a file and copy it into a new file.
new_alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\new_alphabets.txt","a")
new_alphabets.write(f1)

# 5. Write a program to read a file and copy the contents to a new file such that the case gets
# reversed. i.e. upper case becomes lower case and vice versa.
rev_Cap_alphabets=open(r"C:\Users\Gayathri_Kurapati\Desktop\python\Input_Output\rev_cap_alphabets.txt","a")
f2=f1[::-1].upper()
rev_Cap_alphabets.write(f2)

# 6. Write a program that take a file name as command line argument, opens it and then counts
# number of space characters in that file.
fileName=input("Enter fileName: ")
path="C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(fileName)
with open(path, "r") as f1:
    numOfSpaces=f1.read().count(" ")
    print("number of spaces: ",numOfSpaces)

# 7. Modify the above program to count the occurrence of each symbol i.e. count of alphabet ‘a’,
# count of spaces, count of commas and so forth.
fileName=input("Enter fileName: ")
path="C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(fileName)
with open(path, "r") as f1:
    f2=f1.read()
    f3=set(f2)
    for i in f3:
        num=f2.count(i)
        print("count of ",i,":",num)

# 8. Write a script called diff.py that take two file names as arguments and checks if the content of
# both the files is same and prints true or false.
fileName1=input("Enter File 1: ")
fileName2=input("Enter File 2: ")
diff(fileName1,fileName2)
# 9. WAP to count the number of words in a file.
fileName=input("Enter fileName: ")
path="C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(fileName)
with open(path, "r") as f1:
    f2=f1.read()
    l=f2.split()
    print("count the number of words: ",len(l))

# 10. Update the above program to count the number of palindromes present in the file.
fileName=input("Enter fileName: ")
path="C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(fileName)
with open(path, "r") as f1:
    f2=f1.read()
    l=f2.split()
    i=0
    for j in l :
        if j==j[::-1]:
            i+=1
    print("number of palindromes: ",i)

# 11. Update the program again to count and print number of anagrams in the file.
fileName=input("Enter fileName: ")
path="C://Users//Gayathri_Kurapati//Desktop//python//Input_Output//{}".format(fileName)
with open(path, "r") as f1:
    f2=f1.read()
    l=f2.split()
    count=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if sorted(l[i]) == sorted(l[j]):
                count+=1
    print(" number of anagrams :",count)