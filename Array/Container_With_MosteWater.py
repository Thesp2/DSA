def most_water(arr):
    tar=0
    l,r=0,len(arr)-1

    while l<r:
        area=(r-l) * min(arr[l],arr[r])
        tar=max(area,tar)

        if arr[l]<arr[r]:
            l += 1
        else:
            r -= 1
    return tar 

heights =[1,8,6,2,5,4,8,3,7]
result=most_water(heights)
print(result)       