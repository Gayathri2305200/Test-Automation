def reverse_list(l):
    start,end=0,len(l)-1
    while(start<end):
        l[start],l[end]=l[end],l[start]
        start+=1
        end-=1
    return l

def count_even_odd(l):
    count=0
    for i in l:
        if(int(i))%2==0:
            count+=1
    return count

def sort_list(l):
    l1=[]
    l1=l.copy()
    for i in range(len(l)):
        while(i<i+1):
            l1[i],l1[i+1]=l1[i+1],l1[i]
    return l1
def maximum(l):
    # max=l[0]
    # for i in range(1,len(l)):
    #     if l[i]>max:
    #         max=l[i]
    # return max
    sort_list(l)
    return l[0]

def second_maximum(l):
    sort_list(l)
    return l[1]

def mean(l):
    s=0
    for i in l:
        s+=int(i)
    return s/len(l)

def find_in_range(l,start,end):
    l1=[i for i in l if int(i)>=start and int(i) <end]
    return l1




