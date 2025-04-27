# Observations

## Working on AgentPlayer with depth 1
 - Number of runs: 1000
 - Total turns: 118.678
 - Average score: 265.596
 - Max tiles: [16, 32, 64, 128, 256]

 - [x] Times types: [get_valid_moves / copy_game_state / decide_move / play_move]
 - Total time consumed: ['0.0214', '0.0003', '0.0010', '0.0013']
 - Percentage over all time consumed: ['88.94', '1.32', '4.16', '5.58']


## Working on SquareScorePlayer with depth 1
 - Number of runs: 100
 - Total turns: 254.48
 - Average score: 563.78
 - Max tiles: [64, 128, 256, 512]

 - [x] Times types: [get_valid_moves / copy_game_state / decide_move / play_move]
 - Total time consumed: ['0.0230', '0.0004', '0.0045', '0.0021']
 - Percentage over all time consumed: ['76.70', '1.30', '14.95', '7.05']


## Working on SquareScorePlayer with depth 5
 - Average score: 2212.32
 - Max tiles: [256, 512, 1024, 2048]

 - [x] Times types: [get_valid_moves / copy_game_state / decide_move / play_move]
 - Total time consumed: ['0.0590', '0.0000', '16.9947', '0.0183']
 - Percentage over all time consumed: ['0.35', '0.00', '99.55', '0.11']