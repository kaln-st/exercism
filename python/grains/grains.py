"""

Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares.
Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

Write code that calculates:

- The number of grains on a given square
- The total number of grains on the chessboard

"""

SQUARE_START = 1
SQUARE_END = 64

def square(number):

    """
    
    Calculate the number of grains on a given square.

    Parameters:
        number (int): a positive number

    Return:
        int: the number of grains on a given square
    
    """

    if number < SQUARE_START or number > SQUARE_END:
        raise ValueError("square must be between 1 and 64")

    return 2 ** (number - 1)


def total():

    """
    
    Calculate the total number of grains on the chessboard.

    Parameters: None

    Return:
        int: the total number of grains on the chessboard
    
    """
    
    return 2 ** SQUARE_END - 1
