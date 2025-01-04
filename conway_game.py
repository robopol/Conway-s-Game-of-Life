<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Conway's Game of Life</title>
    <style>
        /* Dark Mode Styling */
        body {
            font-family: Arial, sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            margin: 0;
            display: flex;
            flex-direction: column;
            min-height: 100vh; /* Full viewport height */
            position: relative; 
        }
        /* Main Container */
        .container {
            flex: 1; /* Take up remaining space */
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            box-sizing: border-box;
            margin-top: 20px; /* To prevent overlap with language selector if any */
        }
        /* Controls Section */
        #controls {
            width: 100%;
            max-width: 800px;
            background-color: #1e1e1e;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            margin-bottom: 20px;
        }
        /* Control Buttons */
        #controlButtons {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-start;
            margin-bottom: 20px;
        }
        #controlButtons button {
            margin: 5px;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            background-color: #3a3a3a;
            color: #e0e0e0;
            cursor: pointer;
            transition: background-color 0.3s;
            font-size: 14px;
        }
        #controlButtons button:hover {
            background-color: #505050;
        }
        #controlButtons button:active {
            background-color: #666666;
        }
        /* Settings Panel */
        #settingsPanel {
            display: none; /* Hidden by default */
            margin-top: 20px;
        }
        #settingsPanel div {
            margin: 10px 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        label {
            flex: 1;
            font-weight: bold;
            margin-right: 10px;
        }
        input[type="number"], input[type="color"], select {
            flex: 2;
            padding: 5px;
            border: 1px solid #333;
            border-radius: 4px;
            background-color: #2c2c2c;
            color: #e0e0e0;
        }
        input[type="checkbox"] {
            transform: scale(1.2);
            margin-left: 10px;
        }
        /* Canvas Styling */
        #gameCanvas {
            border: 1px solid #333;
            background-color: #000000;
            border-radius: 8px;
            max-width: 100%;
            height: auto;
            display: block;
        }
        /* Footer Styling */
        footer {
            text-align: center;
            padding: 10px 0;
            background-color: #1e1e1e;
            color: #888888;
            font-size: 14px;
        }
        /* Description Styling */
        #description {
            max-width: 800px;
            margin-top: 20px;
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
            display: flex;
            align-items: flex-start;
        }
        #description img {
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 8px;
            margin-right: 20px;
        }
        #descriptionContent {
            flex: 1;
        }
        /* Responsive Layout */
        @media (max-width: 800px) {
            #controls div {
                flex-direction: column;
                align-items: flex-start;
            }
            label {
                margin-bottom: 5px;
            }
            input[type="number"], input[type="color"], select {
                width: 100%;
            }
            #controlButtons button {
                width: 100%;
                margin: 5px 0;
            }
            #description {
                flex-direction: column;
                align-items: center;
            }
            #description img {
                margin: 0 0 20px 0;
            }
            #descriptionContent {
                width: 100%;
            }
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Conway's Game of Life</h1>

        <div id="controls">
            <div id="controlButtons">
                <button id="setupGrid">Setup Grid</button>
                <button id="startSimulation">Start Simulation</button>
                <button id="pauseSimulation">Stop</button>
                <button id="resetGrid">Reset Grid</button>
                <button id="saveGrid">Save Map</button>
                <button id="loadGrid">Load Map</button>
                <button id="configure">Configure</button>
                <input type="file" id="fileInput" accept=".json" style="display:none;">
            </div>

            <div id="settingsPanel">
                <div>
                    <label for="rows">Number of Rows:</label>
                    <input type="number" id="rows" value="50" min="10" max="200">
                </div>
                <div>
                    <label for="cols">Number of Columns:</label>
                    <input type="number" id="cols" value="50" min="10" max="200">
                </div>
                <div>
                    <label for="speed">Speed (FPS):</label>
                    <input type="number" id="speed" value="10" min="1" max="60">
                </div>
                <div>
                    <label for="bgColor">Background Color:</label>
                    <input type="color" id="bgColor" value="#000000">
                </div>
                <div>
                    <label for="cellColor">Cell Color:</label>
                    <input type="color" id="cellColor" value="#FFFFFF">
                </div>
                <div>
                    <label for="randomColors">Random Cell Colors:</label>
                    <input type="checkbox" id="randomColors">
                </div>
                <div>
                    <label for="symmetricPatterns">Symmetric Patterns:</label>
                    <input type="checkbox" id="symmetricPatterns">
                </div>
                <div id="symmetricSettings" style="display: none;">
                    <label for="squareSize">Square Size:</label>
                    <input type="number" id="squareSize" value="10" min="1" max="100">
                </div>
                <div>
                    <label for="gridColor">Grid Color:</label>
                    <input type="color" id="gridColor" value="#282828">
                </div>
                <div>
                    <label for="pattern">Initial Pattern:</label>
                    <select id="pattern">
                        <option value="None">None</option>
                        <option value="Blinker">Blinker</option>
                        <option value="Glider">Glider</option>
                        <option value="Block">Block</option>
                        <option value="Toad">Toad</option>
                        <option value="Beacon">Beacon</option>
                        <option value="Pulsar">Pulsar</option>
                        <option value="Pentadecathlon">Pentadecathlon</option>
                        <option value="LWSS">LWSS</option>
                    </select>
                </div>
                <div>
                    <label for="creativeMode">Creative Mode:</label>
                    <input type="checkbox" id="creativeMode">
                </div>
                <div>
                    <label for="canvasWidth">Canvas Width (px):</label>
                    <input type="number" id="canvasWidth" value="800" min="200" max="1920">
                </div>
                <div>
                    <label for="canvasHeight">Canvas Height (px):</label>
                    <input type="number" id="canvasHeight" value="800" min="200" max="1080">
                </div>
            </div>
        </div>

        <canvas id="gameCanvas" width="800" height="800"></canvas>

        <div id="description">
            <img src="conway.jpg" alt="Conway Portrait">
            <div id="descriptionContent">
                <p id="descText">Conway's Game of Life is a cellular automaton devised by the mathematician John Horton Conway. It consists of a grid of cells that can live, die, or multiply based on a set of rules. Use the control buttons above to manage the simulation. Click the "Configure" button to access and adjust the game settings, including the number of rows and columns, simulation speed, colors, and initial patterns. After making any changes to the settings, be sure to click the "Setup Grid" button to apply the new configurations. Once the grid is set up, you can start, pause, reset the simulation, or save and load grid configurations as needed.</p>
                <p id="instrText"><strong>How to Use Conway's Game of Life:</strong></p>
                <ol>
                    <li><strong>Configure Settings:</strong> Click the "Configure" button to reveal the game settings panel. Here, you can adjust the number of rows and columns, set the simulation speed (FPS), choose colors for the background, cells, and grid, select an initial pattern, enable Creative Mode, and adjust the canvas size.</li>
                    <li><strong>Symmetric Patterns:</strong> If you want to generate symmetric patterns, check the "Symmetric Patterns" box and specify the desired square size. This will create a random pattern in the specified square and mirror it symmetrically across both the x and y axes, resulting in four symmetric squares centered on the canvas.</li>
                    <li><strong>Setup Grid:</strong> After configuring your settings, click the "Setup Grid" button to initialize the grid based on your chosen parameters. This step is crucial to apply any changes you made in the settings.</li>
                    <li><strong>Start Simulation:</strong> Click the "Start Simulation" button to begin the evolution of the grid according to Conway's rules.</li>
                    <li><strong>Pause Simulation:</strong> At any point, you can pause the simulation by clicking the "Pause" button.</li>
                    <li><strong>Reset Grid:</strong> To clear the current grid and start fresh, click the "Reset Grid" button.</li>
                    <li><strong>Save and Load Configurations:</strong> Use the "Save Map" button to download your current grid configuration as a JSON file. You can later load this configuration by clicking the "Load Map" button and selecting your saved file.</li>
                    <li><strong>Creative Mode:</strong> If you enable Creative Mode, you can manually toggle the state of individual cells by clicking on them within the grid. This allows for custom configurations beyond the predefined patterns.</li>
                    <li><strong>Random Cell Colors:</strong> If you enable the "Random Cell Colors" option in the Configure settings, each live cell will be rendered with a randomly generated color. If disabled, all live cells will use the color specified in the "Cell Color" setting.</li>
                    <li><strong>Important:</strong> Whenever you change any settings, always remember to click the "Setup Grid" button to ensure they are applied correctly before starting the simulation.</li>
                </ol>
                <p>Enjoy experimenting with different patterns and settings to explore the fascinating behaviors of Conway's Game of Life!</p>
            </div>
        </div>
    </div>

    <footer>
        <span id="footerText">© Robert Polák 2024</span>
    </footer>

    <script>
        // Game Settings
        const settings = {
            bgColor: '#000000',
            cellColor: '#FFFFFF',
            gridColor: '#282828',
            rows: 50,
            cols: 50,
            speed: 10,
            pattern: 'None',
            creativeMode: false,
            randomCellColors: false,
            symmetricPatterns: false,
            squareSize: 10,
            canvasWidth: 800,
            canvasHeight: 800
        };

        // Grid Initialization
        let grid = createGrid(settings.rows, settings.cols);
        let canvas = document.getElementById('gameCanvas');
        let ctx = canvas.getContext('2d');
        let cellWidth, cellHeight;
        let animationId;
        let isRunning = false;

        // Patterns Definitions
        const patterns = {
            "Blinker": [[0,1], [1,1], [2,1]],
            "Glider": [[0,1], [1,2], [2,0], [2,1], [2,2]],
            "Block": [[0,0], [0,1], [1,0], [1,1]],
            "Toad": [[1,2], [1,3], [1,4], [2,1], [2,2], [2,3]],
            "Beacon": [[0,0], [0,1], [1,0], [1,1], [2,2], [2,3], [3,2], [3,3]],
            "Pulsar": [
                [1,3], [1,4], [1,5], [1,9], [1,10], [1,11],
                [3,1], [3,6], [3,8], [3,13],
                [4,1], [4,6], [4,8], [4,13],
                [5,1], [5,6], [5,8], [5,13],
                [6,3], [6,4], [6,5], [6,9], [6,10], [6,11],
                [8,3], [8,4], [8,5], [8,9], [8,10], [8,11],
                [9,1], [9,6], [9,8], [9,13],
                [10,1], [10,6], [10,8], [10,13],
                [11,1], [11,6], [11,8], [11,13],
                [13,3], [13,4], [13,5], [13,9], [13,10], [13,11]
            ],
            "Pentadecathlon": [
                [0,2], [0,3], [1,1], [1,4],
                [2,2], [2,3], [3,2], [3,3],
                [4,2], [4,3], [5,1], [5,4],
                [6,2], [6,3]
            ],
            "LWSS": [
                [0,1], [0,4],
                [1,0], [1,4],
                [2,4],
                [3,0], [3,3]
            ]
        };

        // Create Empty Grid
        function createGrid(rows, cols, randomize=false) {
            let newGrid = [];
            for (let i = 0; i < rows; i++) {
                let row = [];
                for (let j = 0; j < cols; j++) {
                    row.push(randomize ? (Math.random() < 0.3 ? 1 : 0) : 0); // Slightly lower density
                }
                newGrid.push(row);
            }
            return newGrid;
        }

        // Add Pattern to Grid
        function addPattern(grid, pattern, startX, startY) {
            if (!patterns[pattern]) {
                alert(`Pattern "${pattern}" does not exist.`);
                return;
            }
            patterns[pattern].forEach(([dx, dy]) => {
                let x = startX + dx;
                let y = startY + dy;
                if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
                    grid[x][y] = 1;
                }
            });
        }

        // Generate Symmetric Patterns
        function generateSymmetricPatterns(grid, squareSize) {
            const rows = grid.length;
            const cols = grid[0].length;
            const centerX = Math.floor(rows / 2);
            const centerY = Math.floor(cols / 2);

            // Define starting points for the four squares
            const topLeftX = centerX - squareSize;
            const topLeftY = centerY - squareSize;
            const topRightX = centerX - squareSize;
            const topRightY = centerY;
            const bottomLeftX = centerX;
            const bottomLeftY = centerY - squareSize;
            const bottomRightX = centerX;
            const bottomRightY = centerY;

            // Generate random pattern for the top-left square
            let square = createGrid(squareSize, squareSize, false);
            for (let i = 0; i < squareSize; i++) {
                for (let j = 0; j < squareSize; j++) {
                    square[i][j] = Math.random() < 0.3 ? 1 : 0;
                }
            }

            // Mirror the square across the x-axis
            let mirroredX = createGrid(squareSize, squareSize, false);
            for (let i = 0; i < squareSize; i++) {
                for (let j = 0; j < squareSize; j++) {
                    mirroredX[i][j] = square[squareSize - 1 - i][j];
                }
            }

            // Mirror the square across the y-axis
            let mirroredY = createGrid(squareSize, squareSize, false);
            for (let i = 0; i < squareSize; i++) {
                for (let j = 0; j < squareSize; j++) {
                    mirroredY[i][j] = square[i][squareSize - 1 - j];
                }
            }

            // Mirror the square across both axes
            let mirroredXY = createGrid(squareSize, squareSize, false);
            for (let i = 0; i < squareSize; i++) {
                for (let j = 0; j < squareSize; j++) {
                    mirroredXY[i][j] = square[squareSize - 1 - i][squareSize - 1 - j];
                }
            }

            // Place the four squares onto the grid
            placeSquare(grid, square, topLeftX, topLeftY);
            placeSquare(grid, mirroredX, topRightX, topRightY);
            placeSquare(grid, mirroredY, bottomLeftX, bottomLeftY);
            placeSquare(grid, mirroredXY, bottomRightX, bottomRightY);
        }

        // Helper function to place a square onto the grid
        function placeSquare(grid, square, startX, startY) {
            for (let i = 0; i < square.length; i++) {
                for (let j = 0; j < square[0].length; j++) {
                    let x = startX + i;
                    let y = startY + j;
                    if (x >= 0 && x < grid.length && y >= 0 && y < grid[0].length) {
                        grid[x][y] = square[i][j];
                    }
                }
            }
        }

        // Update Grid Based on Rules (Finite Grid)
        function updateGrid(grid) {
            const rows = grid.length;
            const cols = grid[0].length;
            const newGrid = createGrid(rows, cols, false);

            for (let x = 0; x < rows; x++) {
                for (let y = 0; y < cols; y++) {
                    let neighbors = 0;
                    for (let i = -1; i <=1; i++) {
                        for (let j = -1; j <=1; j++) {
                            if (i === 0 && j === 0) continue;
                            let ni = x + i;
                            let nj = y + j;
                            if (ni >= 0 && ni < rows && nj >= 0 && nj < cols) {
                                neighbors += grid[ni][nj];
                            }
                        }
                    }
                    if (grid[x][y] === 1) {
                        if (neighbors === 2 || neighbors === 3) {
                            newGrid[x][y] = 1;
                        }
                    } else {
                        if (neighbors === 3) {
                            newGrid[x][y] = 1;
                        }
                    }
                }
            }
            return newGrid;
        }

        // Draw Grid on Canvas
        function drawGrid() {
            ctx.fillStyle = settings.bgColor;
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            cellWidth = canvas.width / settings.cols;
            cellHeight = canvas.height / settings.rows;

            for (let x = 0; x < settings.rows; x++) {
                for (let y = 0; y < settings.cols; y++) {
                    if (grid[x][y] === 1) {
                        if (settings.randomCellColors) {
                            ctx.fillStyle = getRandomColor();
                        } else {
                            ctx.fillStyle = settings.cellColor;
                        }
                        ctx.fillRect(y * cellWidth, x * cellHeight, cellWidth, cellHeight);
                    }
                    ctx.strokeStyle = settings.gridColor;
                    ctx.strokeRect(y * cellWidth, x * cellHeight, cellWidth, cellHeight);
                }
            }
        }

        // Generate Random Color in Hex Format
        function getRandomColor() {
            const letters = '0123456789ABCDEF';
            let color = '#';
            for (let i = 0; i < 6; i++) {
                color += letters[Math.floor(Math.random() * 16)];
            }
            return color;
        }

        // Simulation Loop
        function simulate() {
            if (!isRunning) return;
            grid = updateGrid(grid);
            drawGrid();
            animationId = setTimeout(() => {
                requestAnimationFrame(simulate);
            }, 1000 / settings.speed);
        }

        // Start Simulation
        function startSimulation() {
            if (!isRunning) {
                isRunning = true;
                simulate();
            }
        }

        // Pause Simulation
        function pauseSimulation() {
            isRunning = false;
            clearTimeout(animationId);
        }

        // Reset Grid
        function resetGrid() {
            pauseSimulation();
            grid = createGrid(settings.rows, settings.cols, false); // Empty grid
            drawGrid();
        }

        // Setup Grid Based on Settings
        function setupGrid() {
            pauseSimulation();
            // Update Settings
            settings.rows = parseInt(document.getElementById('rows').value);
            settings.cols = parseInt(document.getElementById('cols').value);
            settings.speed = parseInt(document.getElementById('speed').value);
            settings.bgColor = document.getElementById('bgColor').value;
            settings.cellColor = document.getElementById('cellColor').value;
            settings.randomCellColors = document.getElementById('randomColors').checked;
            settings.symmetricPatterns = document.getElementById('symmetricPatterns').checked;
            settings.squareSize = parseInt(document.getElementById('squareSize').value);
            settings.gridColor = document.getElementById('gridColor').value;
            settings.pattern = document.getElementById('pattern').value;
            settings.creativeMode = document.getElementById('creativeMode').checked;
            settings.canvasWidth = parseInt(document.getElementById('canvasWidth').value);
            settings.canvasHeight = parseInt(document.getElementById('canvasHeight').value);

            // Resize Canvas
            canvas.width = settings.canvasWidth;
            canvas.height = settings.canvasHeight;

            // Create Grid
            if (settings.creativeMode) {
                // Preserve the current grid; do not reset
                // Optionally, clear the grid if desired
                // Here, we preserve the current grid
            } else if (settings.symmetricPatterns) {
                grid = createGrid(settings.rows, settings.cols, false); // Empty grid
                generateSymmetricPatterns(grid, settings.squareSize);
            } else if (settings.pattern !== 'None') {
                grid = createGrid(settings.rows, settings.cols, false); // Empty grid
                addPattern(grid, settings.pattern, Math.floor(settings.rows / 2) - 5, Math.floor(settings.cols / 2) - 5); // Adjusted start position
            } else {
                grid = createGrid(settings.rows, settings.cols, true); // Random grid
            }
            drawGrid();
        }

        // Toggle Cell State in Creative Mode
        function toggleCell(event) {
            if (!settings.creativeMode) return;
            const rect = canvas.getBoundingClientRect();
            const x = event.clientY - rect.top;
            const y = event.clientX - rect.left;
            const row = Math.floor(x / cellHeight);
            const col = Math.floor(y / cellWidth);
            if (row >= 0 && row < settings.rows && col >= 0 && col < settings.cols) {
                grid[row][col] = grid[row][col] ? 0 : 1;
                drawGrid();
            }
        }

        // Save Grid to JSON File
        function saveGrid() {
            const data = {
                rows: settings.rows,
                cols: settings.cols,
                grid: grid,
                canvasWidth: settings.canvasWidth,
                canvasHeight: settings.canvasHeight,
                creativeMode: settings.creativeMode,
                randomCellColors: settings.randomCellColors,
                symmetricPatterns: settings.symmetricPatterns,
                squareSize: settings.squareSize
            };
            const json = JSON.stringify(data);
            const blob = new Blob([json], {type: "application/json"});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'game_of_life_map.json';
            a.click();
            URL.revokeObjectURL(url);
        }

        // Load Grid from JSON File
        function loadGrid(event) {
            const file = event.target.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                try {
                    const data = JSON.parse(e.target.result);
                    if (data.rows && data.cols && data.grid && data.canvasWidth && data.canvasHeight) {
                        settings.rows = data.rows;
                        settings.cols = data.cols;
                        settings.canvasWidth = data.canvasWidth;
                        settings.canvasHeight = data.canvasHeight;
                        settings.creativeMode = data.creativeMode || false; // Default to false if not present
                        settings.randomCellColors = data.randomCellColors || false;
                        settings.symmetricPatterns = data.symmetricPatterns || false;
                        settings.squareSize = data.squareSize || 10;

                        document.getElementById('rows').value = data.rows;
                        document.getElementById('cols').value = data.cols;
                        document.getElementById('speed').value = data.speed || settings.speed;
                        document.getElementById('bgColor').value = data.bgColor || settings.bgColor;
                        document.getElementById('cellColor').value = data.cellColor || settings.cellColor;
                        document.getElementById('randomColors').checked = settings.randomCellColors;
                        document.getElementById('symmetricPatterns').checked = settings.symmetricPatterns;
                        document.getElementById('squareSize').value = settings.squareSize;
                        document.getElementById('gridColor').value = data.gridColor || settings.gridColor;
                        document.getElementById('pattern').value = data.pattern || settings.pattern;
                        document.getElementById('creativeMode').checked = settings.creativeMode;
                        document.getElementById('canvasWidth').value = data.canvasWidth;
                        document.getElementById('canvasHeight').value = data.canvasHeight;

                        grid = data.grid.map(row => row.slice()); // Deep copy to ensure it's a 2D array

                        // Resize Canvas
                        canvas.width = settings.canvasWidth;
                        canvas.height = settings.canvasHeight;

                        // Show or hide symmetric settings based on loaded data
                        const symmetricSettings = document.getElementById('symmetricSettings');
                        if (settings.symmetricPatterns) {
                            symmetricSettings.style.display = 'flex';
                        } else {
                            symmetricSettings.style.display = 'none';
                        }

                        drawGrid();
                    } else {
                        alert('Invalid file format.');
                    }
                } catch (err) {
                    alert('Error loading the file.');
                }
            }
            reader.readAsText(file);
        }

        // Toggle Settings Panel Visibility
        function toggleSettings() {
            const settingsPanel = document.getElementById('settingsPanel');
            if (settingsPanel.style.display === 'none' || settingsPanel.style.display === '') {
                settingsPanel.style.display = 'flex';
                settingsPanel.style.flexDirection = 'column';
            } else {
                settingsPanel.style.display = 'none';
            }
        }

        // Toggle Symmetric Settings Visibility
        function toggleSymmetricSettings() {
            const symmetricCheckbox = document.getElementById('symmetricPatterns');
            const symmetricSettings = document.getElementById('symmetricSettings');
            if (symmetricCheckbox.checked) {
                symmetricSettings.style.display = 'flex';
                symmetricSettings.style.flexDirection = 'row';
                symmetricSettings.style.alignItems = 'center';
            } else {
                symmetricSettings.style.display = 'none';
            }
        }

        // Event Listeners
        document.getElementById('configure').addEventListener('click', toggleSettings);
        document.getElementById('setupGrid').addEventListener('click', setupGrid);
        document.getElementById('startSimulation').addEventListener('click', startSimulation);
        document.getElementById('pauseSimulation').addEventListener('click', pauseSimulation);
        document.getElementById('resetGrid').addEventListener('click', resetGrid);
        document.getElementById('saveGrid').addEventListener('click', saveGrid);
        document.getElementById('loadGrid').addEventListener('click', () => {
            document.getElementById('fileInput').click();
        });
        document.getElementById('fileInput').addEventListener('change', loadGrid);
        canvas.addEventListener('click', toggleCell);
        document.getElementById('symmetricPatterns').addEventListener('change', toggleSymmetricSettings);

        // Initialize Grid
        function initialize() {
            setupGrid();
        }

        // Start Initialization on Page Load
        window.onload = initialize;
    </script>

</body>
</html>
