def smallest(s,t):
    if t=="":return ""

    countT,window={},{}

    for c in t:
        countT[c]=countT.get(c,0)+1
    
    have,need=0,len(countT)
    res,resLen=[-1,-1],float ("inf")
    l=0

    for r in range(len(s)):
        k=s[r]
        window[k]=window.get(k,0)+1

        if k in countT and window[k]==countT[k]:
            have +=1
        
        while have==need:
            if (r-l+1)<resLen:
                res=[l,r]
                resLen=r-l+1
            
            window[s[l]] -=1

            if s[l] in countT and window[s[l]]<countT[s[l]]:
                have -=1
            
            l+=1
    l,r=res

    return s[l:r+1] if resLen != float("inf") else ""

s="timetopractice"
t="toc"
print(smallest(s,t))