def make_grid(width, height):
    # creates grid that holds all tiles for boggle game
    return {(row, col): ' ' for row in range(height)
        for col in range(width)
    }