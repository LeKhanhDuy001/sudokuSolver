import time
from sudoku_env import SudokuEnvironment
from solver import SudokuSolver
from utils import board_to_str

# Ví dụ Sudoku (0 = ô trống)
sample = [
[5, 3, 0, 0, 7, 0, 0, 0, 0],
[6, 0, 0, 1, 9, 5, 0, 0, 0],
[0, 9, 8, 0, 0, 0, 0, 6, 0],

[8, 0, 0, 0, 6, 0, 0, 0, 3],
[4, 0, 0, 8, 0, 3, 0, 0, 1],
[7, 0, 0, 0, 2, 0, 0, 0, 6],

[0, 6, 0, 0, 0, 0, 2, 8, 0],
[0, 0, 0, 4, 1, 9, 0, 0, 5],
[0, 0, 0, 0, 8, 0, 0, 7, 9],
]

easy = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],

    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],

    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0],
]

medium = [
    [0, 2, 0, 6, 0, 8, 0, 0, 0],
    [5, 8, 0, 0, 0, 9, 7, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0],

    [3, 7, 0, 0, 0, 0, 5, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 0, 8, 0, 0, 0, 0, 1, 3],

    [0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 9, 8, 0, 0, 0, 3, 6],
    [0, 0, 0, 3, 0, 6, 0, 9, 0],
]

hard = [
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 1, 0, 9, 0, 0, 0, 0],

    [0, 0, 0, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 7, 0, 8, 0, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 0],

    [0, 0, 0, 0, 2, 0, 6, 0, 0],
    [0, 0, 0, 8, 0, 0, 0, 0, 0],
    [4, 3, 0, 0, 0, 0, 0, 0, 0],
]



if __name__ == '__main__':

    initState = hard
    env = SudokuEnvironment(initState)
    solver = SudokuSolver(env)

    print("Bảng Sudoku ban đầu:")
    print(board_to_str(initState))

    start = time.perf_counter()
    solved = solver.solve()
    elapsed = time.perf_counter() - start

    if solved:
        print('\n✅ Giải xong Sudoku:')
        print(f"Thời gian giải: {elapsed}s")
        print(board_to_str(env.board))
    else:
        print('\n❌ Không tìm được lời giải.')