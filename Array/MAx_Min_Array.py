def max_and_min(arr):
    max=0
    min=0
    for i in range(len(arr)):

        if arr[max]<arr[i]:
            max=i
        elif arr[min]>arr[i]:
            min=i
        
    print("Max number of list:",arr[max])
    print("Min number of list:",arr[min])

list=[1,10]
result=max_and_min(list)
print(result)
