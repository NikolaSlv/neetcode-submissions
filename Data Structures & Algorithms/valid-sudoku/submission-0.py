class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seenRow = set()
        seenCol = set()

        for i in range(9):
            seenRow.clear()
            seenCol.clear()
            for j in range(9):
                if board[i][j] in seenRow or board[j][i] in seenCol:
                    return False
                if board[i][j] != '.':
                    seenRow.add(board[i][j])
                if board[j][i] != '.':
                    seenCol.add(board[j][i])
        
        seenSq = set()

        for i in range(3):
            for j in range(3):
                seenSq.clear()
                for ii in range(3 * i, 3 * (i + 1)):
                    for jj in range(3 * j, 3 * (j + 1)):
                        if board[ii][jj] in seenSq:
                            return False
                        if board[ii][jj] != '.':
                            seenSq.add(board[ii][jj])
        
        return True