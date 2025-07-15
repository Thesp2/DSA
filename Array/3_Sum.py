def three_Sum(arr):
    ans=[]
    arr.sort()
    for i in range(len(arr)-1):
        if i>0 and arr[i]==arr[i-1] :
            continue
        j,k=i+1,(len(arr))-1
        while j<k:
            sum=arr[i]+arr[j]+arr[k]
            if sum > 0:
                k -= 1
            elif sum < 0:
                j += 1
            else:
                ans.append([arr[i],arr[j],arr[k]])
                j+=1
                k-=1
                while j < k and arr[j] == arr[j - 1]:  
                    j += 1
                while j < k and arr[k] == arr[k + 1]:  
                    k -= 1
        
    return ans

nums=[-1,1,0,-1,-1,4,2]
result=three_Sum(nums)
print(result)