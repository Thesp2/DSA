def findDuplicates(arr):
    n = len(arr)
    freqArr = [0] * n
    result = []

    for num in arr:
        freqArr[num] += 1

    for i in range(n):
        if freqArr[i] > 1:
            result.append(i)

    if not result:
        result.append(-1)

    return result

arr = [1, 6, 5, 2, 3, 3, 2]
duplicates = findDuplicates(arr)

for element in duplicates:
    print(element, end=" ")