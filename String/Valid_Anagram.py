from collections import Counter

def is_anagram(s:str,t:str)->bool:
    return Counter(s)==Counter(t)
s="banana"
t="anaanb"
print("result:",is_anagram(s,t))

#This is same code but without counter method
# def is_anagram(s:str,t:str)->bool:

#     if len(s)!= len(t):
#         return False
    
#     counterS,counterT={},{}

#     for i in range(len(s)):
#         counterS[s[i]]=1+counterS.get(s[i],0)
#         counterT[t[i]]=1+counterT.get(t[i],0)

#     for c in counterS:
#         if counterS[c]!=counterT.get(c,0):
#             return False
#     return True    

# s="banana"
# t="anaana"
# print("result:",is_anagram(s,t))
