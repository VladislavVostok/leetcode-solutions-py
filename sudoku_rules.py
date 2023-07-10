from typing import List

def isValidSudoku(board: List[List[str]]) -> bool:
    # Horizontal rule
    for i in range(9):
        for j in range(9-1):
            for j_ in range(1 + j, 9):
                if (board[i][j] == board[i][j_]) and board[i][j] != ".":
                    return False
    # Vertical rule
    for j in range(9):
        for i in range(9-1):
            for i_ in range(1+i, 9):
                if (board[i][j] == board[i_][j]) and board[i][j] != ".":
                    return False

    # Square rule transforn in line
    sud_boxed = []

    for li,line in enumerate(board):
        for box in range(3):
            if not li % 3: sud_boxed.append([])    # build a new box every 3 lines
            sud_boxed[box + li//3*3].extend(line[box*3:box*3+3])

    for i in range(9):
        for j in range(9-1):
            for j_ in range(1 + j, 9):
                if (sud_boxed[i][j] == sud_boxed[i][j_]) and sud_boxed[i][j] != ".":
                    return False

    return True

if __name__ == "__main__":

    board_true =    [
                        ["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"],
                    ]

    board_false =   [
                        ["8","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"],
                    ]

    print(isValidSudoku(board_true))

    