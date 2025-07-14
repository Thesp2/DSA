def pair_sum(arr,target):
    s=set()

    for num in arr:
        complement=target-num

        if complement in s:
            return True
        
        s.add(num)

    return False

numbers=[3,4,5,6,1,2]
target=10
result=pair_sum(numbers, target)
print(result)