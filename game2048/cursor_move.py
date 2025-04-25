"""
cursor_move module. Contains movement information especifically for game2048 game.
Valid moves are up, down, left and right.

"""

from enum import Enum

class MoveValue(Enum):
    """MoveValue Class. Enum for cell possible values"""
    EMPTY = 0
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

