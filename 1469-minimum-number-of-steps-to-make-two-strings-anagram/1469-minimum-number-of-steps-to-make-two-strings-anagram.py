class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dici=Counter(s)
        dicii=Counter(t)
        res=0
        for i in dici:
            if dici.get(i,0)>dicii.get(i,0):
                res+=dici.get(i,0)-dicii.get(i,0)
        return res