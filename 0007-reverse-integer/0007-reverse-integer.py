class Solution(object):
    def reverse(self,x):
        
        l=[i for i in str(x)]
        l.reverse()
        if l[-1]=="-":
            l.insert(0,"-")
            l.pop()
        a="".join(l)
        b=int(a)
        if b < -2147483648 or b > 2147483647:
            return 0
        return b
        
        