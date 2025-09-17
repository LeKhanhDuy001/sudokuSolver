import pygame
import sys
import time
import copy
from typing import List, Tuple

from sudoku_env import SudokuEnvironment
from solver import SudokuSolver
from puzzles import sample, easy, hard
from utils import board_to_str

# -------------------- Config & UI constants --------------------
PRESETS = {
    'sample': sample,
    'easy': easy,
    'hard': hard,
}

WIDTH, HEIGHT = 900, 760
GRID_ORIGIN = (20, 20)
CELL_SIZE = 70
BOARD_SIZE = CELL_SIZE * 9
FPS = 60

# Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
LIGHT_BLUE = (173,216,230)
RED = (220,50,50)

# -------------------- UI Button helper --------------------
class Button:
    def __init__(self, rect, text, font):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = font

    def draw(self, surf):
        pygame.draw.rect(surf, GRAY, self.rect)
        pygame.draw.rect(surf, BLACK, self.rect, 2)
        txt = self.font.render(self.text, True, BLACK)
        surf.blit(txt, txt.get_rect(center=self.rect.center))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

# -------------------- Main game function --------------------
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Sudoku Visualizer')
    font = pygame.font.SysFont('consolas', 36)
    small_font = pygame.font.SysFont('consolas', 18)
    clock = pygame.time.Clock()

    # -------------------- State init --------------------
    current_preset = 'hard'
    init_board = copy.deepcopy(PRESETS[current_preset])
    env = SudokuEnvironment(init_board)
    working_board = copy.deepcopy(env.board)  # displayed board
    selected = (0,0)
    solver_gen = None
    solving = False
    last_step_time = 0.0
    step_delay = 0.05
    message = ''
    start_time = None         # thêm biến theo dõi thời gian
    elapsed_time = 0.0

    # Buttons
    btn_load = Button((BOARD_SIZE + 40, 40, 120, 34), 'Load', small_font)
    btn_reset = Button((BOARD_SIZE + 40, 86, 120, 34), 'Reset', small_font)
    btn_solve = Button((BOARD_SIZE + 40, 132, 120, 34), 'Solve', small_font)
    btn_pause = Button((BOARD_SIZE + 40, 178, 120, 34), 'Pause', small_font)
    btn_step = Button((BOARD_SIZE + 40, 224, 120, 34), 'Step', small_font)
    btn_speed_up = Button((BOARD_SIZE + 40, 270, 56, 30), '+', small_font)
    btn_speed_down = Button((BOARD_SIZE + 104, 270, 56, 30), '-', small_font)
    btn_preset = Button((BOARD_SIZE + 40, 320, 120, 34), 'Preset', small_font)

    fixed_cells = [[cell != 0 for cell in row] for row in init_board]

    def reset_to_init():
        nonlocal env, working_board, solver_gen, solving, fixed_cells, message, init_board, start_time, elapsed_time
        env = SudokuEnvironment(copy.deepcopy(init_board))
        working_board = copy.deepcopy(env.board)
        fixed_cells = [[cell != 0 for cell in row] for row in init_board]
        solver_gen = None
        solving = False
        message = ''
        start_time = None
        elapsed_time = 0.0

    reset_to_init()

    # -------------------- Draw helpers --------------------
    def draw_board(surf, board, selected_cell=None):
        ox, oy = GRID_ORIGIN
        pygame.draw.rect(surf, WHITE, (ox-2, oy-2, BOARD_SIZE+4, BOARD_SIZE+4))

        for r in range(9):
            for c in range(9):
                x = ox + c * CELL_SIZE
                y = oy + r * CELL_SIZE
                cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
                if selected_cell == (r,c):
                    pygame.draw.rect(surf, LIGHT_BLUE, cell_rect)
                pygame.draw.rect(surf, BLACK, cell_rect, 1)

                val = board[r][c]
                if val != 0:
                    color = (50,50,50) if fixed_cells[r][c] else BLACK
                    txt = font.render(str(val), True, color)
                    surf.blit(txt, txt.get_rect(center=cell_rect.center))

        # thick lines
        for i in range(10):
            lw = 3 if i % 3 == 0 else 1
            pygame.draw.line(surf, BLACK, (ox + i*CELL_SIZE, oy), (ox + i*CELL_SIZE, oy + BOARD_SIZE), lw)
            pygame.draw.line(surf, BLACK, (ox, oy + i*CELL_SIZE), (ox + BOARD_SIZE, oy + i*CELL_SIZE), lw)

    # -------------------- Main loop --------------------
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos
                ox, oy = GRID_ORIGIN
                if ox <= mx <= ox + BOARD_SIZE and oy <= my <= oy + BOARD_SIZE:
                    c = (mx - ox) // CELL_SIZE
                    r = (my - oy) // CELL_SIZE
                    selected = (r, c)
                else:
                    if btn_reset.clicked((mx,my)):
                        init_board = copy.deepcopy(PRESETS[current_preset])
                        reset_to_init()
                        message = 'Reset.'
                    elif btn_preset.clicked((mx,my)):
                        keys = list(PRESETS.keys())
                        i = keys.index(current_preset)
                        current_preset = keys[(i+1) % len(keys)]
                        init_board = copy.deepcopy(PRESETS[current_preset])
                        reset_to_init()
                        message = f'Preset: {current_preset}'
                    elif btn_solve.clicked((mx,my)):
                        if not solving:
                            solver_gen = SudokuSolver(SudokuEnvironment(copy.deepcopy(working_board))).solve_generator()
                            solving = True
                            message = 'Solving...'
                            start_time = time.perf_counter()   # bắt đầu đếm giờ
                            elapsed_time = 0.0
                    elif btn_pause.clicked((mx,my)):
                        solving = not solving
                        message = 'Paused.' if not solving else 'Resumed.'
                    elif btn_step.clicked((mx,my)):
                        if solver_gen is None:
                            solver_gen = SudokuSolver(SudokuEnvironment(copy.deepcopy(working_board))).solve_generator()
                        try:
                            action, r, c, val, board_snap = next(solver_gen)
                            working_board = board_snap
                            message = f'{action} {val} at ({r},{c})'
                        except StopIteration:
                            solving = False
                            solver_gen = None
                            elapsed_time = time.perf_counter() - start_time if start_time else elapsed_time
                            message = 'Done.'
                    elif btn_speed_up.clicked((mx,my)):
                        step_delay = max(0.005, step_delay - 0.01)
                        message = f'Speed: {step_delay:.3f}s/step'
                    elif btn_speed_down.clicked((mx,my)):
                        step_delay = min(1.0, step_delay + 0.01)
                        message = f'Speed: {step_delay:.3f}s/step'

            elif event.type == pygame.KEYDOWN:
                r, c = selected
                if event.key in (pygame.K_BACKSPACE, pygame.K_DELETE):
                    if not fixed_cells[r][c]:
                        working_board[r][c] = 0
                elif event.unicode and event.unicode.isdigit():
                    d = int(event.unicode)
                    if 1 <= d <= 9 and not fixed_cells[r][c]:
                        working_board[r][c] = d

        # solver stepping
        if solving and solver_gen is not None:
            now = time.perf_counter()
            elapsed_time = now - start_time if start_time else elapsed_time
            if now - last_step_time >= step_delay:
                try:
                    action, r, c, val, board_snap = next(solver_gen)
                    working_board = board_snap
                except StopIteration:
                    solving = False
                    solver_gen = None
                    elapsed_time = now - start_time if start_time else elapsed_time
                    message = 'Finished.'

        # render
        screen.fill((240,240,240))
        draw_board(screen, working_board, selected_cell=selected)

        # draw buttons
        for b in [btn_load, btn_reset, btn_solve, btn_pause, btn_step, btn_speed_up, btn_speed_down, btn_preset]:
            b.draw(screen)

        # message + time
        screen.blit(small_font.render(f'Message: {message}', True, RED), (BOARD_SIZE+40, 420))
        screen.blit(small_font.render(f'Time: {elapsed_time:.2f} s', True, RED), (BOARD_SIZE+40, 450))

        pygame.display.flip()

    pygame.quit()
    sys.exit()
