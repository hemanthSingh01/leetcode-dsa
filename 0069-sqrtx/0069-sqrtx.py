class Solution:
    def mySqrt(self, x: int) -> int:
      l=0
      r=x
      res=0
      while l<=r:
        m=l+(r-l)//2
        if m*m>x:
            r=m-1
        elif m*m<x:
            l=m+1
            res=m
        else:
            return m
      return res
