'''
This file represents the base rectangle which all/most of the sprites
consist of.
'''


import pygame

from .statics import (
    BLACK
)


class BaseRectangle(pygame.sprite.Sprite):

    '''
    This class represents the base rectangle which all/most of the
    sprites consist of.
    '''

    def __init__(self, color):
        super().__init__()
        self.color = color
        self.image = None
        self.rect = None

    def resize(self, sprite_size):
        '''Sets the new sprite size.'''
        self.image = pygame.Surface(sprite_size)
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        pygame.draw.rect(self.image, self.color, (0, 0, sprite_size[0], sprite_size[1]))
        self.rect = self.image.get_rect()

    def set_position(self, sprite_pos):
        '''Sets the x and y position of the upper left corner of the rectangle.'''
        self.rect.x = sprite_pos[0]
        self.rect.y = sprite_pos[1]
