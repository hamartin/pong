'''This file represents the ball in the game.'''


import random

from .baserectangle import BaseRectangle
from .statics import (
    BALLMOVE
)


class Ball(BaseRectangle):

    '''This class represents the ball in the game.'''

    SIZE_RATIO = (0.015, 0.02)

    def __init__(self, color, screen_size):
        self.screen_size = screen_size
        self.vel_x = 0
        self.vel_y = 0
        
        self.ball_width = int(screen_size[0]*self.SIZE_RATIO[0])
        self.ball_height = int(screen_size[1]*self.SIZE_RATIO[1])
        self.reset_pos_x = int(screen_size[0]/2)-int(self.ball_width/2)
        self.reset_pos_y = int((screen_size[1]-self.ball_height)/2)
        pox_x = int(screen_size[0]/2)-int(self.ball_width/2)
        pos_y = int((screen_size[1]-self.ball_height)/2)

        super().__init__(color)
        super().resize((self.ball_width, self.ball_height))
        super().set_position((pox_x, pos_y))

    def bounce(self):
        '''Sends the ball in a new direction (bounces).'''
        vel_x_max = int(self.screen_size[0]*BALLMOVE[0]) 
        vel_x_min = -int(self.screen_size[0]*BALLMOVE[0])
        self.vel_x = -self.vel_x
        self.vel_y = random.randint(vel_x_min, vel_x_max)

    def reset(self):
        '''Puts the ball back to its original place.'''
        self.vel_x = 0
        self.vel_y = 0
        self.set_position((self.reset_pos_x, self.reset_pos_y))

    def resize(self, screen_size):
        '''Resizes the sprite to match the current screen size.'''
        self.screen_size = screen_size

        ball_width = int(screen_size[0]*self.SIZE_RATIO[0])
        ball_height = int(screen_size[1]*self.SIZE_RATIO[1])
        super().resize((ball_width, ball_height))

        pos_x = int(screen_size[0]/2) - int(ball_width/2)
        pos_y = int((screen_size[1] - ball_height)/2)
        super().set_position((pos_x, pos_y))

    def random_velocity(self):
        '''Gives the ball a random direction and speed.'''
        vel_x_max = int(self.screen_size[0]*BALLMOVE[0]) 
        vel_x_min = -int(self.screen_size[0]*BALLMOVE[0])
        vel_x_max2 = int(self.screen_size[1]*BALLMOVE[1])
        vel_x_min2 = -int(self.screen_size[1]*BALLMOVE[1])

        while self.vel_x < vel_x_max2 and self.vel_x > vel_x_min2:
            self.vel_x = random.randint(vel_x_min, vel_x_max)
        self.vel_y = random.randint(vel_x_min, vel_x_max)

    def update(self):
        '''Moves the ball in the direction velocity has been set to.'''
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y >= self.screen_size[1]-self.ball_height:
            self.vel_y = -self.vel_y
        if self.rect.y <= 0:
            self.vel_y = -self.vel_y
