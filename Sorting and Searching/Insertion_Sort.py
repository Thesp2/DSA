def insertion_sort(arr):
    size=len(arr)
    for i in range(1,size):
        current=arr[i]
        correct=i-1

        while correct>=0:
            if(arr[correct]<current):
                break
            else:
                arr[correct+1]=arr[correct]
                correct -= 1
            
            arr[correct+1]=current

    return arr

list=[1,4,3,8,6]
result=insertion_sort(list)
print(result)
