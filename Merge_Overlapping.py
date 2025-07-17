def merge_overlapping_intervals(arr):
    arr.sort()
    ans = []

    for interval in arr:
        if not ans or interval[0] > ans[-1][1]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans

arr = [[1, 3], [2, 4], [5, 6]]
print(merge_overlapping_intervals(arr))



