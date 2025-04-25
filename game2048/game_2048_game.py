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
The player loses if, after a valid move, the new number cannot be placed. Their final score will be the total sum of the cells.
The player wins if they score 2048 points in a single cell.
Agents:
user interface
MLP
Convilucionals
Recurrent networks
"""

import random

from game_single_agent import GameSingleAgent
from game2048.cursor_move import MoveValue
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
        self.win_threshold = 2048
        self.turns_limit = 300
        print(self.game_name)


    def print_game_state(self, state = None):
        """print_game_state method. Print the tic tac toe game state. """
        print("board state:")
        if state is None:
            state = self.game_state
        for row in state:
            print("".join(f"{num:5}" for num in row))


    def set_move(self, player: AgentPlayer)-> bool:
        """set_move method. Run the player decide method."""
        player.set_game_state(self.game_state.copy())
        move = player.decide_move()
        move_status = self.play_move(move)
        if not move_status:
            print("invalid Move, lose")
        return move_status


    def play_move(self, move)-> bool:
        """play_move method. Upate the game state based on the player move."""
        print(move, type(move))
        if move in (MoveValue.UP, MoveValue.DOWN, MoveValue.LEFT, MoveValue.RIGHT):
            tempState = self.moveToTempState(move)
            self.sumValuesAndShrink(tempState)
            self.moveToState(tempState, move)
            self.add_new_number()
            return True
        return False


    def check_win(self) -> bool | None:
        """check_win method. Validate if the player won.
        It also validates if the game is over by checking that no other sum of same numbers can be done."""

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.game_state[i][j] == self.win_threshold:
                    return True
        
        is_move_possible = False
        original_state = self.game_state.copy()
        for move in (MoveValue.UP, MoveValue.DOWN, MoveValue.LEFT, MoveValue.RIGHT):
            tempState = self.moveToTempState(move)
            self.sumValuesAndShrink(tempState)
            self.moveToState(tempState, move)
            if original_state != self.game_state:
                print(f"move possible at {move}")
                self.print_game_state(tempState)
                self.print_game_state()
                print("move possible")
                is_move_possible = True
                self.game_state = original_state.copy()
                break
            self.game_state = original_state.copy()
        if not is_move_possible:
            return False
        return None


    def reset_state(self):
        """reset_state method. Clear game_state."""
        self.game_state = [ [0] * self.grid_size for i in range(self.grid_size) ]


    ### game specific methods ###

    def sumValuesAndShrink(self, state):
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
                if state[i][j] != 0:
                    for k in range(j+1, grid_size):
                        if state[i][k] != 0:
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

    def moveToTempState(self, direction):
        """Convert state to a temporary representation for left move processing."""
        state = self.game_state
        if direction == MoveValue.UP:
            return [list(row) for row in zip(*state)]
        elif direction == MoveValue.DOWN:
            # Transpose then reverse each row.
            transposed = [list(row) for row in zip(*state)]
            return [list(reversed(row)) for row in transposed]
        elif direction == MoveValue.LEFT:
            return [row[:] for row in state]
        elif direction == MoveValue.RIGHT:
            return [list(reversed(row)) for row in state]

    def moveToState(self, state, direction):
        """Revert the temporary representation back to original orientation."""
        if direction == MoveValue.UP:
            self.game_state = [list(row) for row in zip(*state)]
        elif direction == MoveValue.DOWN:
            reversed_rows = [list(reversed(row)) for row in state]
            self.game_state = [list(row) for row in zip(*reversed_rows)]
        elif direction == MoveValue.LEFT:
            self.game_state = [row[:] for row in state]
        elif direction == MoveValue.RIGHT:
            self.game_state = [list(reversed(row)) for row in state]

    def add_new_number(self):
        """
        add_new_number method. Add a new number to the state.
        """
        grid_size = self.grid_size
        state = self.game_state
        empty_cells = [(i, j) for i in range(grid_size) for j in range(grid_size) if state[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            state[i][j] = random.choice([2, 4])



