from typing import List
from sudoku_env import Board


SEPARATOR = "------+-------+------"


def board_to_str(board: Board) -> str:
    lines: List[str] = []
    for r in range(9):
        parts: List[str] = []
        for c in range(9):
            if c != 0 and c % 3 == 0:
                parts.append("|")
            parts.append(str(board[r][c]) if board[r][c] != 0 else ".")
        lines.append(" ".join(parts))
        if r % 3 == 2 and r != 8:
            lines.append(SEPARATOR)
    return "\n".join(lines)