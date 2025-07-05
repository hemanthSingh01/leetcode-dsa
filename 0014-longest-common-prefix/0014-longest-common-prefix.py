class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=sorted(strs)
        f=a[0]
        l=a[-1]
        res=""
        n=min(len(f),len(l))
        for i in range(n):
            if f[i]==l[i]:
                res+=l[i]
            else:
                break
        return(res)