def search_RSA(arr: list[int], target: int)->int:
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            
            if target==arr[mid]:
                return mid
            
            if arr[start]<=arr[mid]:
                if target>arr[mid] or target<arr[start]:
                    start=mid+1
                else:
                    end=mid-1

            else:
                if target<arr[mid] or target>arr[end]:
                    end=mid-1
                else:
                    start=mid+1
            
        return -1
    
list=[5,6,7,0,1,2,3,4]
goal=6
result=search_RSA(list, goal)
print(result)


            
            

        