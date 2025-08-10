def ceiling(arr,x):
    lo=0
    hi=len(arr)-1
    res=-1

    while lo<=hi:
        mid=lo+(hi-lo)//2

        if arr[mid]<x:
            lo=mid+1
        else:
            res=mid
            hi=mid-1

    return res

arr=[1,2,8,10,10,12,19]
x=5
print(ceiling(arr,x))