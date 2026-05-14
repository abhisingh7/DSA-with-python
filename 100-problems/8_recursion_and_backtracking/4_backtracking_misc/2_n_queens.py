# LeetCode - 51 - N Queens (Hard)

# https://leetcode.com/problems/n-queens/

# Problem -
# Place N queens on an N×N chessboard such that no two queens attack each other.
# A queen in chess can attack in 3 ways:

# Same row ↔️
# Same column ↕️
# Same diagonal ↗️↙️

# For example - 4 Queens on 4×4 board
# . Q . .
# . . . Q
# Q . . .
# . . Q .

# Every queen is safe — no two queens share the same row, column, or diagonal.

def solve_n_queens(n):
    result = []
    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    board = [["."] * n for _ in range(n)]

    def solve(row):
        # base case
        if row == n:
            result.append(["".join(row) for row in board])
            return

        for col in range(n):
            # check if safe
            if col not in cols and \
               (row-col) not in diag1 and \
               (row+col) not in diag2:

                # place queen
                # 1. Place queen on board
                board[row][col] = "Q"
                # 2. Mark column as used
                cols.add(col)
                # 3. Mark ↘ diagonal as used
                diag1.add(row-col)
                # 4. Mark ↗ diagonal as used
                diag2.add(row + col)

                # go deeper
                solve(row + 1)

                # GO BACK - remove queen
                # undo 1 - remove queen from board
                board[row][col] = "."  # reset back to empty
                # undo 2 - unmark column
                cols.remove(col)
                # undo 3 - unmark ↘ diagonal
                diag1.remove(row-col)
                # undo 4 - unmark ↗ diagonal
                diag2.remove(row+col)

    solve(0)
    return result

# Test
print(solve_n_queens(4))