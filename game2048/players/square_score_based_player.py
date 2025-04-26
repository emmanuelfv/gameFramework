"""square score module. brute force player for game 2048.
Strategy: sum of all squares in the grid."""
from game2048.players.agent_player import AgentPlayer
from game2048.cursor_move import CursorValue
from game2048.game_2048_game import Game2048


class SquareScorePlayer(AgentPlayer):
    """SquareScorePlayer class. search next possible moves to get the best option based on 
    strategy score."""
    def __init__(self, game: Game2048 = None, depth = 1):
        """__init__ method."""
        super().__init__()
        print("square score player set")
        self.name = "squareScorePlayer"
        self.depth = depth
        self.game: Game2048 = game

    def decide_move(self):
        """decide_move method. Implement the strategy and return a movement.
        This method also implements a BFS to find the best move."""
        from copy import deepcopy
        # Helper: simulate a move on a given state using game methods.
        def simulate_move(state, move):
            # Use deepcopy to avoid side effects.
            new_state = deepcopy(state)
            if move == CursorValue.UP:
                temp_state = [list(row) for row in zip(*new_state)]
                self.game.sum_values_and_shrink(temp_state)
                new_state = [list(row) for row in zip(*temp_state)]
            elif move == CursorValue.DOWN:
                temp_state = [list(row) for row in zip(*new_state)]
                temp_state = [list(reversed(row)) for row in temp_state]
                self.game.sum_values_and_shrink(temp_state)
                reversed_rows = [list(reversed(row)) for row in temp_state]
                new_state = [list(row) for row in zip(*reversed_rows)]
            elif move == CursorValue.LEFT:
                temp_state = [row[:] for row in new_state]
                self.game.sum_values_and_shrink(temp_state)
                new_state = [row[:] for row in temp_state]
            elif move == CursorValue.RIGHT:
                temp_state = [list(reversed(row)) for row in new_state]
                self.game.sum_values_and_shrink(temp_state)
                new_state = [list(reversed(row)) for row in temp_state]
            return new_state

        # Initialize BFS from the current state.
        orig_state = deepcopy(self.game.game_state)
        best_score = float('-inf')
        best_first_move = None
        
        # Use valid_move_list as initial candidates.
        queue = []
        for move in self.valid_move_list:
            state_after_move = simulate_move(orig_state, move)
            # Only add if the move changes the state.
            if state_after_move != orig_state:
                queue.append((state_after_move, move, 1))
        
        # BFS over moves up to self.depth
        while queue:
            state, first_move, depth = queue.pop()
            #print(queue)
            if depth == self.depth:
                score = self.strategy(state)
                #print(f"try score: {score} for move {first_move}")
                #self.game.print_game_state(state)
                if score > best_score:
                    #print(f"New best score: {score} for move {first_move}")
                    #self.game.print_game_state(state)
                    best_score = score
                    best_first_move = first_move
            else:
                for move in (CursorValue.UP, CursorValue.DOWN, CursorValue.LEFT, CursorValue.RIGHT):
                    self.game.add_new_number(state)
                    next_state = simulate_move(state, move)
                    # Only pursue moves that change the state.
                    if next_state != state:
                        queue.append((next_state, first_move, depth + 1))
                        
        # Fallback if no BFS branch improved score.
        return best_first_move if best_first_move is not None else self.valid_move_list[0]

    def strategy(self, state):
        """strategy method. return the score of the state."""
        return  sum([x**2 for row in state for x in row if x > 0])