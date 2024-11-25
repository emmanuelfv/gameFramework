"""
tic_tac_toe_screen.py module. Class to showcase the graphic interface prior the agent player creation  

"""
import time
import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (255,0,255)
WHITE = (255,255,255)
BLACK = (0,0,0)

class TicTacToeScreen:
    """
    TicTacToeScreen class. Graphic interface for human interaction
    """
    

    def __init__(self):
        """__init__ method."""
        pygame.init()
        self.displacement = 64
        self.piece_size = (self.displacement,self.displacement)
        self.grid_size = (self.displacement*5, self.displacement*5)
        self.display = pygame.display.set_mode(self.grid_size)
        pygame.display.set_caption("tic_tac_toe")
        self.icon_o = pygame.transform.scale(pygame.image.load("resources/icon_o.png"), self.piece_size)
        self.icon_x = pygame.transform.scale(pygame.image.load("resources/icon_x.png"), self.piece_size)
        pygame.display.set_icon(self.icon_o)
        self.background = pygame.image.load("resources/background.jpg")
        self.turn = 1
        self.movements = [[0] * 3 for i in range(3)]

    def add_movement(self):
        mouse_values = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()
        game_pos = (mouse_pos[0]//self.displacement - 1, mouse_pos[1]//self.displacement - 1)
        if mouse_values[0] and 0 <= game_pos[0] <= 2 and 0 <= game_pos[1] <= 2 and self.movements[game_pos[0]][game_pos[1]] == 0:
            self.movements[game_pos[0]][game_pos[1]] = self.turn
            self.turn += 1
            time.sleep(0.1)
            

    def display_movements(self):
        count = 0
        for i in range(3):
            for j in range(3):
                if self.movements[i][j]  != 0:
                    count += 1
                    movement_pos = (self.displacement * (i+1), self.displacement * (j+1))
                    icon = self.icon_o if self.movements[i][j] % 2 == 0 else self.icon_x
                    self.display.blit(icon, movement_pos)
        if count == 9:
            self.set_game_results(0)

    def run(self):
        """display method. Runs the game loop for tic tac toe game"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.display.blit(self.background, (0,0))
            d = self.displacement
            pygame.draw.lines(self.display, PURPLE, True, ((d*2,d*1),(d*3,d*1),(d*3,d*4),(d*2,d*4)), 3)
            pygame.draw.lines(self.display, PURPLE, True, ((d*1,d*2),(d*4,d*2),(d*4,d*3),(d*1,d*3)), 3)
            pygame.draw.lines(self.display, GREEN, True, ((d*1,d*1),(d*4,d*1),(d*4,d*4),(d*1,d*4)), 3)
            #self.checkForMovement()
            self.add_movement()
            self.display_movements()
            pygame.display.update()

    def set_game_results(self, results):
        """show_end_game Method. Shows the results of the game"""
        fond = pygame.font.Font('freesansbold.ttf', 32)
        end_message = fond.render('END GAME', True, WHITE, BLACK)
        winner = fond.render(('DRAW','WINNER','LOSER')[results], True, WHITE, BLACK)
        self.display.blit(end_message, (self.get_centered_x_position(end_message), 100))
        self.display.blit(winner, (self.get_centered_x_position(winner), 132))
         

    def get_centered_x_position(self, surface):
        return (self.grid_size[0]-surface.get_size()[0])//2




if __name__ == "__main__":
    TicTacToeScreen().run()