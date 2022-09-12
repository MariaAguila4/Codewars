#validate row
def isRowValid(board, row_num):
    return len(set(board[row_num])) == 9

#validate column
def isColValid(board, col_num):
    col = [item[col_num] for item in board]
    return len(set(col)) == 9

#validate cell
def isCelValid(board, cel_row, cel_col):
    vals = board[cel_row][cel_col: cel_col+3]
    vals.extend(board[cel_row+1] [cel_col: cel_col+3])
    vals.extend(board[cel_row+2] [cel_col: cel_col+3])
    return len(set(vals)) == 9

def done_or_not(board): #board[i][j]
    for i in range(0, 9):
        if not isRowValid(board,i):
            return 'Try again!'
        if not isColValid(board,i):
            return 'Try again!'
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if not isCelValid(board, i, j):
                return 'Try again!'
    return 'Finished!'

  # return 'Finished!'
  # ..
  # or return 'Try again!'


print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                  , [4, 9, 8, 2, 6, 1, 3, 7, 5]
                  , [7, 5, 6, 3, 8, 4, 2, 1, 9]
                  , [6, 4, 3, 1, 5, 8, 7, 9, 2]
                  , [5, 2, 1, 7, 9, 3, 8, 4, 6]
                  , [9, 8, 7, 4, 2, 6, 5, 3, 1]
                  , [2, 1, 4, 9, 3, 5, 6, 8, 7]
                  , [3, 6, 5, 8, 1, 7, 9, 2, 4]
                  , [8, 7, 9, 6, 4, 2, 1, 5, 3]]))

print(done_or_not([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                        ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))