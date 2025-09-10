# Conway's Game of Life (Terminal)

This is a simple Python implementation of Conway's Game of Life that runs in your terminal.

## Features

- Terminal-based simulation of Conway's Game of Life
- Customizable grid size and number of generations (via command-line arguments)
- Random initial board state

## Requirements

- Python 3.x

## Usage

1. **Clone this repository or download the script.**

2. **Run the game:**

   ```bash
   python conway_game_of_life.py
   ```

   By default, this will display a 20x40 board for 100 generations.

3. **Customize grid size and generations:**

   ```
   python conway_game_of_life.py <rows> <cols> <generations>
   ```

   Example (30 rows, 60 columns, 200 generations):

   ```
   python conway_game_of_life.py 30 60 200
   ```

4. **Stop the simulation at any time with** `Ctrl+C`.

## How It Works

- **Alive cells** are displayed as `█`.
- **Dead cells** are displayed as spaces.
- Each generation is computed based on the classic Game of Life rules.

## Customization

You can easily modify the script to use a custom initial pattern by editing the `create_board` function.

## License

This project is provided for educational purposes.
