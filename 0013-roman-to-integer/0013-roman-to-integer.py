class Solution(object):
    def romanToInt(self, s):
       dici={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
       res=0
       for i in range(len(s) - 1):
           if dici[s[i]] < dici[s[i + 1]]:
               res -= dici[s[i]] 
           else:
               res += dici[s[i]] 
       res += dici[s[-1]]
       return res