"""
minimax_player module. Player which check all steps forward.
define 1 point for winning, -1 for loosing and 0 for draw.
choose the opponent minimun score as it's option.
choose the best player score as the move.
perfect method but computationally slow.
"""
import random
from TicTacToe.players.agent_player import AgentPlayer
from ttt_move import MoveValue, TTTMove, PLAYER1, PLAYER2

class MinimaxPlayer(AgentPlayer):
    """
    minimax_player module. Player which check all steps forward.
    define 1 point for winning, -1 for loosing and 0 for draw.
    choose the opponent minimun score as it's option.
    choose the best player score as the move.
    perfect method but computationally slow.
    """
    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("best move agent player set")
        self.name = "minimax agent"
        self.cached_state = {}

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        raw_scores = [self.score_move(x, y) for x, y in self.valid_move_list]
        scores = list(zip(raw_scores, self.valid_move_list))
        max_value = max(scores)[0]
        #print(f"scores: {scores} {max_value}")
        max_choices = [move_pair for value, move_pair in scores if value == max_value]
        choice = random.choice(max_choices)
        move: TTTMove = TTTMove(choice[0], choice[1], self.turn.value)
        return move

    ### internal methods: ###

    def score_move(self, x, y):
        """score_move method. Return a value based on the moment score."""
        next_state = self.get_next_state(self.game_state, x, y)
        #print(f"next_state: {next_state}")
        return self.get_heuristic(next_state)

    def get_next_state(self, state, x, y, opponent=False):
        """get_next_state method. Makes a copy of the current state 
        and make a change based on the possible movement."""
        next_state = [ state[i].copy() for i in range(3) ]
        next_state[x][y] = self.turn.value if not opponent else self.opponent_turn.value
        return next_state

    def get_heuristic(self, state):
        """get_heuristic method. Calls calculate_position_value to obtain the score.
        the score is cached as per state."""
        cached_value, found = self.get_cached_state(state)
        if found:
            return cached_value

        pos_value = self.calculate_position_value(state)

        self.put_state_in_cache(state, pos_value)
        return pos_value

    def calculate_position_value(self, state):
        """calculate_position_value method. Implement the logic to obtain the score
        This is based on the win posibility rate againt lose posibilty rate.
        Only current moment is cosidered."""
        #print(f"in calculate_position_value, state:")
        #[ print(state[i]) for i in range(3)]
        player = self.check_win(state, self.turn)
        if player is not None:
            return 1
        player = self.check_win(state, self.opponent_turn)
        if player is not None:
            return -1

        valid_move_indexes = self.get_valid_move_indexes(state)
        #print(f"valid_move_indexes: {valid_move_indexes}")

        opponent = not self.get_turn(state) == self.turn
        values = [self.get_heuristic(self.get_next_state(state, x, y, opponent))
                  for x, y in valid_move_indexes]
        #print(f"values: {values}")

        if len(values) == 0:
            return 0

        min_or_max = self.choose_min_or_max_for_comparison(state)
        pos_value = min_or_max(values)
        #print(f"pos_value: {pos_value}")
        return pos_value

    def put_state_in_cache(self, state, pos_value):
        """put_state_in_cache method. Add the state as a key to add it into a dictionary"""
        state_str = self.state_to_string(state)
        self.cached_state[state_str] = pos_value

    def get_cached_state(self, state):
        """get_cached_state method. fetch the state from a dictionary."""
        state_str = self.state_to_string(state)
        if self.cached_state.get(state_str) is not None:
            return self.cached_state[state_str], True
        return -1, False

    def state_to_string(self, state):
        """state_to_string method. Stransform the state into a hashable string."""
        state_str = ""
        for i in range(3):
            for j in range(3):
                state_str = state_str + str(state[i][j])
        return state_str

    def check_win(self, state, player):
        """check_win method. Validate if the a state is a win state."""
        p_win = [player.value] * 3
        for i in range(3):
            if state[i] == p_win:
                return player
            col = []
            for j in range(3):
                col.append(state[j][i])
            if col == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(state[i][i])
            if diag == p_win:
                return player
        diag = []
        for i in range(3):
            diag.append(state[i][2-i])
            if diag == p_win:
                return player
        return None

    def get_valid_move_indexes(self, state):
        """get_valid_move_indexes method. get the list of valid moved for the provided state"""
        move_list = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == MoveValue.EMPTY.value:
                    move_list.append((i,j))
        return move_list

    def choose_min_or_max_for_comparison(self, state):
        """choose_min_or_max_for_comparison method. check the turn on the board,
        based on that defines the method to implement (min for opponen, max for current player)"""
        turn = self.get_turn(state)
        return max if turn == self.turn else min

    def get_turn(self, state, reverse = False):
        """get_turn method. get the turn of the next player based on the board state"""
        order_value = 1 if reverse else 0
        count = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == PLAYER1:
                    count += 1
                elif state[i][j] == PLAYER2:
                    count -= 1
        if count == order_value:
            return MoveValue.PLAYER1
        return MoveValue.PLAYER2
