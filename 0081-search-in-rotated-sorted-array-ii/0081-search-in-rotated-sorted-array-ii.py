class Solution:
    def search(self, arr: List[int], target: int) -> bool:
        s=set(arr)
        if target in s:
            return True
        else:
            return False
      