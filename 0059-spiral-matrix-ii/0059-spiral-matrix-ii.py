class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[]
        for i in range(1,(n**2)+1):
            matrix.append(i)
        l=[[0]*n for i in range(n)]
        up,down,right,left=0,1,2,3
        Up_wall=0
        Down_wall=n
        Right_wall=n
        Left_wall=-1
        direction=right
        i,j,k=0,0,0
        while k<len(matrix):
             if direction==right:
                while j<Right_wall:
                    l[i][j]=matrix[k]
                    j+=1
                    k+=1
                i,j=i+1,j-1
                Right_wall-=1
                direction=down
             elif direction==down:
                while i<Down_wall:
                    l[i][j]=matrix[k]
                    i+=1
                    k+=1
                i,j=i-1,j-1
                Down_wall-=1
                direction=left
             elif direction==left:
                while j>Left_wall:
                    l[i][j]=matrix[k]
                    k+=1
                    j-=1
                i,j=i-1,j+1
                Left_wall+=1
                direction=up
             else:
                while i>Up_wall:
                    l[i][j]=matrix[k]
                    k+=1
                    i-=1
                i,j=i+1,j+1
                Up_wall+=1
                direction=right
        return l        

            