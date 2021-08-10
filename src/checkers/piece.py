import pygame
from .constants import RED, SQUARE_SIZE, GREY, CROWN


class Piece:
    PADDING = 13
    OUTLINE = 4

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
    
    def calc_pos(self):
        self.x = (SQUARE_SIZE * self.col) + (SQUARE_SIZE // 2)
        self.y = (SQUARE_SIZE * self.row) + (SQUARE_SIZE // 2)

    def make_king(self):
        self.king = True
    
    def move(self, row, col):
        """Moves the Piece to its new postion (row,col)

        Args:
            row (int): Row to move the piece to
            col (int): Col to move the piece to
        """
        self.row = row
        self.col = col
        self.calc_pos()

    def draw(self,win):
        self.calc_pos()
        radius = (SQUARE_SIZE//2) - self.PADDING
        pygame.draw.circle(win,GREY, (self.x,self.y), radius + self.OUTLINE)
        pygame.draw.circle(win,self.color, (self.x,self.y), radius)

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2))
    
    def __repr__(self) -> str:
        return str(self.color)
