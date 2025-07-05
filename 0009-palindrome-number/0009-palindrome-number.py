class Solution(object):
    def isPalindrome(self, x):
        if x<0:
           return False
        else:
           b=[ i for i in str(x)]
           c=b[::-1]
           n1="".join(map(str,c))
           r=int(n1)
           if x==r:
               return True
           else:
               return False