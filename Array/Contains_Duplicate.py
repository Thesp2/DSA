class result:
    def find_duplicate(arr):
        if not arr:
            return []

        max_val = max(arr)

        count = [0] * (max_val + 1)

        for num in arr:
            count[num] += 1

        sorted_arr = []
        for num in range(len(count)):
            sorted_arr.extend([num] * count[num])
        
        size=len(sorted_arr)
        
        for i in range(size-1):
            if sorted_arr[i]==sorted_arr[i+1]:
                return True
        return False

array=[7,2,0,1,3]
print(result.find_duplicate(array))

