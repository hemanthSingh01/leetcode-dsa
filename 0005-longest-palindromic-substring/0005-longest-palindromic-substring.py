class Solution:
    def longestPalindrome(self, s: str) -> str:
        s2=s[::-1]
        if s==s2:
            return s
        l=[ s[i:j] for i in range(len(s))for j in range(i+1,len(s)+1) if s[i:j]==s[i:j][::-1]]
        dici={}
        for i in l:
            if i not in dici:
                dici[i]=len(i)
        res=max(dici,key=dici.get)
        return res
        