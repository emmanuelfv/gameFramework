"""
ui_player.py

"""
import time
import pygame
import sys

from TicTacToe.players.agent_player import AgentPlayer
from ttt_move import TTTMove

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

class UiPlayer(AgentPlayer):
    """
    UiPlayer class. Graphic interface for human interaction
    """
    

    def __init__(self):
        """__init__ method."""
        super().__init__()
        print("UI player set")
        self.name = "ui player"

        self.displacement = 64
        self.piece_size = (self.displacement,self.displacement)
        self.grid_size = (self.displacement*5, self.displacement*5)
        pygame.init()
        pygame.display.set_caption("tic_tac_toe")
        self.display = pygame.display.set_mode(self.grid_size)
        self.icon_o = pygame.transform.scale(pygame.image.load("resources/icon_o.png"), self.piece_size)
        self.icon_x = pygame.transform.scale(pygame.image.load("resources/icon_x.png"), self.piece_size)
        pygame.display.set_icon(self.icon_o)
        self.background = pygame.image.load("resources/background.jpg")
        self.turn = 1

        self.sleeps = True
        self.sleep_time = 0.2

    def decide_move(self) -> TTTMove:
        """decide_move method. Implement the strategy and return a movement"""
        #print(self.game_state)
        x, y = self.run()
        #print("res", x, y)
        return TTTMove(x, y, self.turn.value)

    ## Other methods ##

    def add_movement(self):
        mouse_values = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        game_pos = (mouse_pos[0]//self.displacement - 1, mouse_pos[1]//self.displacement - 1)
        #print(mouse_pos, mouse_values, game_pos)
        if mouse_values[0] and 0 <= game_pos[0] <= 2 and 0 <= game_pos[1] <= 2 and self.game_state[game_pos[0]][game_pos[1]] == 1:
            movement_pos = (self.displacement * (game_pos[0]+1), self.displacement * (game_pos[1]+1))
            icon = self.icon_o if self.turn.value % 2 == 0 else self.icon_x
            self.display.blit(icon, movement_pos)
            return game_pos
        return -1, -1
            

    def display_movements(self):
        for i in range(3):
            for j in range(3):
                if self.game_state[i][j]  != 1:
                    movement_pos = (self.displacement * (i+1), self.displacement * (j+1))
                    icon = self.icon_o if self.game_state[i][j] % 2 == 0 else self.icon_x
                    self.display.blit(icon, movement_pos)

    def run(self):
        """display method. Runs the game loop for tic tac toe game"""
        self.display.blit(self.background, (0,0))
        d = self.displacement
        pygame.draw.lines(self.display, PURPLE, True, ((d*2,d*1),(d*3,d*1),(d*3,d*4),(d*2,d*4)), 3)
        pygame.draw.lines(self.display, PURPLE, True, ((d*1,d*2),(d*4,d*2),(d*4,d*3),(d*1,d*3)), 3)
        pygame.draw.lines(self.display, GREEN, True, ((d*1,d*1),(d*4,d*1),(d*4,d*4),(d*1,d*4)), 3)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            move_x, move_y = self.add_movement()
            self.display_movements()
            #print("move_x, move_y", move_x, move_y)
            if move_x != -1:
                running = False
            pygame.display.update()
        if self.sleeps: 
            time.sleep(self.sleep_time)
        return move_x, move_y

    def set_game_results(self, results):
        """show_end_game Method. Shows the results of the game"""
        fond = pygame.font.Font('freesansbold.ttf', self.displacement//2)
        end_message = fond.render('END GAME', True, WHITE, BLACK)
        winner = fond.render(('DRAW','WINNER is O','WINNER is X')[results-1], True, WHITE, BLACK)
        self.display_movements()
        self.display.blit(end_message, (self.get_centered_x_position(end_message), int(self.displacement*1.5)))
        self.display.blit(winner, (self.get_centered_x_position(winner), self.displacement*2))
        pygame.display.update()
        if self.sleeps: 
            time.sleep(self.sleep_time*5)
         

    def get_centered_x_position(self, surface):
        return (self.grid_size[0]-surface.get_size()[0])//2
    
    def button_msg(self, msg_str, font=None, color=WHITE, bg=BLACK, pos_x=-1, pos_y=-1):
        if font is None:
            fond = pygame.font.Font('freesansbold.ttf', 20)
        message = fond.render(msg_str, True, color, bg)
        if pos_x == -1:
            pos_x = self.get_centered_x_position(message)
        if pos_y == -1:
            pos_y = self.get_centered_y_position(message)
        mouse_values = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        message_size = message.get_size()
        self.display.blit(message, (pos_x, pos_y))

        if mouse_values[0] and pos_x <= mouse_pos[0] <= pos_x + message_size[0] and pos_y <= mouse_pos[1] <= pos_y + message_size[1]:
            return True

    def ask_for_retry(self):
        """ask_for_retry method. tells the game to retry"""
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if self.button_msg("RETRY?", pos_y=int(self.displacement*3)):
                    if self.sleeps: 
                        time.sleep(self.sleep_time)
                    return True
                if self.button_msg("Exit", pos_y=int(self.displacement*3.5)):
                    return False
                pygame.display.update()
                
                




