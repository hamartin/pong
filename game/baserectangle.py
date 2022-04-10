'''This file represents the base rectangle which all the sprites consist off.'''


import pygame

from .statics import (
    BLACK
)


class BaseRectangle(pygame.sprite.Sprite):

    '''This class represents the base rectangle which all the sprites consist off.'''

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = None
        self.rect = None

    def get_position(self):
        '''Returns the rectangle position as a tuple.'''
        return (self.rect.x, self.rect.y)

    def get_size(self):
        '''Returns the rectangle size as a tuple.'''
        return self.image.get_size()

    def set_position(self, pos):
        '''Sets the x and y position of the upper left corner of the rectangle.'''
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def set_size(self, size):
        '''Sets a new sprite size.'''
        self.image = pygame.Surface(size)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.color, (0, 0, size[0], size[1]))
        self.rect = self.image.get_rect()
