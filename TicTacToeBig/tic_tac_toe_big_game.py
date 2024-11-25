"""
tic_tac_toe_big_game module. Defines tic tac toe big 
methods and validations based on GameTwoAgents.
In tic tac toe big, the board is a 9x9 board 
where every 3x3 sub board is a tixc tactoe game
player a movement in the subboard will determine the board for the next player
if that board is not available due to win or board full, all subboards are available
win the player making a subboards line in the bit board
"""
from game_two_agents import GameTwoAgents
from ttt_move import TTTMove, EMPTY
from TicTacToeBig.players.ttt_big_agent_player import TTTBigAgentPlayer

class TicTacToeBigGame(GameTwoAgents):
    """
    tic_tac_toe_big_game module. Defines tic tac toe big 
    methods and validations based on GameTwoAgents.
    In tic tac toe big, the board is a 9x9 board 
    where every 3x3 sub board is a tixc tactoe game
    player a movement in the subboard will determine the board for the next player
    if that board is not available due to win or board full, all subboards are available
    win the player making a subboards line in the bit board
    """
    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.board_dimentions = 3
        self.game_name = "TicTacToeBigGame"
        self.game_state = [[ [ [ [EMPTY] * 3 for i in range(3) ]
                              for i in range(3) ] for i in range(3) ],
                          [ [EMPTY] * 3 for i in range(3) ],
                          None]
        self.turns_limit = 81
        print(self.game_name)

    def print_game_state(self):
        """print_game_state method. Print the tic tac toe big game state. """
        print("big board state:")
        for i in range(3):
            print(self.game_state[1][i])
        print("boards state:")
        print("_  1  2  3     4  5  6     7  8  9")
        for i in range(3):
            for j in range(3):
                print(3*i + j + 1, end=" ")
                for k in range(3):
                    print(self.game_state[0][i][k][j], end=" | ")
                print("")
            print("-------------------------------------")
        if self.game_state[2]:
            print(f"last move: {self.game_state[2].x + 1} {self.game_state[2].y + 1}")

    def print_board_state(self, board):
        """print_board_state method. Print a specific subboard state."""
        for i in range(3):
            print(board[i])

    def set_move(self, player: TTTBigAgentPlayer)-> bool:
        """set_move method. Run the player decide method."""
        player.set_game_state(self.game_state.copy())
        move: TTTMove = player.decide_move()
        move_status = self.play_move(player, move)
        if not move_status:
            print("invalid Move, lose")
        return move_status

    def play_move(self, player: TTTBigAgentPlayer, move: TTTMove)-> bool:
        """play_move method. Upate the game state based on the player move."""
        try:
            bx, by, x, y = move.x // 3, move.y // 3, move.x % 3, move.y % 3
            if self.game_state[1][bx][by] != EMPTY or self.game_state[0][bx][by][x][y] != EMPTY:
                raise ValueError("cell block/already used")

            self.game_state[0][bx][by][x][y] = move.value
            if self.check_board_win(self.game_state[0][bx][by], player.turn):
                self.game_state[1][bx][by] = move.value
            self.game_state[2] = move
        except ValueError:
            return False
        return True

    def check_board_win(self, board: list[list[int]], player: TTTBigAgentPlayer):
        """check_board_win method. Validate if the player won for a subboard."""
        #print("in checkBoardWin")
        #self.printBoardState(board)
        p_win = [player.value] * 3
        #print(p_win)
        #print(board[1])
        for i in range(3):
            if board[i] == p_win:
                return player
            col = []
            for j in range(3):
                col.append(board[j][i])
            if col == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(board[i][i])
            if diag == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(board[i][2-i])
            if diag == p_win:
                return player
        return None

    def check_win(self, player: TTTBigAgentPlayer):
        """check_win method. Validate if the player won."""
        #print("in checkWin")
        return self.check_board_win(self.game_state[1], player)

    def reset_state(self):
        """reset_state method. Clear game_state."""
        self.game_state = [[ [ [ [EMPTY] * 3 for i in range(3) ]
                              for i in range(3) ] for i in range(3) ],
                          [ [EMPTY] * 3 for i in range(3) ],
                          None]
