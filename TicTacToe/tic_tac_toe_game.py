"""tic_tac_toe_game module. Defines tic tac toe 
methods and validations based on GameTwoAgents"""
from game_two_agents import GameTwoAgents
from ttt_move import TTTMove, EMPTY
from TicTacToe.players.agent_player import AgentPlayer

class TicTacToeGame(GameTwoAgents):
    """tic_tac_toe_game class. Defines tic tac toe 
    methods and validations based on GameTwoAgents"""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.game_name = "TicTacToeGame"
        self.game_state = [ [EMPTY] * 3 for i in range(3) ]
        self.turns_limit = 9
        print(self.game_name)

    def print_game_state(self):
        """print_game_state method. Print the tic tac toe game state. """
        print("board state:")
        for i in range(3):
            print(self.game_state[i])

    def set_move(self, player: AgentPlayer)-> bool:
        """set_move method. Run the player decide method."""
        player.set_game_state(self.game_state.copy())
        move: TTTMove = player.decide_move()
        move_status = self.play_move(move)
        if not move_status:
            print("invalid Move, lose")
        return move_status

    def play_move(self, move: TTTMove)-> bool:
        """play_move method. Upate the game state based on the player move."""
        if 0 <= move.x < 3 and 0 <= move.y < 3 and self.game_state[move.x][move.y] == EMPTY:
            self.game_state[move.x][move.y] = move.value
            return True
        return False

    def check_win(self, player):
        """check_win method. Validate if the player won."""
        p_win = [player.value] * 3
        for i in range(3):
            if self.game_state[i] == p_win:
                return player
            col = []
            for j in range(3):
                col.append(self.game_state[j][i])
            if col == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(self.game_state[i][i])
            if diag == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(self.game_state[i][2-i])
            if diag == p_win:
                return player
        return None


    def reset_state(self):
        """reset_state method. Clear game_state."""
        self.game_state = [ [EMPTY] * 3 for i in range(3) ]
