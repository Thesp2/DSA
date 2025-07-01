def choocolate_distibution(arr,num):
    size=len(arr)
    
    if size==0 or num==0:
        return 0
    
    arr.sort()
    
    min_diff=float("inf")

    for i in range(size-num+1):
        min=arr[i]
        max=arr[i+num-1]
        diff=max-min
        if diff<min_diff:
            min_diff=diff
    return min_diff

list=[1,2]
students=1
result=choocolate_distibution(list, students)
print(result)