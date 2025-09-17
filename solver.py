from typing import Optional, Set, Tuple, Generator
import copy
from sudoku_env import SudokuEnvironment, Coord
from utils import board_to_str

class SudokuSolver:
    def __init__(self, env: SudokuEnvironment):
        self.env = env

    def find_best_cell(self) -> Optional[Tuple[int, int, Set[int]]]: #Có thể trả về none
        best_r = -1
        best_c = -1
        best_options = None
        for r in range(9):
            for c in range(9):
                if self.env.is_empty(r, c): #tìm được ô trống
                    opts = self.env.possible_values(r, c)
                    if best_options is None or len(opts) < len(best_options):
                        best_r, best_c, best_options = r, c, opts
                        if len(best_options) == 1: #chỉ có một số có thể điền được vào ô trống
                            return (best_r, best_c, best_options)
        if best_options is None: #bài toán đã được giải
            return None
        return (best_r, best_c, best_options)

    def solve_generator(self) -> Generator[Tuple[str, int, int, int, list], None, bool]:
        found = self.find_best_cell()
        if found is None:
            return True
        r, c, options = found
        if not options:
            return False
        #Thử đặt từng giá trị có thể vào ô trống
        for val in sorted(options):
            self.env.set(r, c, val)
            #Trả về một tuple, thông báo đã đặt val vào ô
            yield ('place', r, c, val, copy.deepcopy(self.env.board))

            #Gọi đệ quy để giải các ô còn lại
            subgen = self.solve_generator()
            try:
                while True:
                    # lấy từng giá trị mà subgen tạo ra
                    yielded = next(subgen)
                    yield yielded
            except StopIteration as e:
                result = e.value

            if result:
                return True

            self.env.set(r, c, 0)
            yield ('back', r, c, 0, copy.deepcopy(self.env.board))

        return False
