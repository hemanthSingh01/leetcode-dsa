
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        l=[[] for _ in range(numRows)]
        i=0
        d=1
        for char in s:
            l[i].append(char)
            if i==0:
                d=1
            elif i==numRows-1:
                d=-1
            i=i+d
        result=""
        for i in range(numRows):
            result+="".join(l[i])
        return result