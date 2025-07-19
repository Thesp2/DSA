from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        # Convert all integers to strings
        elements = list(map(str, nums))
        
        # Define a custom comparator function
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0

        # Sort the elements using custom comparator
        elements.sort(key=cmp_to_key(compare))

        # Edge case: if the largest element is '0'
        if elements[0] == "0":
            return "0"

        # Join the sorted elements into a single string
        return ''.join(elements)
sol = Solution()
print(sol.largestNumber([3, 30, 34, 5, 9]))
