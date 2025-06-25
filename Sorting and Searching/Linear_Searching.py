def liner_search(arr, tag):
    size=len(arr)
    final=0
    
    while(final < size):
        if(arr[final]==tag):
            return final
        else:
            final += 1
    
    return -1

list=[10,45,33,60,34]
target=35
result=liner_search(list, target)
print(result)