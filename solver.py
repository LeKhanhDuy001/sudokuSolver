from typing import Optional, Set, Tuple
from sudoku_env import SudokuEnvironment, Coord
from utils import board_to_str


class SudokuSolver:
    def __init__(self, env: SudokuEnvironment):
        self.env = env
        self.step = 0

    def find_best_cell(self) -> Optional[Tuple[int, int, Set[int]]]:
        best_r = -1
        best_c = -1
        best_options = None
        for r in range(9):
            for c in range(9):
                if self.env.is_empty(r, c):
                    opts = self.env.possible_values(r, c)
                    if best_options is None or len(opts) < len(best_options):
                        best_r, best_c, best_options = r, c, opts
                        if len(best_options) == 1:
                            return (best_r, best_c, best_options)
        if best_options is None:
            return None
        return (best_r, best_c, best_options)

    def _print_step(self, kind: str, r: int, c: int, val: int) -> None:
    # kind: 'place' or 'backtrack'
        self.step += 1
        action = 'place' if kind == 'place' else 'back'
        val_str = str(val) if val != 0 else '.'
        msg = f"\nStep {self.step:05d}: {action:9s} val={val_str:>2s} at ({r},{c})\n" + board_to_str(self.env.board)
        print(msg, flush=True)

    def solve(self) -> bool:
        found = self.find_best_cell()
        if found is None:
            return True # no empty cell

        r, c, options = found
        # if no possible options -> fail
        if not options:
            return False

        for val in sorted(options):
            self.env.set(r, c, val)
            self._print_step('place', r, c, val)

            if self.solve():
                return True


        # backtrack
            self.env.set(r, c, 0)
            self._print_step('backtrack', r, c, 0)


        return False