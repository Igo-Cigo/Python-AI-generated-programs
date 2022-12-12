# promt used: make a game of life in python

# Game of Life

# Define the initial state of the grid
grid = [
    [1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

# Define the number of generations to simulate
generations = 10

# Define a function to count the number of live neighbors for a cell
def count_live_neighbors(grid, row, col):
    # Initialize a counter for the number of live neighbors
    live_neighbors = 0
    
    # Loop through the 3x3 grid centered around the cell
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            # Check if the current cell is live and not the center cell
            if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1 and (i != row or j != col):
                live_neighbors += 1
    
    # Return the number of live neighbors
    return live_neighbors

# Define a function to update the grid based on the rules of the Game of Life
def update_grid(grid):
    # Create a new grid to store the next generation
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    # Loop through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Count the number of live neighbors for the current cell
            live_neighbors = count_live_neighbors(grid, i, j)
            
            # Apply the rules of the Game of Life to update the cell
            if grid[i][j] == 1 and live_neighbors in [2, 3]:
                new_grid[i][j] = 1
            elif grid[i][j] == 0 and live_neighbors == 3:
                new_grid[i][j] = 1
            else:
                new_grid[i][j] = 0
    
    # Return the updated grid
    return new_grid

# Simulate the Game of Life for the specified number of generations
for i in range(generations):
    # Print the current generation
    print(f"Generation {i}:")
    for row in grid:
        print(row)
    print()
    
    # Update the grid to the next generation
    grid = update_grid(grid)

# Print the final generation
print(f"Generation {generations}:")
for row in grid:
    print(row)
