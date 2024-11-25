"""ttt_big_agent_player module. Player with basic random logic over valid movements."""
import random
from ttt_move import MoveValue, TTTMove, EMPTY

class TTTBigAgentPlayer:
    """TTBigPlayerAgent module. Player with basic random logic over valid movements."""
    def __init__(self):
        """__init__ method."""
        self.last_opponent_move = None
        self.valid_move_list = None
        self.game_state = None
        self.updatable_state = False
        self.turn = MoveValue.EMPTY
        self.name = "TTTBigPlayerAgent"
        print("TTTBig player agent set")

    def get_name(self) -> str:
        """get_name method. get name."""
        return self.name

    def set_turn(self, turn):
        """set_turn method. set turn."""
        self.turn = turn

    def set_opponent_move(self, move: TTTMove):
        """set_opponent_move method. Setter"""
        self.last_opponent_move = move

    def set_valid_moves(self, valid_move_list = None):
        """set_valid_moves method. Set valid_move_list with all of valid moves."""
        if valid_move_list is not None:
            self.valid_move_list = valid_move_list
        else:
            self.valid_move_list = self.create_move_list_from_state()

    def create_move_list_from_state(self):
        """set_valid_moves method. Create a list all of valid moves."""
        #print("in createMoveListFromState")
        enemy_move: TTTMove = self.game_state[2]
        #print(f"enemyMove {enemyMove}")
        self.set_opponent_move(enemy_move)
        big_board = self.game_state[1]

        all_board_flag = enemy_move is None
        if enemy_move:
            x, y = enemy_move.x % 3, enemy_move.y % 3
            if big_board[x][y] != EMPTY:
                all_board_flag = True

        #print(f"allBoardFlag {allBoardFlag}")
        new_valid_move_list = []
        for i in range(3):
            for j in range(3):
                if all_board_flag:
                    for k in range(3):
                        for ii in range(3):
                            if self.game_state[0][i][j][k][ii] == EMPTY:
                                new_valid_move_list.append([3*i + k, 3*j + ii])
                else:
                    if self.game_state[0][x][y][i][j] == EMPTY:
                        new_valid_move_list.append([3*x + i, 3*y + j])
        #print(newValidMoveList)
        return new_valid_move_list

    def set_game_state(self, game_state):
        """set_game_state method. update the state from the game"""
        self.game_state = game_state
        self.set_valid_moves()

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        position = random.choice(self.valid_move_list)
        move: TTTMove = TTTMove(position[0], position[1], self.turn.value)
        #time.sleep(3)
        return move
