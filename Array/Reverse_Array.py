def reverse_array(arr):
    size=len(arr)
    rlist=[]
    for i in range(size-1, -1, -1):
        rlist.append(arr[i])

    return rlist

list=[12,3,44,343,5]
result=reverse_array(list)
print(result)