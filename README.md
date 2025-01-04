Conway's Game of Life
A web-based implementation of Conway's Game of Life featuring an interactive graphical user interface for configuring initial parameters and patterns.

Features
Configurable Grid Size and Speed: Adjust the number of rows and columns, as well as the simulation speed (frames per second).
Randomized Initial Grid, Specific Patterns, or Symmetric Patterns: Choose between a random setup, select predefined patterns, or generate symmetric patterns by specifying a square size.
Adjustable Colors for Background, Cells, and Grid: Customize the background color, live cell color, and grid lines color.
Resizable Canvas: Set the width and height of the game canvas to fit your display.
Symmetric Patterns: Generate symmetric patterns by specifying the size of a square, which is then mirrored across both x and y axes, resulting in four symmetric squares centered on the canvas.
Blurred Background with Equations: A visually appealing background featuring mathematical equations with a blur effect.
Random Cell Colors: Option to render each live cell with a randomly generated color for dynamic visuals.
Creative Mode: Manually toggle the state of individual cells by clicking on them within the grid, allowing for custom configurations.
Installation
No installation is required. Simply download or clone the repository and open the index.html file in your web browser.

Usage
Open the Application:

Open the index.html file in your preferred web browser.
Configure Game Settings:

Click the "Configure" button to reveal the settings panel.

Number of Rows: Set the number of rows in the grid.

Number of Columns: Set the number of columns in the grid.

Speed (FPS): Set the simulation speed in frames per second.

Random Cell Colors: Enable this option to render each live cell with a randomly generated color.

Symmetric Patterns: Check this box to generate symmetric patterns.

Square Size: Specify the size of the square used for generating symmetric patterns.

Grid Color: Select the color of the grid lines.

Background Color: Choose the background color of the canvas.

Cell Color: Select the color for live cells (used if Random Cell Colors is disabled).

Initial Pattern: Choose from a list of predefined patterns or select "None" for a random grid.

Creative Mode: Enable this mode to manually toggle the state of individual cells by clicking on them.

Canvas Width (px): Set the width of the game canvas in pixels.

Canvas Height (px): Set the height of the game canvas in pixels.

Apply Settings:

After configuring your settings, click the "Setup Grid" button to initialize the grid based on your selections.
Run the Simulation:

Click the "Start Simulation" button to begin the evolution of the grid according to Conway's rules.

Pause Simulation: Click the "Pause" button to temporarily halt the simulation.

Reset Grid: Click the "Reset Grid" button to clear the current grid and start fresh.

Save Map: Click the "Save Map" button to download the current grid configuration as a JSON file.

Load Map: Click the "Load Map" button to upload a previously saved JSON file and restore a grid configuration.

Creative Mode:

If Creative Mode is enabled, click on individual cells within the grid to toggle their state between alive and dead, allowing for custom configurations.
Controls
Start Simulation: Begin the simulation of Conway's Game of Life.
Pause: Temporarily pause the simulation.
Reset Grid: Clear the current grid and start with a fresh setup.
Save Map: Download the current grid configuration as a JSON file.
Load Map: Upload a JSON file to load a saved grid configuration.
Configure: Open or close the settings panel to adjust game parameters.
Examples
Symmetric Patterns
When Symmetric Patterns is enabled and a Square Size is specified, the application generates a random pattern within the defined square and mirrors it symmetrically across both the x and y axes, resulting in four symmetric squares centered on the canvas.

Random Cell Colors
Enabling Random Cell Colors assigns each live cell a unique, randomly generated color, adding dynamic visual diversity to the simulation.

Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue.

License
This project is licensed under the MIT License.
