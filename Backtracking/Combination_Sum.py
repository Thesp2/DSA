def curcombination(arr,target,cur,res,index):
    if target==0:
        res.append(list(cur))
        return
    if target<0 or index>=len(arr):
        return
    
    cur.append(arr[index])

    curcombination(arr,target-arr[index],cur,res,index)

    cur.pop()

    curcombination(arr,target,cur,res,index+1)

def combination(arr,target):
    arr.sort()
    res=[]
    cur=[]

    curcombination(arr,target,cur,res,0)

    return res

arr = [2, 4, 6, 8]
target = 8

res = combination(arr, target)

for v in res:
    print(" ".join(map(str, v)))