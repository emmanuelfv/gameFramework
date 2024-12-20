"""
Main.py 
fution to test the basic fuctionality
"""

from game_two_agents import GameTwoAgents
from TicTacToe.tic_tac_toe_game import TicTacToeGame
from TicTacToe.agent_factory import agent_factory

from TicTacToeBig.tic_tac_toe_big_game import TicTacToeBigGame
from TicTacToeBig.players.ttt_big_best_move_player import TTTBigAgentPlayer
from TicTacToeBig.players.ttt_big_ui_player import TTTBigUiPlayer

def main():
    """
    main function
    
    example for TicTacToeBigGame:
    """
    game: GameTwoAgents = TicTacToeBigGame()
    game.set_player2(TTTBigAgentPlayer())
    game.set_player1(TTTBigUiPlayer())
    game.set_starter_player()
    game.start_game()

    """
    end game menu
    last piece
    game: GameTwoAgents = TicTacToeGame()
    game.set_player2(agent_factory('UiPlayer'))
    game.set_player1(agent_factory('MinimaxPlayer'))
    game.set_starter_player()
    retry = True
    while retry:
        game.reset_state()
        game.start_game()
        retry = game.ask_for_retry()
        if retry:
            print("Retrying")
    print("closing program.")
    """
if __name__ == "__main__":
    main()
