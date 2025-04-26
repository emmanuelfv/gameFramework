"""human_player module. Player to manual movements based on consol input"""
from game2048.players.agent_player import AgentPlayer
from game2048.cursor_move import CursorValue



class HumanPlayer(AgentPlayer):
    """HumanPlayer class. Player to manual movements based on consol input"""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("Human player set")
        self.name = "Human" #input("Name:").strip()
        self.direction_list = {"w":CursorValue.UP,
                          "s":CursorValue.DOWN,
                          "a":CursorValue.LEFT,
                          "d":CursorValue.RIGHT,
                          "z":None}

    def decide_move(self):
        """decide_move method. Implement the strategy and return a movement"""
        move_str="z"
        print("valid moves: ", self.valid_move_list)
        while self.direction_list[move_str] not in self.valid_move_list :
            move_str=input("your turn. Set direction (up/down/left/right: [w/s/a/d]):").lower()
            x = self.direction_list[move_str]
            print(f"you selected {x}")
        return x
