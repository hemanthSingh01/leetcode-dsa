class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m=len(matrix)
        n=len(matrix[0])
        up,down,right,left=0,1,2,3
        Up_wall=0
        Down_wall=m
        Right_wall=n
        Left_wall=-1
        direction=right
        ans=[]
        i,j=0,0
        while len(ans)!=m*n:
             if direction==right:
                while j<Right_wall:
                    ans.append(matrix[i][j])
                    j+=1
                i,j=i+1,j-1
                Right_wall-=1
                direction=down
             elif direction==down:
                while i<Down_wall:
                    ans.append(matrix[i][j])
                    i+=1
                i,j=i-1,j-1
                Down_wall-=1
                direction=left
             elif direction==left:
                while j>Left_wall:
                    ans.append(matrix[i][j])
                    j-=1
                i,j=i-1,j+1
                Left_wall+=1
                direction=up
             else:
                while i>Up_wall:
                    ans.append(matrix[i][j])
                    i-=1
                i,j=i+1,j+1
                Up_wall+=1
                direction=right
        return ans
                 
            
