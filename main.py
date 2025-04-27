"""
Main.py 
fution to test the basic fuctionality
"""

import time
from collections import Counter

from game_two_agents import GameTwoAgents
from TicTacToe.tic_tac_toe_game import TicTacToeGame
from TicTacToe.agent_factory import agent_factory

from TicTacToeBig.tic_tac_toe_big_game import TicTacToeBigGame
from TicTacToeBig.players.ttt_big_best_move_player import TTTBigAgentPlayer
from TicTacToeBig.players.ttt_big_ui_player import TTTBigUiPlayer

from game_single_agent import GameSingleAgent
from game2048.game_2048_game import Game2048
from game2048.players.agent_player import AgentPlayer 
from game2048.players.human_player import HumanPlayer
from game2048.players.square_score_based_player import SquareScorePlayer
from game2048.performance_test import test_overal_performance

def main():
    """
    main function
    
    example for TicTacToeBigGame:
    """
    """ 
    game: GameTwoAgents = TicTacToeBigGame()
    game.set_player2(TTTBigAgentPlayer())
    game.set_player1(TTTBigUiPlayer())
    game.set_starter_player()
    game.start_game()
    """
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
    #test_overal_performance("SquareScorePlayer", runs=100, depth=5)
    test_overal_performance("AgentPlayer", runs=1000)

if __name__ == "__main__":
    main()
