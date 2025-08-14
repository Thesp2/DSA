def mincost(arr):
    arr.sort()
    n=len(arr)

    right=sum(arr)
    left=0
    ans=float('inf')

    for i in range(n):
        right -= arr[i]

        leftcost=i*arr[i]-left
        rightcost=right-(n-1-i)*arr[i]

        ans=min(ans,rightcost+leftcost)

        left += arr[i]
    return ans

arr = [1, 100, 101]
print(mincost(arr))