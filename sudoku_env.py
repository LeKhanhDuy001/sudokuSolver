from typing import List, Tuple, Set

Board = List[List[int]]
Coord = Tuple[int, int]

class SudokuEnvironment:
    def __init__(self, board: Board):
        if len(board) != 9 or any(len(row) != 9 for row in board):
            raise ValueError("Board phải là 9x9.")
        self.board = [row[:] for row in board]

    def get(self, r: int, c: int) -> int:
        return self.board[r][c]

    def set(self, r: int, c: int, val: int) -> None:
        self.board[r][c] = val

    def is_empty(self, r: int, c: int) -> bool:
        return self.board[r][c] == 0

    def possible_values(self, r: int, c: int) -> Set[int]: #loại bỏ các số đã xuất hiện trong cùng một hàng, cột, khối
        if not self.is_empty(r, c):
            return set()

        nums = set(range(1, 10))
        nums -= set(self.board[r])
        nums -= {self.board[i][c] for i in range(9)}
        br, bc = (r // 3) * 3, (c // 3) * 3
        nums -= {self.board[i][j] for i in range(br, br + 3) for j in range(bc, bc + 3)}

        return nums
