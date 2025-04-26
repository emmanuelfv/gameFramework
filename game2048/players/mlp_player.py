"""mlp_player module. deep learning player for game 2048"""
from game2048.players.agent_player import AgentPlayer
from game2048.cursor_move import CursorValue



class MLPPlayer(AgentPlayer):
    """MLPPlayer class. calls torch and mlp model to predict the next move."""
    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("MLP player set")
        self.name = "2048MLP"

    def decide_move(self):
        """decide_move method. Implement the strategy and return a movement"""
        """NO YET IMPLEMENTED"""
        move_str="z"
        print("valid moves: ", self.valid_move_list)
        while self.direction_list[move_str] not in self.valid_move_list :
            move_str=input("your turn. Set direction (up/down/left/right: [w/s/a/d]):").lower()
            x = self.direction_list[move_str]
            print(f"you selected {x}")
        return x

    def loss_function(self, state):
        """loss_function method. loss function for the model"""
        """Proposals:
        - sum of sqares of all values in the grid"""
        return  sum()