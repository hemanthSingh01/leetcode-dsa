class Solution:
    def search(self, arr: List[int], target: int) -> int:
        start=0
        end=len(arr)-1
        ans=-1
        while start<=end:
             mid=start+(end-start)//2
             if mid<end and arr[mid]>arr[mid+1]:
                    ans=mid
                    break
             if start<mid and arr[mid]<arr[mid-1]:
                    ans=mid-1
                    break
             if arr[start]>=arr[mid]:
                 end=mid-1
             else:
                start=mid+1
        start=0
        end=ans
        #search in right half.
        while start<=end:
            mid=start+(end-start)//2
            if arr[mid]==target:
                return(mid)
                break
            elif arr[mid]>target:
                     end=mid-1
            else:
                start=mid+1
        start=ans+1
        end=len(arr)-1
        #search in left half.
        while start<=end:
             mid=start+(end-start)//2
             if arr[mid]==target:
                return(mid)
                break
             elif arr[mid]>target:
                end=mid-1
             else:
                start=mid+1
        return -1   
