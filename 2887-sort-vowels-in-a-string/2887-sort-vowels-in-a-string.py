class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        vow={"a","e","i","o","u"}
        for ch in s:
            if ch.lower() in vow:
                l.append(ch)
        l.sort()
        i=0
        res=""
        for ch in s:
            if ch.lower() in vow:
                res+=l[i]
                i+=1
            else:
                res+=ch
        return res