class solution:
    def palindrome(self, s:str)->bool:
        l,r=0,len(s)-1

        while l<r:
            while l<r and not self.alphanumber(s[l]):
                l+=1
            while l<r and not self.alphanumber(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l,r= l+1,r-1
        return True


    def alphanumber(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
    
s="A man, a plan, a canal: Panama"
result=solution().palindrome(s)
print(result)


