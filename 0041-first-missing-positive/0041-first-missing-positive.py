class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        i=0
        while i < len(arr):
            val = arr[i] - 1  
            if 0 <= val < len(arr) and arr[val] != arr[i]:
               arr[val], arr[i] = arr[i], arr[val]
            else:
                 i += 1
        for i,val in enumerate(arr):
            if val!=i+1:
                return(i+1)
                break
        else:
            return arr[-1]+1
