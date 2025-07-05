class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # For rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] != ".":
                    s.add(board[i][j])

        # For columns
        for i in range(9):
            s2 = set()
            for j in range(9):
                if board[j][i] in s2:
                    return False
                elif board[j][i] != ".":
                    s2.add(board[j][i])

        # For boxes
        Boxes = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
        for i, j in Boxes:
            s3 = set()  # Create a new set for each box
            for row in range(i, i + 3):
                for column in range(j, j + 3):
                    if board[row][column] in s3:
                        return False
                    elif board[row][column] != ".":
                        s3.add(board[row][column])
        
        return True
