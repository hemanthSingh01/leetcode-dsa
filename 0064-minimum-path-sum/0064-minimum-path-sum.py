class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        heap=[[grid[0][0],0,0]]
        directions=[(1,0),(0,1)]
        min_cost = [[float('inf')] * n for _ in range(m)]
        min_cost[0][0] = grid[0][0]
        while heap:
            cost,r,c=heapq.heappop(heap)
            if (r,c)==(m-1,n-1):
                return(cost)
            for dx,dy in directions:
                nx=dx+r
                ny=dy+c
                if 0<=nx<m and 0<=ny<n:
                    new_cost = cost + grid[nx][ny]
                    if new_cost < min_cost[nx][ny]:
                        min_cost[nx][ny] = new_cost
                        heapq.heappush(heap, [new_cost, nx, ny])
                    
