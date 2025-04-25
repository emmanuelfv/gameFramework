"""
game_two_agents.py
This class works as an interface to play 2 player games
A player can be a human or any artifitial inteligence as an agent
"""
from TicTacToe.players.agent_player import AgentPlayer
from ttt_move import MoveValue, TTTMove, EMPTY

class GameTwoAgents:
    """
    This class works as an interface to play 2 player games
    A player can be a human or any artifitial inteligence as an agent    
    """
    def __init__(self):
        """
        __init__ method. Variables: 
        player1, player2, is_player1_starting, game_state, turns_limit, 
        """
        self.player1: AgentPlayer = None
        self.player2: AgentPlayer = None
        self.is_player1_starting: bool = True
        self.game_state = None
        self.turns_limit: int = 100

    def print_game_state(self):
        """print_game_state method. Print the game state."""
        print("function printGameState in game_two_agents not created yet")

    def set_player1(self, player):
        """
        set_player1 method. Decide player1.
        """
        self.player1 = player
        player.set_turn(MoveValue.PLAYER1)

    def set_player2(self, player):
        """
        set_player2 method. Decide player2.
        """
        self.player2 = player
        player.set_turn(MoveValue.PLAYER2)

    def set_starter_player(self, player=None):
        """
        set_starter_player method. Decide the first player.
        """
        if not player:
            self.is_player1_starting = True
        elif player == MoveValue.PLAYER2:
            self.is_player1_starting = False
        print("Player {1 if self.is_player1_starting else 2} starts")

    def set_move(self, player: AgentPlayer)-> bool:
        # pylint: disable=unused-argument
        """set_move method. Run the player decide method."""
        print("function set_move in game_two_agents not created yet")
        return True

    def play_move(self, move: TTTMove)-> bool:
        # pylint: disable=unused-argument
        """play_move method. Upate the game state based on the player move."""
        print("function play_move in game_two_agents not created yet")
        return True

    def check_win(self, player) -> AgentPlayer:
        # pylint: disable=unused-argument
        """check_win method. Validate if the player won. """
        print("function check_win in game_two_agents not created yet")

    def get_player(self, turn: int, player_turn_rotation: int)-> AgentPlayer:
        """get_player method. Uses the turn to decide the next player."""
        #print(f"in get_player. Turn: {turn}")
        #print("player_turn_rotation {player_turn_rotation}")
        #print("players: {self.player1}, {self.player2}")
        return self.player1 if turn % 2 == player_turn_rotation else self.player2

    def reset_state(self):
        """reset_state method. Clear game_state."""
        self.game_state = None

    def update_players(self, results):
        if hasattr(self.player1, "set_game_results"):
            self.player1.set_game_state(self.game_state.copy())
            self.player1.set_game_results(results)
        if hasattr(self.player2, "set_game_results"):
            self.player2.set_game_state(self.game_state.copy())
            self.player2.set_game_results(results)
    
    def ask_for_retry(self):
        retry = False
        if hasattr(self.player1, "ask_for_retry"):
            retry = self.player1.ask_for_retry() or retry
            if retry:
                print("retry has been requested by player 1")
        if hasattr(self.player2, "ask_for_retry"):
            retry = self.player2.ask_for_retry() or retry
            if retry:
                print("retry has been requested by player 2")
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
        self.reset_state()
        player_turn_rotation = 0
        turn = 0
        if not self.is_player1_starting:
            player_turn_rotation = 1

        while turn < self.turns_limit:
            print(f"starting turn {turn+1}")
            self.print_game_state()
            player = self.get_player(turn, player_turn_rotation)
            if not self.set_move(player):
                return None
            turn+=1

            if self.check_win(player.turn) is not None:
                break

        if turn == self.turns_limit:
            print("turns limit reached, draw")
            self.print_game_state()
            self.update_players(EMPTY)
            return None

        print(f"winner is {self.check_win(player.turn)}, {player.get_name()}")
        self.print_game_state()

        self.update_players(player.turn.value)
        return player.get_name()
