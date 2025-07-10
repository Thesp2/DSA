def next_permutation(arr):
    n=len(arr)
    pivot=0

    for i in range(n-1,0,-1):
        if arr[i-1]<arr[i]:
            pivot=i
            break

    if pivot==0:
        arr.sort()
        return
    
    swap=n-1

    while arr[pivot-1]>=arr[swap]:
        swap -= 1

    arr[pivot-1],arr[swap]=arr[swap],arr[pivot-1]

    arr[pivot:]=sorted(arr[pivot:])
    return arr

list=[1,2,5,4,3,2,1]
result=next_permutation(list)
print(result)
