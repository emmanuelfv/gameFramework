"""
ttt_move module. Contains movement information especifically for tic-tac-toe game.
"""

from dataclasses import dataclass
from enum import Enum

class MoveValue(Enum):
    """MoveValue Class. Enum for cell possible values"""
    EMPTY = 1
    PLAYER1 = 2
    PLAYER2 = 3

@dataclass
class TTTMove:
    """TTTMove Class. Cell relevant information"""
    x: int
    y: int
    value: int

EMPTY = MoveValue.EMPTY.value
PLAYER1 = MoveValue.PLAYER1.value
PLAYER2 = MoveValue.PLAYER2.value
