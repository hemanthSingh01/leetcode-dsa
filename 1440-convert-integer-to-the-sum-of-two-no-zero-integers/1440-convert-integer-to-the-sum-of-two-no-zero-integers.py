class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        i=1
        def isZero(b):
            for i in str(b):
                if i=="0":
                    return False
            return True
        while i<n:
            b=n-i
            if isZero(b) and isZero(i):
                return [i,b]
            i+=1