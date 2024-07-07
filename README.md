Conway's Game of Life
This project implements Conway's Game of Life with a graphical user interface (GUI) for setting initial parameters and patterns. The game is built using pygame for visualization and tkinter for the configuration GUI.

Features
Configurable grid size and speed
Randomized initial grid or specific patterns
Adjustable colors for background and cells
Fullscreen or windowed mode
Multiple pre-defined initial patterns:
Blinker
Glider
Block
Toad
Beacon
Pulsar
Pentadecathlon
LWSS (Lightweight Spaceship)

Install the required packages:
pip install pygame numpy
Usage
Run the script:

python conway_game.py
Configure the game settings in the GUI:

Number of Rows: Set the number of rows in the grid.
Number of Columns: Set the number of columns in the grid.
Speed (FPS): Set the speed of the simulation in frames per second.
Randomize Grid: Choose whether to start with a random grid.
Fullscreen Mode: Choose whether to run the game in fullscreen mode.
Background Color: Select the background color.
Cell Color: Select the cell color.
Resolution: Set the screen resolution (e.g., 1920x1080).
Initial Pattern: Choose from a list of pre-defined patterns.
Start the game by clicking the Start Game button.

Controls
Spacebar: Pause/Resume the game.
R: Reset the grid with a new random pattern.
C: Clear the grid.
Esc: Close the game window (returns to the GUI).
Examples


Patterns
The game includes several predefined patterns:

Blinker: A simple oscillator.
Glider: A small pattern that moves diagonally.
Block: A still life pattern.
Toad: A small oscillator.
Beacon: A larger oscillator.
Pulsar: A larger and more complex oscillator.
Pentadecathlon: An oscillator with a 15-generation period.
LWSS: A lightweight spaceship that moves across the grid.
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Pygame
NumPy
Tkinter
Feel free to adjust the content to better match your repository or personal style!
