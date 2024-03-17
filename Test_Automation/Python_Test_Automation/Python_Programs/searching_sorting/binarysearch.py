def binary_search(l,low,high,key):
    while(low<=high):
        mid=(low+high)//2
        if l[mid]==key:
            print(key,"found at index",mid)
            break
        elif key>l[mid]:
            low=mid+1
        else:
            high=mid-1

l=[1,3,5,6,7,8,9]
key=9
binary_search(l,0,len(l)-1,key)