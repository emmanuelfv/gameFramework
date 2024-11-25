"""agent_player module. Player with basic random logic over valid movements."""
import random
from ttt_move import MoveValue, TTTMove, EMPTY

class AgentPlayer:
    """AgentPlayer class. Player with basic random logic over valid movements."""
    def __init__(self):
        """__init__ method."""
        self.last_opponent_move = None
        self.valid_move_list = None
        self.game_state = None
        self.updatable_state = False
        self.turn = MoveValue.EMPTY
        self.opponent_turn = MoveValue.EMPTY
        self.name = "AgentPlayer"
        print("player agent set")

    def get_name(self) -> str:
        """get_name method. get name."""
        return self.name

    def set_turn(self, turn):
        """set_turn method. set turn."""
        self.turn = turn
        self.opponent_turn = MoveValue.PLAYER1 if MoveValue.PLAYER1 != turn else MoveValue.PLAYER2

    def set_opponent_move(self, mode: TTTMove):
        """set_opponent_move method. Setter"""
        self.last_opponent_move = mode

    def set_valid_moves(self, valid_move_list = None):
        """set_valid_moves method. Set valid_move_list with all of valid moves."""
        if valid_move_list is not None:
            self.valid_move_list = valid_move_list
        else:
            self.valid_move_list = self.create_move_list_from_state()

    def create_move_list_from_state(self):
        """set_valid_moves method. Create a list all of valid moves."""
        #print(f"function createMoveListFromState not created yet")
        x_len, y_len = len(self.game_state), len(self.game_state[0])
        new_valid_move_list = []
        for x in range(x_len):
            for y in range(y_len):
                if self.game_state[x][y] == EMPTY:
                    new_valid_move_list.append([x,y])
        return new_valid_move_list

    def set_game_state(self, game_state):
        """set_game_state method. update the state from the game"""
        self.game_state = game_state
        self.set_valid_moves()

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        position = random.choice(self.valid_move_list)
        move: TTTMove = TTTMove(position[0], position[1], self.turn.value)
        return move
