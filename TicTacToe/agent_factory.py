
from TicTacToe.players import best_move_player,minimax_player,agent_player,human_player,ui_player

def agent_factory(player_str):
    if player_str == 'BestMovePlayer':
        return best_move_player.BestMovePlayer()
    if player_str == 'MinimaxPlayer':
        return minimax_player.MinimaxPlayer()
    if player_str == 'PlayerAgent':
        return agent_player.AgentPlayer()
    if player_str == 'HumanPlayer':
        return human_player.HumanPlayer()
    if player_str == 'UiPlayer':
        return ui_player.UiPlayer()

