def samenum(arr1,arr2,arr3):
    i,j,k=0,0,0
    ans=[]

    while i<len(arr1) and j<len(arr2) and k<len(arr3):
        if arr1[i]==arr2[j]==arr3[k]:
            ans.append(arr1[i])

            i+=1
            j+=1
            k+=1

            while i<len(arr1) and arr1[i]==arr1[i-1]:
                i+=1
            while j<len(arr2) and arr2[j]==arr2[j-1]:
                j+=1
            while k<len(arr3) and arr3[k]==arr3[k-1]:
                k+=1
        
        elif arr1[i]<arr2[j]:
            i+=1
        elif arr2[j]<arr3[k]:
            j+=1
        else:
            k+=1
    if len(ans)==0:
        return -1
    else:
        return ans

arr1=[1,5,10,20,30]
arr2=[5,13,15,20]
arr3=[5,20]

result=samenum(arr1,arr2,arr3)
print(result)
