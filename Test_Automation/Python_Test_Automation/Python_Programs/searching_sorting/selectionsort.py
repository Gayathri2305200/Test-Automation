l=[2,3,1,2,4,5]
def selection_sort(l):
    for i in range(len(l)):
        min_pos=i
        for j in range(i+1,len(l)):
            if l[j]<l[min_pos]:
                min_pos=j
        l[i],l[min_pos]=l[min_pos],l[i]
    return l

print(selection_sort(l))