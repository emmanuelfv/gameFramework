"""agent_player module. Player with basic random logic over valid movements."""
import random

from game2048.cursor_move import MoveValue

class AgentPlayer:
    """AgentPlayer class. Player with basic random logic over valid movements."""
    def __init__(self):
        """__init__ method."""
        self.valid_move_list = None
        self.game_state = None
        self.updatable_state = False
        self.name = "2048AgentPlayer"
        print("player agent set")

    def get_name(self) -> str:
        """get_name method. get name."""
        return self.name

    def set_valid_moves(self, valid_move_list = None):
        """set_valid_moves method. Set valid_move_list with all of valid moves."""
        if valid_move_list is not None:
            self.valid_move_list = valid_move_list
        else:
            self.valid_move_list = self.create_move_list_from_state()

    def create_move_list_from_state(self):
        """set_valid_moves method. Create a list all of valid moves."""
        new_valid_move_list = [MoveValue.UP, MoveValue.DOWN, MoveValue.LEFT, MoveValue.RIGHT]
        return new_valid_move_list

    def set_game_state(self, game_state):
        """set_game_state method. update the state from the game"""
        self.game_state = game_state
        self.set_valid_moves()

    def decide_move(self):
        """decide_move method. Implement the strategy and return a movement"""
        direction = random.choice(self.valid_move_list)
        return direction
