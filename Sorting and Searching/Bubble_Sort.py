def bubble_sort(arr):
    passes=len(arr)

    for j in range(0, passes):
        for i in range(0, passes-1-j):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr


list=[84,45,10,67,90]
result=bubble_sort(list)
print(result)