def countsort(arr):
    n=len(arr)
    maxval=max(arr)

    counter=[0]*(maxval+1)
    for i in arr:
        counter[i]+=1

    for i in range(1,maxval+1):
        counter[i]+=counter[i-1]

    ans=[0]*n
    for i in range(n-1,-1,-1):
        val=arr[i]
        ans[counter[val]-1]=val
        counter[val]-=1
    return ans

array=[1,4,3,2,2,1]
print(countsort(array))