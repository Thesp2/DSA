def wordtonum(s):
    arr = ["2","22","222","3","33","333",
           "4","44","444","5","55","555",
           "6","66","666","7","77","777","7777",
           "8","88","888","9","99","999","9999"]
    
    result=[]

    for ch in s.upper():
        if ch==' ':
            result.append("0")
        else:
            idx=ord(ch)-ord('A')
            result.append(arr[idx])
        
    return "".join(result)

s="Hello"
print(wordtonum(s))
