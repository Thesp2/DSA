from collections import defaultdict
def groupanagrams(strs):
    res=defaultdict(list)

    for s in strs:
        counts=[0]*26

        for c in s:
            counts[ord(c)-ord("a")] += 1
        
        res[tuple(counts)].append(s)
    return list(res.values())

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupanagrams(strs))