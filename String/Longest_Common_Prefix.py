def check(stars):
    if not stars:
        return ''
    
    for i in range(len(stars[0])):
        char=stars[0][i]
        for s in stars[1:]:
            if i>=len(s) or s[i]!=char:
                return stars[0][:i]
            
    return stars[0]

strs=["flower", "flow", "flight"]    
print(check(strs))  