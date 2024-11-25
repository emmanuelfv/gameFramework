"""best_move_player module. Player which check the best inmediate move."""
import random
from TicTacToe.players.agent_player import AgentPlayer
from ttt_move import TTTMove, PLAYER1, PLAYER2

class BestMovePlayer(AgentPlayer):
    """BestMovePlayer class. Player which check the best inmediate move."""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("best move agent player set")
        self.name = "best move agent"

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        scores = list(zip([self.score_move(x, y) for x, y in self.valid_move_list],
                          self.valid_move_list))
        max_value = max(scores)[0]
        #print(f"scores: {scores} {max_value}")
        max_choices = [key for value, key in scores if value == max_value]
        choice = random.choice(max_choices)
        move: TTTMove = TTTMove(choice[0], choice[1], self.turn.value)
        return move

    ### internal methods: ###

    def score_move(self, x, y):
        """score_move method. Return a value based on the moment score."""
        next_state = self.get_next_state(x, y)
        #print(f"next_state: {next_state}")
        return self.get_heuristic(next_state)

    def get_next_state(self, x, y):
        """get_next_state method. Makes a copy of the current state 
        and make a change based on the possible movement."""
        next_state = [ self.game_state[i].copy() for i in range(3) ]
        next_state[x][y] = self.turn.value
        return next_state

    def get_heuristic(self, state):
        """get_heuristic method. Implement the logic to obtain the score
        This is based on the win posibility rate againt lose posibilty rate.
        Only current moment is cosidered."""
        lines_list = self.get_line_list(state)
        #print(f"lines_list: {lines_list}")
        #print(f"self.turn.value: {self.turn.value}")
        player_value = str(self.turn.value)
        oponent_value = str(PLAYER2) if self.turn.value == PLAYER1 else str(PLAYER1)
        good_points = [10**(2*s.count(player_value)) for s in lines_list
                       if player_value in s and oponent_value not in s]
        bad_points = [10**(2*s.count(oponent_value) + 1) for s in lines_list
                      if oponent_value in s and player_value not in s]
        total = sum(good_points) - sum(bad_points)
        #print(f"total: {total}")
        return total

    def get_line_list(self, state):
        """get_line_list method. Return the list of all possible lines
        which can be formed"""
        lines_list = []
        for i in range(3):
            lines_list.append("".join(map(str, state[i])))
            col = []
            for j in range(3):
                col.append(str(state[j][i]))
            lines_list.append("".join(col))
        diag = []
        for i in range(3):
            diag.append(str(state[i][i]))
        lines_list.append("".join(diag))
        diag = []
        for i in range(3):
            diag.append(str(state[i][2-i]))
        lines_list.append("".join(diag))
        return lines_list
