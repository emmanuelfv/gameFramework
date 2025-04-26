"""human_player module. Player to manual movements based on consol input"""
from TicTacToe.players.agent_player import AgentPlayer
from ttt_move import TTTMove

class HumanPlayer(AgentPlayer):
    """HumanPlayer class. Player to manual movements based on consol input"""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("Human player set")
        self.name = "Human" #input("Name:").strip()

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        print(self.game_state)
        move_str=input(f"{self.name}'s turn. Set space separated mark:")
        move_pos = list(map(int, move_str.strip().split(" ")))

        while move_pos not in self.valid_move_list:
            move_str=input("Invalid movement, please set space separated mark:")
            move_pos = list(map(int, move_str.strip().split(" ")))
        x, y = move_pos
        return TTTMove(x, y, self.turn.value)
