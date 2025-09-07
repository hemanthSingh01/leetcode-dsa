class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]
        res=[]
        if n%2!=0:
            res.append(0)
        i=1
        while len(res)<n:
            res.append(-i)
            res.append(i)
            i+=1
        return(res)