def count_sort(arr,place):
    n=len(arr)
    output=[0]*n
    count=[0]*10

    for num in arr:
        index=(num//place)%10
        count[index]+=1
    
    for i in range(1,10):
        count[i]+=count[i-1]

    for i in range(n-1,-1,-1):
        index=(arr[i]//place)%10
        output[count[index]-1]=arr[i]
        count[index]-=1

    for i in range(n):
        arr[i]=output[i]

def radix_sort(arr):
    place=1
    maxnum=max(arr)

    while maxnum//place>0:
        count_sort(arr,place)
        place*=10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)
print("Sorted array:", arr)