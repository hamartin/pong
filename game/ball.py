'''This file represents the ball in the game.'''


import random

from .baserectangle import BaseRectangle


class Ball(BaseRectangle):

    '''This class represents the ball in the game.'''

    PERCENT_SIZE = (0.015, 0.02)
    MOVEMENT_RATIO = (0.00125, 0.0016666666666666668)

    def __init__(self, color, screen_size):
        super().__init__(color)
        self.screen_size = screen_size
        self.vel_x = 0
        self.vel_y = 0

        # We calculate the height and width of the ball.
        size_x = int(screen_size[0]*self.PERCENT_SIZE[0])
        size_y = int(screen_size[1]*self.PERCENT_SIZE[1])
        super().set_size((size_x, size_y))

        # We calculate the position of the net.
        pos_x = self.reset_x = int((screen_size[0]/2.0)-(size_x/2.0))
        pos_y = self.reset_y = int((screen_size[1]-size_y)/2)
        super().set_position((pos_x, pos_y))

    def bounce(self):
        '''Sends the ball in a new direction (bounces).'''
        vel_y_max = int(8*self.MOVEMENT_RATIO[1]*self.screen_size[1])
        vel_y_min = -vel_y_max
        self.vel_x = -self.vel_x
        self.vel_y = random.randint(vel_y_min, vel_y_max)

    def random_velocity(self):
        '''Gives the ball a random velocity within certain parameters.'''
        vel_x_max = int(8*self.MOVEMENT_RATIO[0]*self.screen_size[0])
        vel_x_min = -vel_x_max
        vel_x_max2 = int(4*self.MOVEMENT_RATIO[0]*self.screen_size[0])
        vel_x_min2 = -vel_x_max2

        while self.vel_x < vel_x_max2 and self.vel_x > vel_x_min2:
            self.vel_x = random.randint(vel_x_min, vel_x_max)
        self.vel_y = random.randint(vel_x_min, vel_x_max)

    def reset(self):
        '''Moves the ball back to its reset position and sets velocity to 0 in both directions.'''
        self.vel_x = 0
        self.vel_y = 0
        self.set_position((self.reset_x, self.reset_y))

    def update(self):
        '''Moves the ball in the direction vel_x and vel_y has been set to.'''
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.y >= self.screen_size[1]-self.get_size()[1]:
            self.vel_y = -self.vel_y
        if self.rect.y <= 0:
            self.vel_y = -self.vel_y
