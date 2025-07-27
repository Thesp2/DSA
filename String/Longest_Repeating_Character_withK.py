def maxlength(s:str,k:int)->int:
    counter={}
    maxf=0
    res=0
    l=0

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r],0) + 1
        maxf=max(maxf,counter[s[r]])

        while (r-l+1) - maxf>k:
            counter[s[l]] -= 1
            l += 1
        
        res=max(res,r-l+1)
    return res

s="ABAABBB"
k=2
print(maxlength(s,k))
