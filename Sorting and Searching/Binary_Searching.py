def binary_search(arr, tag):
    size=len(arr)

    start=0
    end=size-1

    while(start <= end):
        mid=(start + end)//2

        if(arr[mid]==tag):
            return mid
        elif(arr[mid] > tag):
            end=mid - 1
        else:
            start=mid + 1
    return -1


sorted_list=[10,15,23,45,70,97]
target=90
result=binary_search(sorted_list, target)
print(result)