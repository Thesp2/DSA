def majority(arr):
    n=len(arr)
    candidate=-1
    count=0

    for num in arr:
        if count==0:
            candidate=num
            count=1
        elif num==candidate:
            count+=1
        else:
            count-=1
    
    count=0
    for num in arr:
        if candidate==num:
            count+=1
    
    if count>(n//2):
        return candidate
    else:
        return -1

arr= [1, 1, 2, 1, 3, 5, 1]
print(majority(arr))