class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        max_len=0
        dici={}
        for r in range(len(s)):
            if s[r] not in dici:
                dici[s[r]]=1
            else:
                dici[s[r]]+=1
            while dici[s[r]]>1:
                dici[s[l]]-=1
                if dici[s[l]]==0:
                    del dici[s[l]]
                l+=1
            max_len=max(max_len,(r-l+1))
        return(max_len)