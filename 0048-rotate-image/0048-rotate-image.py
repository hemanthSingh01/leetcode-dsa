class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[0])):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row=row.reverse()