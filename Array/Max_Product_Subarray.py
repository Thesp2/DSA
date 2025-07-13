def max_product(arr:list[int])->int:
    result=max(arr)
    curmin,curmax=1,1

    for n in arr:
        temp=n*curmax
        curmax=max(n*curmax, n*curmin, n)
        curmin=min(temp, n*curmin, n)
        result=max(result,curmax)
    
    return result

res=max_product([-2,3,-4])
print(res)