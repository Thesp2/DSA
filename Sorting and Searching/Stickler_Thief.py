def maxloot(arr):
    n=len(arr)

    if n==0:return 0

    if n==1:return arr[0]

    secondlast=0
    last=arr[0]
    res=0

    for i in range(1,n):
        res=max(arr[i]+secondlast,last)
        secondlast=last
        last=res
    return res
arr= [6, 5, 5, 7, 4]
print(maxloot(arr))