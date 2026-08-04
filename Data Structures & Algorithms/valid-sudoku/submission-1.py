class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dups = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dups:
                    return False
                dups.add(board[i][j])
            dups.clear()
        for j in range(len(board[0])):
            for i in range(len(board)):
                if board[i][j] == ".":
                    continue
                if board[i][j] in dups:
                    return False
                dups.add(board[i][j])
            dups.clear()
        
        for start_i in range(0, 9, 3):
            for start_j in range(0, 9, 3):
                for i in range(start_i, start_i + 3):
                    for j in range(start_j, start_j + 3):
                        if board[i][j] == ".":
                            continue
                        if board[i][j] in dups:
                            return False
                        dups.add(board[i][j])
                dups.clear()

        

        return True