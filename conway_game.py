import tkinter as tk
from tkinter import ttk, colorchooser
import pygame
import numpy as np

class GameSettings:
    def __init__(self):
        self.bg_color = (0, 0, 0)  # čierna farba ako RGB tuple
        self.cell_color = (255, 255, 255)  # biela farba ako RGB tuple

# Funkcia na inicializáciu mriežky s náhodnými hodnotami
def create_grid(rows, cols, randomize=True):
    if randomize:
        return np.random.choice([0, 1], (rows, cols))
    else:
        return np.zeros((rows, cols), dtype=int)

# Funkcia na pridanie preddefinovaných vzorov do mriežky
def add_pattern(grid, pattern, start_x=0, start_y=0):
    patterns = {
        "Blinker": [(0, 1), (1, 1), (2, 1)],
        "Glider": [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)],
        "Block": [(0, 0), (0, 1), (1, 0), (1, 1)],
        "Toad": [(1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3)],
        "Beacon": [(0, 0), (0, 1), (1, 0), (1, 1), (2, 2), (2, 3), (3, 2), (3, 3)],
        "Pulsar": [(1, 3), (1, 4), (1, 5), (1, 9), (1, 10), (1, 11),
                   (3, 1), (3, 6), (3, 8), (3, 13),
                   (4, 1), (4, 6), (4, 8), (4, 13),
                   (5, 1), (5, 6), (5, 8), (5, 13),
                   (6, 3), (6, 4), (6, 5), (6, 9), (6, 10), (6, 11),
                   (8, 3), (8, 4), (8, 5), (8, 9), (8, 10), (8, 11),
                   (9, 1), (9, 6), (9, 8), (9, 13),
                   (10, 1), (10, 6), (10, 8), (10, 13),
                   (11, 1), (11, 6), (11, 8), (11, 13),
                   (13, 3), (13, 4), (13, 5), (13, 9), (13, 10), (13, 11)],
        "Pentadecathlon": [(0, 2), (0, 3), (1, 1), (1, 4), (2, 2), (2, 3),
                           (3, 2), (3, 3), (4, 2), (4, 3), (5, 1), (5, 4),
                           (6, 2), (6, 3)],
        "LWSS": [(0, 1), (0, 4), (1, 0), (1, 4), (2, 4), (3, 0), (3, 3)]
    }
    for dx, dy in patterns[pattern]:
        grid[start_x + dx, start_y + dy] = 1

# Funkcia na aktualizáciu stavu mriežky podľa pravidiel hry
def update_grid(grid):
    rows, cols = grid.shape
    new_grid = grid.copy()
    for x in range(rows):
        for y in range(cols):
            neighbors = (
                grid[(x-1) % rows, (y-1) % cols] +
                grid[(x)   % rows, (y-1) % cols] +
                grid[(x+1) % rows, (y-1) % cols] +
                grid[(x-1) % rows, (y)   % cols] +
                grid[(x+1) % rows, (y)   % cols] +
                grid[(x-1) % rows, (y+1) % cols] +
                grid[(x)   % rows, (y+1) % cols] +
                grid[(x+1) % rows, (y+1) % cols]
            )
            if grid[x, y] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x, y] = 0
            else:
                if neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

# Funkcia na vykreslenie mriežky do okna
def draw_grid(screen, grid, cell_size, settings):
    screen.fill(settings.bg_color)
    rows, cols = grid.shape
    for x in range(rows):
        for y in range(cols):
            if grid[x, y] == 1:
                rect = pygame.Rect(y * cell_size[0], x * cell_size[1], cell_size[0], cell_size[1])
                pygame.draw.rect(screen, settings.cell_color, rect)
    pygame.display.flip()

# Hlavná funkcia pre spustenie hry
def run_game(rows, cols, speed, randomize, full_screen, resolution, settings, pattern=None):
    pygame.init()
    if full_screen:
        screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(resolution)
    
    pygame.display.set_caption("Conway's Game of Life")
    cell_size = (resolution[0] // cols, resolution[1] // rows)
    grid = create_grid(rows, cols, randomize)

    if pattern and pattern != "None":
        add_pattern(grid, pattern, rows // 2, cols // 2)
    
    running = True
    paused = False
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    grid = create_grid(rows, cols, randomize=True)
                    if pattern and pattern != "None":
                        add_pattern(grid, pattern, rows // 2, cols // 2)
                elif event.key == pygame.K_c:
                    grid = create_grid(rows, cols, randomize=False)
                elif event.key == pygame.K_ESCAPE:
                    pygame.display.quit()
                    return
        if not paused:
            grid = update_grid(grid)
        draw_grid(screen, grid, cell_size, settings)
        clock.tick(speed)

    pygame.quit()

# Funkcia na spustenie GUI
def start_gui(settings):
    def choose_bg_color():
        color = colorchooser.askcolor()[1]
        if color:
            bg_color_button.config(bg=color)
            settings.bg_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    def choose_cell_color():
        color = colorchooser.askcolor()[1]
        if color:
            cell_color_button.config(bg=color)
            settings.cell_color = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))

    def start_game():
        rows = int(rows_entry.get())
        cols = int(cols_entry.get())
        speed = int(speed_entry.get())
        randomize = randomize_var.get() == 1
        full_screen = fullscreen_var.get() == 1
        resolution = tuple(map(int, resolution_entry.get().split('x')))
        pattern = pattern_var.get()
        run_game(rows, cols, speed, randomize, full_screen, resolution, settings, pattern)

    root = tk.Tk()
    root.title("Conway's Game of Life Settings")

    # Zistenie aktuálneho rozlíšenia obrazovky
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    default_resolution = f"{screen_width}x{screen_height}"
    # Výpočet predvoleného počtu riadkov a stĺpcov (1/10 rozlíšenia)
    default_rows = screen_height // 10
    default_cols = screen_width // 10
    
    mainframe = ttk.Frame(root, padding="10 10 10 10")
    mainframe.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    rows_label = ttk.Label(mainframe, text="Number of Rows:")
    rows_label.grid(column=1, row=1, sticky=tk.W)
    rows_entry = ttk.Entry(mainframe, width=7)
    rows_entry.grid(column=2, row=1, sticky=(tk.W, tk.E))
    rows_entry.insert(0, str(default_rows))
    
    cols_label = ttk.Label(mainframe, text="Number of Columns:")
    cols_label.grid(column=1, row=2, sticky=tk.W)
    cols_entry = ttk.Entry(mainframe, width=7)
    cols_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
    cols_entry.insert(0, str(default_cols))
    
    speed_label = ttk.Label(mainframe, text="Speed (FPS):")
    speed_label.grid(column=1, row=3, sticky=tk.W)
    speed_entry = ttk.Entry(mainframe, width=7)
    speed_entry.grid(column=2, row=3, sticky=(tk.W, tk.E))
    speed_entry.insert(0, "10")
    
    randomize_var = tk.IntVar(value=1)
    randomize_checkbutton = ttk.Checkbutton(mainframe, text="Randomize Grid", variable=randomize_var)
    randomize_checkbutton.grid(column=1, row=4, columnspan=2, sticky=tk.W)
    
    fullscreen_var = tk.IntVar()
    fullscreen_checkbutton = ttk.Checkbutton(mainframe, text="Fullscreen Mode", variable=fullscreen_var)
    fullscreen_checkbutton.grid(column=1, row=5, columnspan=2, sticky=tk.W)
    
    bg_color_label = ttk.Label(mainframe, text="Background Color:")
    bg_color_label.grid(column=1, row=6, sticky=tk.W)
    bg_color_entry = ttk.Entry(mainframe, width=15)
    bg_color_entry.grid(column=2, row=6, sticky=(tk.W, tk.E))
    bg_color_entry.insert(0, "#000000")
    bg_color_button = tk.Button(mainframe, text="Choose Color", command=choose_bg_color)
    bg_color_button.grid(column=3, row=6, sticky=tk.W)
    
    cell_color_label = ttk.Label(mainframe, text="Cell Color:")
    cell_color_label.grid(column=1, row=7, sticky=tk.W)
    cell_color_entry = ttk.Entry(mainframe, width=15)
    cell_color_entry.grid(column=2, row=7, sticky=(tk.W, tk.E))
    cell_color_entry.insert(0, "#FFFFFF")
    cell_color_button = tk.Button(mainframe, text="Choose Color", command=choose_cell_color)
    cell_color_button.grid(column=3, row=7, sticky=tk.W)
    
    resolution_label = ttk.Label(mainframe, text="Resolution (e.g., 1920x1080):")
    resolution_label.grid(column=1, row=8, sticky=tk.W)
    resolution_entry = ttk.Entry(mainframe, width=15)
    resolution_entry.grid(column=2, row=8, sticky=(tk.W, tk.E))
    resolution_entry.insert(0, default_resolution)
    
    pattern_label = ttk.Label(mainframe, text="Initial Pattern:")
    pattern_label.grid(column=1, row=9, sticky=tk.W)
    pattern_var = tk.StringVar()
    pattern_combobox = ttk.Combobox(mainframe, textvariable=pattern_var)
    pattern_combobox['values'] = ("None", "Blinker", "Glider", "Block", "Toad", "Beacon", "Pulsar", "Pentadecathlon", "LWSS")
    pattern_combobox.grid(column=2, row=9, sticky=(tk.W, tk.E))
    pattern_combobox.current(0)
    
    start_button = ttk.Button(mainframe, text="Start Game", command=start_game)
    start_button.grid(column=2, row=10, sticky=tk.W)
    
    for child in mainframe.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()

if __name__ == "__main__":
    settings = GameSettings()
    start_gui(settings)
