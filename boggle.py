from string import ascii_uppercase
from random import choice

def make_grid(width, height):
    # creates grid that holds all tiles for boggle game
    return {(row, col): choice(ascii_uppercase) 
        for row in range(height)
        for col in range(width)
    }
    
def neighbours_of_position(coords):
    # get neighbours of a given position
    row = coords[0]
    col = coords[1]
    
    # assign neighbours, top left to top right
    top_left = (row -1, col -1)
    top_center = (row -1, col )
    top_right = (row -1, col +1)
    
    # assign neighbours, left and right
    left = (row, col -1)
    right = (row, col +1)
    
    # assign neighbours, bottom left to right
    bottom_left = (row +1, col -1)
    bottom_center = (row +1, col)
    bottom_right = (row +1, col +1)
    
    return [ 
        top_left, top_center, top_right,
        left, right,
        bottom_left, bottom_center, bottom_right]
        
def all_grid_neighbours(grid):
    # get all neighbours for each position of the grid
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    # Add all of the letters on the path to a string
    return ''.join([grid[p] for p in path])


def search(grid, dictionary):
    # Search thrugh the paths to locate words by matching
    # strings to words in a dictionary
    neighbours = all_grid_neighbours(grid)
    paths = []

    def do_search(path):
        word = path_to_word(grid, path)
        if word in dictionary:
            paths.append(path)
        for next_pos in neighbours[path[-1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
    
    for position in grid:
        do_search([position])
    
    words = []
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)


def get_dictionary(dictionary_file):
    
    # Load dictionary file
    with open(dictionary_file) as f:
        return [w.strip().upper() for w in f]