def max_subaaray(arr:list[int])->int:
    maxsub=arr[0]
    cursum=0
    for i in arr:
        if cursum<0:
            cursum=0
        cursum += i
        maxsub=max(maxsub, cursum)
    return maxsub

array=[5,9,-10,7,0]
result=max_subaaray(array)
print(result)