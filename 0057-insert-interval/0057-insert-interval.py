class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])
        mergedIntervals=[intervals[0]]
        for i in range(1,len(intervals)):
            current=intervals[i]
            prev=mergedIntervals[-1]
            if current[0]<=prev[1]:
                prev[1]=max(prev[1],current[1])
            else:
                mergedIntervals.append(intervals[i])
        return mergedIntervals