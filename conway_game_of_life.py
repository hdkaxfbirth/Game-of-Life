import os
import time
import random
import sys

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Prints the game board to the terminal."""
    for row in board:
        print("".join(['█' if cell else ' ' for cell in row]))

def get_neighbors(board, x, y):
    """Returns the number of alive neighbors for a cell at (x, y)."""
    neighbors = 0
    rows, cols = len(board), len(board[0])
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                neighbors += board[nx][ny]
    return neighbors

def next_generation(board):
    """Computes the next generation of the board."""
    rows, cols = len(board), len(board[0])
    new_board = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbors = get_neighbors(board, i, j)
            if board[i][j]:
                new_board[i][j] = 1 if neighbors in [2, 3] else 0
            else:
                new_board[i][j] = 1 if neighbors == 3 else 0
    return new_board

def create_board(rows, cols, randomize=True):
    """Creates a new game board."""
    if randomize:
        return [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    else:
        return [[0 for _ in range(cols)] for _ in range(rows)]

def main():
    rows, cols = 20, 40
    generations = 100
    delay = 0.1

    # Optionally, allow command line arguments for custom size
    if len(sys.argv) >= 3:
        rows = int(sys.argv[1])
        cols = int(sys.argv[2])
    if len(sys.argv) >= 4:
        generations = int(sys.argv[3])

    board = create_board(rows, cols, randomize=True)

    try:
        for gen in range(generations):
            clear_screen()
            print(f"Generation {gen + 1}")
            print_board(board)
            board = next_generation(board)
            time.sleep(delay)
    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
