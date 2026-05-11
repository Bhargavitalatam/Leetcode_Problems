class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ro=[[False]*9 for _ in range(9)]
        co=[[False]*9 for _ in range(9)]
        bo=[[False]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    num=ord(board[i][j])-ord('1')
                    bi=(i//3)*3+(j//3)
                    if ro[i][num] or co[j][num] or bo[bi][num]:
                        return False
                    ro[i][num]=co[j][num]=bo[bi][num]=True
        return True
        