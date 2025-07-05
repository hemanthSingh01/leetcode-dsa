class Solution:
    def trap(self, height: List[int]) -> int:
        max_l=[]
        max_left=0
        for i in range(len(height)):
            max_l.append(max_left)
            max_left=max(max_left,height[i])
        max_r=[]
        max_right=0
        for i in range(len(height)-1,-1,-1):
            max_r.append(max_right)
            max_right=max(max_right,height[i])
        max_r=max_r[::-1]
        totalwater=0
        for i in range(len(height)):
            val=min(max_r[i],max_l[i])-height[i]
            if val>0:
                totalwater+=val
        return(totalwater)