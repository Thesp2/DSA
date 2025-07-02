def smallest_element(arr, targate):
    size=len(arr)

    if targate>size:
        return False
    
    for j in range(0, size):
        for i in range(0, size-1-j):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]

    return arr[targate-1]

list=[1,7,2,8,3,9]
element=9
result=smallest_element(list, element)
print(result)