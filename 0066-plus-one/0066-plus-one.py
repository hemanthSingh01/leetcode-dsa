class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l=[str(i) for i in digits]
        string="".join(l)
        a=int(string)+1
        res=[ int(i) for i in str(a)]
        return(res)