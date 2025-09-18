from game_pygame import run_game
from sudoku_env import Board
from utils import board_to_str
import copy
from sudoku_env import SudokuEnvironment
from solver import SudokuSolver

sample_board: Board = [
        [0,0,0,2,6,0,7,0,1],
        [6,8,0,0,7,0,0,9,0],
        [1,9,0,0,0,4,5,0,0],
        [8,2,0,1,0,0,0,4,0],
        [0,0,4,6,0,2,9,0,0],
        [0,5,0,0,0,3,0,2,8],
        [0,0,9,3,0,0,0,7,4],
        [0,4,0,0,5,0,0,3,6],
        [7,0,3,0,1,8,0,0,0]
    ]


'''
env = SudokuEnvironment(copy.deepcopy(sample_board))
solver = SudokuSolver(env)
solved = solver.solve_generator()
if hasattr(solved, '__iter__'):  # kiểm tra nếu trả về generator
    for _ in solved:
        pass
print("Sudoku board after solving:")
print(board_to_str(env.board))
'''

if __name__ == "__main__":
    run_game()
