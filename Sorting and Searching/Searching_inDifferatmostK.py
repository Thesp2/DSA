def findelment(arr,k,x):
    n=len(arr)
    i=0

    while (i<n):
        if arr[i]==x:
            return i
        
        i=i+max(1,int(abs(arr[i]-x)/k))

    print("Element not found!")
    return -1

arr= [20, 40, 50, 70, 70, 60]
k = 20
x = 60
print(findelment(arr,k,x))