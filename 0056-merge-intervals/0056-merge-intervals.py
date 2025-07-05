class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged=[intervals[0]]
        for i in range(1,len(intervals)):
            current=intervals[i]
            prev=merged[-1]
            if current[0]<=prev[1]:
                prev[1]=max(prev[1],current[1])
            else:
                merged.append(intervals[i])
        return merged
