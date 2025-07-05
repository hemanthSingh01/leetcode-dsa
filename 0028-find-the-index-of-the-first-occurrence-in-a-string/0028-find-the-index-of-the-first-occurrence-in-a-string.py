class Solution:
    def lps(self,needle: str) -> list[int]:
        lps=[0]*len(needle)
        j=0
        i=1
        while i<len(needle):
            if needle[j]==needle[i]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return lps

    def strStr(self, haystack: str, needle: str) -> int:
        lps=self.lps(needle)
        i=j=0
        while i<len(haystack):
            if haystack[i]==needle[j]:
                i+=1
                j+=1
            if j==len(needle):
                return (i-j)
            else:
                if i<len(haystack) and haystack[i]!=needle[j]:
                    if j!=0:
                        j=lps[j-1]
                    else:
                        i+=1
        return -1