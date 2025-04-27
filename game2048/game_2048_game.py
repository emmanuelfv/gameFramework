"""game_2048_game module. Defines game 2048 
methods and validations based on SingleAgentGame

Rules:
state is a 4x4 matrix with numbers of values 0 2 4 8 16 32 64 128 256 1024 2048.
Valid moves are up, down, left and right.
A valid move causes all non-zero numbers to shift in the selected direction. 
Equal numbers that collide will be added together, eliminating one of the two numbers. 
A new number 2 or 4 will be generated in a space with a value of 0.
example:
0 0 0 0
0 2 2 0
4 4 4 0
4 2 4 2
right
0 0 0 2
0 0 0 4
0 0 4 8
4 2 4 2
A move will be invalid if it does not generate any movement in the current cells.
The player loses if, after a valid move, the new number cannot be placed. 
Their final score will be the total sum of the cells.
The player wins if they score 2048 points in a single cell.
Agents:
user interface
MLP
Convilucionals
Recurrent networks
"""

import time
import random 
from copy import deepcopy

from game_single_agent import GameSingleAgent
from game2048.cursor_move import CursorValue
from game2048.players.agent_player import AgentPlayer

class Game2048(GameSingleAgent):
    """tic_tac_toe_game class. Defines tic tac toe 
    methods and validations based on GameTwoAgents"""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        self.game_name = "Game2048"
        self.grid_size = 4
        self.game_state = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.win_threshold = 4096
        self.turns_limit = 2000
        self.current_turn = 0
        print(self.game_name)

    def print_game_state(self, state = None):
        """print_game_state method. Print the tic tac toe game state. """
        print("board state:")
        if state is None:
            state = self.game_state
        for row in state:
            print("".join(f"{num:5}" for num in row))

    def get_valid_moves(self):
        """get_valid_moves method. Get the valid moves for the current game state."""
        valid_moves = []
        original_state = deepcopy(self.game_state)   # using deepcopy for nested lists
        for move in (CursorValue.UP, CursorValue.DOWN, CursorValue.LEFT, CursorValue.RIGHT):
            temp_state = self.move_to_temp_state(move)
            self.sum_values_and_shrink(temp_state)
            self.move_to_state(temp_state, move)
            if self.game_state != original_state:
                valid_moves.append(move)
            self.game_state = deepcopy(original_state)  # restore state from deepcopy
        return valid_moves

    def set_move(self, player: AgentPlayer, times=None)-> bool:
        """set_move method. Run the player decide method."""
        self.current_turn += 1
        print(f"turn {self.current_turn}")

        t1 = time.time()
        valid_moves = self.get_valid_moves()
        t2 = time.time()
        player.set_game_state(self.game_state.copy(), valid_moves)
        t3 = time.time()
        move = player.decide_move()
        t4 = time.time()
        move_status = self.play_move(move)
        t5 = time.time()

        if times is not None:
            times[0] += t2 - t1
            times[1] += t3 - t2
            times[2] += t4 - t3
            times[3] += t5 - t4

        if not move_status:
            print("invalid Move, lose")
        return move_status

    def play_move(self, move)-> bool:
        """play_move method. Upate the game state based on the player move."""
        #print(move, type(move))
        if move in (CursorValue.UP, CursorValue.DOWN, CursorValue.LEFT, CursorValue.RIGHT):
            temp_state = self.move_to_temp_state(move)
            self.sum_values_and_shrink(temp_state)
            self.move_to_state(temp_state, move)
            self.add_new_number()
            return True
        return False

    def check_win(self) -> bool | None:
        """check_win method. Validate if the player won. It also validates if the game 
        is over by checking that no other sum of same numbers can be done."""
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.game_state[i][j] == self.win_threshold:
                    return True
        is_move_possible = False
        original_state = deepcopy(self.game_state)   # use deepcopy here
        for move in (CursorValue.UP, CursorValue.DOWN, CursorValue.LEFT, CursorValue.RIGHT):
            temp_state = self.move_to_temp_state(move)
            self.sum_values_and_shrink(temp_state)
            self.move_to_state(temp_state, move)
            if original_state != self.game_state:
                is_move_possible = True
                self.game_state = deepcopy(original_state)
                break
            self.game_state = deepcopy(original_state)
        if not is_move_possible:
            return False
        return None

    def reset_state(self):
        """reset_state method. Clear game_state."""
        self.game_state = [ [0] * self.grid_size for i in range(self.grid_size) ]
        self.add_new_number()
        self.add_new_number()


    ### game specific methods ###

    def sum_values_and_shrink(self, state):
        """
        sumValues method. Sum two consecutive values for every row.
        After the sum, the values are moved to the left.
        The empty spaces are filled with 0.
        examples: 
            0 2 2 0 -> 4 0 0 0
            4 0 0 4 -> 8 0 0 0
            2 2 2 2 -> 4 4 0 0
        """
        grid_size = self.grid_size
        for i in range(grid_size):
            for j in range(grid_size-1):
                if state[i][j] == 0:
                    continue
                for k in range(j+1, grid_size):
                    if state[i][k] == 0:
                        continue
                    if state[i][j] == state[i][k]:
                        state[i][j] *= 2
                        state[i][k] = 0
                    break
            cont = 0
            for j in range(grid_size):
                if state[i][j] != 0:
                    state[i][cont] = state[i][j]
                    cont += 1
            for j in range(cont, grid_size):
                state[i][j] = 0

    def move_to_temp_state(self, direction):
        """Convert state to a temporary representation for left move processing."""
        state = self.game_state
        if direction == CursorValue.UP:
            return [list(row) for row in zip(*state)]
        if direction == CursorValue.DOWN:
            # Transpose then reverse each row.
            transposed = [list(row) for row in zip(*state)]
            return [list(reversed(row)) for row in transposed]
        if direction == CursorValue.LEFT:
            return [row[:] for row in state]
        if direction == CursorValue.RIGHT:
            return [list(reversed(row)) for row in state]

    def move_to_state(self, state, direction):
        """Revert the temporary representation back to original orientation."""
        if direction == CursorValue.UP:
            self.game_state = [list(row) for row in zip(*state)]
        elif direction == CursorValue.DOWN:
            reversed_rows = [list(reversed(row)) for row in state]
            self.game_state = [list(row) for row in zip(*reversed_rows)]
        elif direction == CursorValue.LEFT:
            self.game_state = [row[:] for row in state]
        elif direction == CursorValue.RIGHT:
            self.game_state = [list(reversed(row)) for row in state]

    def add_new_number(self, state=None):
        """
        add_new_number method. Add a new number to the state.
        The number is either 2 or 4 with 90% probability of being 2.
        """
        grid_s = self.grid_size
        if state is None:
            state = self.game_state
        empty_cells = [(i, j) for i in range(grid_s) for j in range(grid_s) if state[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            state[i][j] = 2 if random.random() < 0.9 else 4

    def calculate_score(self) -> dict:
        """
        calculate_score method. Calculate the score of the game.
        """
        results_dict = {}
        score = 0
        for row in self.game_state:
            for num in row:
                score += num
        results_dict["score"] = score
        results_dict["turns"] = self.current_turn
        results_dict["is_win"] = self.check_win()
        results_dict["max_tile"] = max([max(row) for row in self.game_state])
        return results_dict
