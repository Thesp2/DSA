def trapping_rainwater(arr):
    n=len(arr)
    lmax=rmax=total=0
    l,r=0,n-1

    while l<r:
        if (arr[l]<arr[r]):
            if arr[l]<lmax:
                total += lmax - arr[l]
            else:
                lmax=arr[l]
            l += 1
        else:
            if (arr[r]<rmax):
                total += rmax - arr[r]
            else:
                rmax=arr[r]
            r -= 1
        
    return total

numbers=[0,3,0,2,3,0,2]
result=trapping_rainwater(numbers)
print(result)