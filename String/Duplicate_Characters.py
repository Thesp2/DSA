def duplicate(s):
    hashmap={}

    for c in s:
        hashmap[c]=hashmap.get(c,0)+1
    
    for key in hashmap:
        if hashmap[key]>1:
            print(["{}".format(key),hashmap[key]],end=", ")


s = "programming"

duplicate(s)