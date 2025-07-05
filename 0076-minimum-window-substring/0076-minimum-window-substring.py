class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if not s1 or not s2 or len(s2) > len(s1):
            return ""
        dici=Counter()
        dici_s2=Counter(s2)
        min_len=float("inf")
        l=0
        res=""
        for r in range(len(s1)):
            if s1[r] not in dici:
                dici[s1[r]]=1
            else:
                dici[s1[r]]+=1
            while dici>=dici_s2:
                if min_len > r-l+1:
                    min_len=r-l+1
                    res=s1[l:r+1]
                dici[s1[l]]-=1
                if dici[s1[l]]==0:
                    del dici[s1[l]]
                l+=1
        return res
        
        