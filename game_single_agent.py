"""
game_single_agent.py
This class works as an interface to play 1 player games.
A player can be a human or any artifitial inteligence as an agent
"""

class GameSingleAgent:
    """
    This class works as an interface to play 2 player games
    A player can be a human or any artifitial inteligence as an agent    
    """
    def __init__(self):
        """
        __init__ method. Variables: 
        player1, player2, is_player1_starting, game_state, turns_limit, 
        """
        self.player = None
        self.game_state = None
        self.turns_limit: int = 100
        self.turns_limit_result: str = "Undefined"

    def print_game_state(self):
        """print_game_state method. Print the game state."""
        print("function printGameState in game_single_agent not created yet")

    def set_player(self, player):
        """
        set_player method. Decide player1.
        """
        self.player = player

    def set_move(self, player)-> bool:
        # pylint: disable=unused-argument
        """set_move method. Run the player decide method."""
        print("function set_move in game_two_agents not created yet")
        return True

    def play_move(self, move)-> bool:
        # pylint: disable=unused-argument
        """play_move method. Upate the game state based on the player move."""
        print("function play_move in game_two_agents not created yet")
        return True

    def check_win(self) -> bool:
        """check_win method. Validate if the player won. """
        print("function check_win in game_two_agents not created yet")

    def reset_state(self) -> None:
        """reset_state method. Clear game_state."""
        self.game_state = None

    def update_player(self, results):
        """
        update_player method. Update the player with the game state and results.
        """
        if hasattr(self.player, "set_game_results"):
            self.player.set_game_state(self.game_state.copy())
            self.player.set_game_results(results)

    def ask_for_retry(self) -> bool:
        """
        ask_for_retry method. Ask the player if he wants to retry.
        """
        retry = False
        if hasattr(self.player, "ask_for_retry"):
            retry = self.player1.ask_for_retry()
            if retry:
                print("retry has been requested by player 1")
        return retry

    def start_game(self):
        """
        start_game method. Control the game flow.
        flow:
            choose player
            make player move
            check win
            if win r moves limit: end game 
        """
        player = self.player
        self.reset_state()
        turn = 0

        while turn < self.turns_limit:
            #self.print_game_state()
            if not self.set_move(player):
                return None
            turn+=1

            game_finished = self.check_win() # pylint: disable=E1111
            if game_finished is not None:
                break

        if turn == self.turns_limit:
            print("Turns limit reached, game over")
            print(f"Result is {self.turns_limit_result}")
            self.print_game_state()
            return None

        print(f"Result is {"win" if game_finished else "lose"}")
        self.print_game_state()

        return player.get_name()

    def calculate_score(self) -> dict:
        """
        calculate_score method. Calculate the score of the game.
        """
        return {}
