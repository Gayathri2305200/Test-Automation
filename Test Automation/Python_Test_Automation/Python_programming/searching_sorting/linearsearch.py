l=[1,5,6,3,4]
key=5
def linear_search(l,key):
    for i in range(len(l)):
        if l[i]==key:
            print(key,"found at index",i)
            break
linear_search(l,key)