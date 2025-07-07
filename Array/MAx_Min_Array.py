def max_and_min(arr):
    max=0
    min=float("inf")
    for i in range(len(arr)):

        if max<arr[i]:
            max=arr[i]
        
        if min>arr[i]:
            min=arr[i]
        
    print("Max number of list:",arr[max])
    print("Min number of list:",arr[min])

list=[1,10]
result=max_and_min(list)
print(result)
