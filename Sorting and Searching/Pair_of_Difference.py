def pair(arr,x):
    arr.sort()
    n=len(arr)
    j=1

    for i in range(n):
        while j<n and arr[j]-arr[i]<x:
            j+=1

        if j<n and i!=j and arr[j]-arr[i]==x:
            return "Yes"
    
    return "No"

arr=[5, 20, 3, 2, 50, 80]
x = 78
print(pair(arr,x))