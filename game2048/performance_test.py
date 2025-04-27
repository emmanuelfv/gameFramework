"""
performance_test.py. File to define test case to measure the performance of the game2048.
"""

from collections import Counter

from game2048.game_2048_game import Game2048
from game2048.players.agent_player import AgentPlayer
from game2048.players.human_player import HumanPlayer
from game2048.players.square_score_based_player import SquareScorePlayer
from game_single_agent import GameSingleAgent


def agent_factory(agent_type: str, game: Game2048 = None, depth: int = 1) -> AgentPlayer:
    """
    agent_factory function. Factory function to create an agent based on the type.
    """
    if agent_type == "SquareScorePlayer":
        return SquareScorePlayer(game, depth)
    elif agent_type == "HumanPlayer":
        return HumanPlayer()
    elif agent_type == "AgentPlayer":
        return AgentPlayer()
    else:
        raise ValueError(f"Unknown agent type: {agent_type}")
    
def test_random_player():
    """
    test_random_player function. Test the random player.
    """
    game = Game2048()
    game.set_player(agent_factory("AgentPlayer"))
    game.start_game()
    return game.calculate_score()

def test_human_player():
    """
    test_human_player function. Test the human player.
    """
    game = Game2048()
    game.set_player(agent_factory("HumanPlayer"))
    game.start_game()
    return game.calculate_score()


def test_square_score_player():
    """
    test_square_score_player function. Test the square score player.
    """
    game = Game2048()
    game.set_player(agent_factory("SquareScorePlayer", game, 5))
    game.start_game()
    return game.calculate_score()

def run_single_tests():
    """
    run_single_tests function. Run the tests individually.
    """
    results = {
        "random_player": test_random_player(),
        "human_player": test_human_player(),
        "square_score_player": test_square_score_player()
    }
    print("Performance Test Results:")
    for player, score in results.items():
        print(f"{player}: {score}")


def test_score_average(agent_type, runs=1, depth=1, print_game_state=False):
    """
    test_score_average function. Test the game with multiple runs.
    """
    result_score = []
    result_turns = []
    for i in range(runs):
        game: GameSingleAgent = Game2048()
        game.set_player(agent_factory(agent_type, game, depth))
        game.start_game(print_game_state=False)
        result_turns.append(game.calculate_score()["turns"])
        result_score.append(game.calculate_score()["score"])
    print(f"number of runs: {runs}")
    print(f"your total turns is {sum(result_turns) / runs}")
    print(f"your score is {sum(result_score) / runs}")

def test_time_performance(agent_type, runs=1, depth=1, print_game_state=False):
    """
    test_multiple_runs function. Test the game with multiple runs.
    """
    results = []
    for i in range(runs):
        game: GameSingleAgent = Game2048()
        game.set_player(agent_factory(agent_type, game, depth))
        times = [0, 0, 0, 0] 
        game.start_game(print_game_state, times=times)
        results.append(game.calculate_score()["turns"])
    print(f"total time consumed: {[t for t in times]}")
    print(f"average times per run: {[t/runs for t in times]}")
    print(f"percentage over all time consumed: { [100 * t / sum(times) for t in times]}")

def test_max_tiles(agent_type, runs=100, depth=1):
    """
    test_max_tile function. Test the game with multiple runs.
    """
    results = []
    for i in range(runs):
        game: GameSingleAgent = Game2048()
        game.set_player(agent_factory(agent_type, game, depth))
        game.start_game(print_game_state=False)
        results.append(game.calculate_score()["max_tile"])
    print(f"max tiles are: {Counter(results)}")

def test_overal_performance(agent_type, runs=100, depth=1, print_game_state=False):
    """
    test_overal_performance function. Test the game with multiple runs.
    """
    result_score = []
    result_turns = []
    result_max_tile = []
    for i in range(runs):
        game: GameSingleAgent = Game2048()
        game.set_player(agent_factory(agent_type, game, depth))
        times = [0, 0, 0, 0] 
        game.start_game(print_game_state, times=times)
        result_turns.append(game.calculate_score()["turns"])
        result_score.append(game.calculate_score()["score"])
        result_max_tile.append(game.calculate_score()["max_tile"])
    print(f"## Working on {agent_type} with depth {depth}")
    print(f" - Number of runs: {runs}")
    print(f" - Total turns: {sum(result_turns) / runs}")
    print(f" - Average score: {sum(result_score) / runs}")
    tiles_count = Counter(result_max_tile)
    print(f" - Max tiles: {[ f"{k}:{tiles_count[k]}" for k in sorted(tiles_count.keys(), reverse=True)]}")
    print("")
    print(" - [x] Times types: [get_valid_moves / copy_game_state / decide_move / play_move]")
    print(f" - Total time consumed: {[f'{t:.4f}' for t in times]}")
    print(f" - Percentage over all time consumed: {[f'{100 * t / sum(times):.2f}' for t in times]}")

