def slection_sort(arr):
    lenght=len(arr)

    for i in range(0, lenght-1):
        min_element=i
        for j in range(i+1 , lenght):
            if arr[min_element] > arr[j] :
                min_element=j

        arr[i],arr[min_element]=arr[min_element],arr[i]
    
    return arr 

list=[10]
sorted_list=slection_sort(list)
print(sorted_list)