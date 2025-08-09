def pair(a,b,k):
    n=len(a)
    a.sort()
    b.sort(reverse=True)

    for i in range(n):
        if a[i]+b[i]<k:
            return False
        
    return True

a=[1,2,3]
b=[9,7,8]
k=10
print(pair(a,b,k))
