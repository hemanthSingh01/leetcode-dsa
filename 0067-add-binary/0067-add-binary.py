class Solution(object):
    def addBinary(self, a, b):
        s=int(a,2)
        s2=int(b,2)
        s3=s+s2
        return bin(s3)[2:]