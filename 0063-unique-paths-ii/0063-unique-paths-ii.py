class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:return 0
        r=len(obstacleGrid)
        c=len(obstacleGrid[0])
        if obstacleGrid[r-1][c-1]==1:return 0
        if obstacleGrid[0][0]==1:return 0
        obstacles=set()
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j]==1:
                    obstacles.add((i,j))
        if r==1 and len(obstacles)>0:
            return 0
        for i in range(r):
            if (i,0) in obstacles:
                break
            obstacleGrid[i][0]=1
        for i in range(c):
            if (0,i) in obstacles:
                break
            obstacleGrid[0][i]=1
        for i in range(1,r):
            for j in range(1,c):
                if (i,j) in obstacles:
                    continue
                elif (i,j-1) in obstacles and (i-1,j) in obstacles:
                    obstacleGrid[i][j]=0
                elif (i,j-1) in obstacles:
                    obstacleGrid[i][j]=obstacleGrid[i-1][j]
                elif (i-1,j) in obstacles:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j]=obstacleGrid[i][j-1]+obstacleGrid[i-1][j]

        return(obstacleGrid[r-1][c-1])
