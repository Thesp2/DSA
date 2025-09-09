def partation(arr):
    total=sum(arr)

    if total%2!=0:
        return False
    
    target=total//2
    n=len(arr)

    def backtrack(i,cursum):
        if cursum==target:
            return True
        
        if cursum>target or i==n:
            return False
        
        if backtrack(i+1,cursum+arr[i]):
            return True
        
        return backtrack(i+1,cursum)
    
    return backtrack(0,0)

arr=[5,5,1,11]
print(partation(arr))