
def solution(A, B):
    N=len(A)+1
    # Implement your solution here
    for i in range(N):
        a=sum(A[:i+1])
        b=sum(A[i+1:N])
        c=sum(B[:i+1])
        d=sum(B[i+1:N])
        if((a==b) and (b==c) and (c==d)):
            return i+1
            break
    return 0
N=5
A=[2,-2,-3,3]

B=[0,0,4,-4]
print(solution(A,B))

g

