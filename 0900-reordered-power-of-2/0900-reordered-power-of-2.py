class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n==1:
            return True
        arr1=[int(i) for i in str(n)]
        sorted_num1="".join(map(str,sorted(arr1)))
        def sort(power):
            arr=[int(i) for i in str(power)]
            sorted_num="".join(map(str,sorted(arr)))
            return sorted_num
        for i in range(2,32):
            power=2**i
            if sort(power)==sorted_num1:
                return True
        return False