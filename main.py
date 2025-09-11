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


if __name__ == '__main__':
    env = SudokuEnvironment(sample)
    solver = SudokuSolver(env)

    print("Bảng Sudoku ban đầu:")
    print(board_to_str(sample))

    solved = solver.solve()

    if solved:
        print('\n✅ Giải xong Sudoku:')
        print(board_to_str(env.board))
    else:
        print('\n❌ Không tìm được lời giải.')