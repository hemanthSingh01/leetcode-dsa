class Solution:
    def longestValidParentheses(self, s: str) -> int:
        l=r=maxi=0
        for i in s:
            if i=="(":
                l+=1
            else:
                r+=1
            if l==r:
                maxi=max(maxi,l*2)
            elif r>l:
                l=r=0
        l=r=0
        for i in s[::-1]:
            if i=="(":
                l+=1
            else:
                r+=1
            if l==r:
                maxi=max(maxi,l*2)
            elif r<l:
                l=r=0
        return maxi
