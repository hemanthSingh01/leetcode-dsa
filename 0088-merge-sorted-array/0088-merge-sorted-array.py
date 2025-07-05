class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr=nums1[:m]
        nums1.clear()
        i=j=0
        while i<len(arr) and j<len(nums2):
            if arr[i]<=nums2[j]:
                nums1.append(arr[i])
                i+=1
            else:
                nums1.append(nums2[j])
                j+=1
        while i<len(arr):
            nums1.append(arr[i])
            i+=1
        while j<len(nums2):
            nums1.append(nums2[j])
            j+=1