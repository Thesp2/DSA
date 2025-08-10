def triplets(arr,sum):
    n=len(arr)
    arr.sort()
    ans=0

    for i in range(0,n-2):
        j=i+1
        k=n-1
        while j<k:
            if arr[i]+arr[j]+arr[k]>=sum:
                k=k-1
            else:
                ans+=(k-j)
                j+=1
    return ans

arr= [-2, 0, 1, 3]
sum = 2
print(triplets(arr,sum))