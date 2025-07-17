def merge_operation(arr):
    ans=0
    n=len(arr)
    l,r=0,n-1

    while l<=r:
        if arr[l]==arr[r]:
            l += 1
            r -= 1
        elif arr[l]>arr[r]:
            r -=1
            arr[r] += arr[r+1]
            ans += 1
        else:
            l += 1
            arr[l] += arr[l-1]
            ans += 1
    return ans

nums=[1,5,6,5,5,1]
print(merge_operation(nums))

