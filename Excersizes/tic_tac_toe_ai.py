import pygame 
import random 
import time 
import math 


class Game:
    def __init__(self): 

        self._BOARD = [None]*9 

        pygame.init() 
        # game constants 
        self.display_width = 900
        self.display_height = 900

        self.unit = self.display_width/3 

        ## colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN  = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        #Main game objects 
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Unbeatable Tic-Tac-Toe AI')
        self.clock = pygame.time.Clock()
        self.locations_arr = [(i,j) for j in range(3) for i in range(3)]
        self.location2ind = {self.locations_arr[i]:i for i in range(len(self.locations_arr))} 
        self.ind2location = {k: j for j, k in self.location2ind.items()}

        self.player  = {1:'X', 2:'O'}
    ### text_objects 
    def _text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect() 

    def _text_display(self, text, location):
        large_font = pygame.font.Font('freesansbold.ttf', 75)
        text_surf, text_rect = self._text_objects(" "+text+" ", large_font, self.BLACK)
        self.gameDisplay.blit(text_surf, location)
        pygame.display.update()

    def _line(self, screen, lcolor, start, end, thickness=5):
        pygame.draw.line(screen, lcolor, start, end, thickness)


    def show_on_board(self):
        for index, sym in enumerate(self._BOARD): 
            if sym is not None: 
                x, y = self.ind2location[index]
                x *= self.unit 
                y *= self.unit 

                x += self.unit/2 - 45
                y += self.unit/2 - 45 
                self._text_display(sym, location = (x,y))

    def build_grid(self): 
        points = [((1,0), (1, 3)), ((2,0), (2, 3)), ((0,1), (3, 1)), ((0,2), (3, 2))]
        for point in points: 
            self._line(self.gameDisplay, lcolor = self.BLACK, start = (point[0][0]*self.unit, point[0][1]*self.unit), end = (point[1][0]*self.unit, point[1][1]*self.unit))

    def main_loop(self):
        Exit = False
        stopPlaying = False 
        self.gameDisplay.fill(self.WHITE)
        while not Exit and not stopPlaying:
            self.build_grid()
            if self.is_winning_configuration(self._BOARD, 1): 
                print('X WON!')
                stopPlaying = True
                time.sleep(5)
            if self.is_winning_configuration(self._BOARD, 2): 
                print('Computer WON!')
                stopPlaying = True
                time.sleep(5)

            if self.is_draw(self._BOARD):
                print('Draw Game')
                stopPlaying = True
                time.sleep(5)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    Exit = True
                if event.type == pygame.MOUSEBUTTONDOWN and not stopPlaying: 
                    player_index = self.get_user_input(event)
                    if self._BOARD[player_index] is not None:
                        continue 
                    self._BOARD[player_index] = 'X'
                    self.show_on_board()


                    comp_index = self.computer_play()
                    if comp_index is not None: 
                        self._BOARD[comp_index] = 'O'
        
                    else:
                        print('Game Over')
                        stopPlaying = True 
                    self.show_on_board() 
                    time.sleep(0.5)

            pygame.display.update()
            self.clock.tick(25)


    def get_user_input(self, event):
        pos = pygame.mouse.get_pos()
        x, y = pos 
        x = int (x//self.unit) 
        y = int (y//self.unit)  
        index = self.location2ind[(x,y)]
        return index


    def is_winning_configuration(self, board, player):
        def get_cols(seq):
            new_seq = list(seq)
            x = [new_seq[i:i + 3] for i in range(0, len(new_seq), 3)] 
            x = list(map(list, zip(*x)))
            return x
        def get_diags(seq):
            new_seq = list(seq)
            x = [new_seq[i:i + 3] for i in range(0, len(new_seq), 3)] 
            diag_1 = [row[-(i+1)] for i, row in enumerate(x)]
            diag_2 = [row[i] for i, row in enumerate(x)]
            return [diag_1, diag_2]

        if player == 1:
            sym = 'X'
        elif player == 2:
            sym = 'O'

        winning = False

        if (all(item == sym for item in board[:3])) or (all(item == sym for item in board[3:6])) or(all(item == sym for item in board[6:])):
            winning = True

        cols = get_cols(board)
        if (all(item == sym for item in cols[0])) or (all(item == sym for item in cols[1])) or (all(item == sym for item in cols[2])): 
            winning = True

        diags = get_diags(board)
        if (all(item == sym for item in diags[0])) or (all(item == sym for item in diags[1])): 
            winning = True
        
        return winning


    def static_evaluation(self, board):
        if self.is_winning_configuration(board, 1):
            return -1
        if self.is_winning_configuration(board, 2):
            return 1
        if self.is_draw(board):
            return 0

    def is_draw(self, board): 
        cond_1 = self.is_winning_configuration(board, 1) or self.is_winning_configuration(board, 2)
        cond_2 = all(item is not None for item in board) 
        return (not cond_1) and (cond_2) 

    def computer_play(self):
        best_location = None
        max_value = -math.inf
        for location in self.get_empty_locations(self._BOARD): 
            child = list(self._BOARD)
            child[location] = 'O'
            value = self.minimax(child, maximizing = False)
            if value > max_value:
                max_value = value
                best_location = location
        return best_location


    def get_empty_locations(self, board): 
        empty_locations = [i for i, item in enumerate(board) if item is None]
        return empty_locations 

    def minimax(self, board, maximizing): 
        if self.static_evaluation(board) is not None:
            return self.static_evaluation(board)

        if maximizing:
            max_eval = -math.inf
            for location in self.get_empty_locations(board):
                child = list(board) 
                child[location] = 'O'
                val = self.minimax(child, maximizing = False)
                max_eval = max(max_eval, val)
            return max_eval
        else:
            min_eval = math.inf
            for location in self.get_empty_locations(board):
                child = list(board)
                child[location] = 'X'
                val = self.minimax(child, maximizing = True)
                min_eval = min(min_eval, val)
            return min_eval
        pass

    def get_best_location(self, board_1, board_2):
        return [i for i, (x, y) in enumerate(zip(board_1, board_2)) if x!= y]


b = Game()

b.main_loop()
 
