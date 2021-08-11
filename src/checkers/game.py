# from .piece import Piece
import pygame
from .constants import RED, SQUARE_SIZE, WHITE, BLUE
from .board import Board


class Game:
    def __init__(self,win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
    
    def _init(self):
        self.selected = None
        self.valid_moves = {}
        self.board = Board()
        self.turn = RED
    
    def reset(self):
        self._init()
    
    def winner(self):
        return self.board.winner()

    def select(self, row, col):
        if self.selected:
            #print("piece already selected")
            result = self._move(row,col)
            if not result:
                #print("That was invalid. Calling select again")
                self.selected = None
                self.select(row,col)
        
        piece = self.board.get_piece(row,col)
        #print("Getting Piece from board")
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            #print(f"We got moves: {self.valid_moves}")
            #print("Returning True")
            return True

        #print("Returning False")    
        return False

    def _move(self, row,col):
        #print("trying to move")
        piece = self.board.get_piece(row,col)
        #print("Got piece at row,col")
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            #print("Calling board.move")
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                #print("Piece captured")
                self.board.remove(skipped)
            #print("Changing turns")
            self.change_turn()
        else:
            return False
        
        return True

    def draw_valid_moves(self,moves):
        for move in moves:
            row,col = move
            pygame.draw.circle(self.win, BLUE,(col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = RED
        else:
            self.turn = WHITE

    
    def get_board(self):
        return self.board
    
    def ai_move(self,board):
        self.board = board
        self.change_turn()

