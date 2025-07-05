class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length=0
        n=len(s)
        i=n-1
        while s[i]==" ":
            i-=1
        for i in range(i+1):
            if s[i]!=" ":
                length+=1
            else:
                length=0
        return length
