'''This file represents a player in the game.'''


from .paddle import Paddle
from .statics import (
    WHITE
)


class PlayerError(Exception):
    pass


class Player:

    '''This class represents a player in the game.'''

    SIDE = ("LEFT", "RIGHT")
    PERCENT_POS = {
        "LEFT": (0.0125, 0.5),
        "RIGHT": (0.9875, 0.5)
    }

    def __init__(self, side, screen_size):
        self.side = side
        self.screen_size = screen_size
        self.paddle = Paddle(WHITE, screen_size)
        self.points = 0

        if side not in self.PERCENT_POS.keys():
            raise PlayerError("Side cannot be {0}, must be one of {1}.".format(side, self.PERCENT_POS.keys()))

        # We calculate the position of the net.
        pos_x = int(screen_size[0]*self.PERCENT_POS[side][0])
        pos_y = int(screen_size[1]*self.PERCENT_POS[side][1] - self.paddle.get_size()[1]/2)
        if "RIGHT" in side:
            pos_x -= self.paddle.get_size()[0]
        self.paddle.set_position((pos_x, pos_y))

        # The size of the paddle is handled by the Paddle object itself.

    def get_sprite(self):
        '''Returns the paddle sprite.'''
        return self.paddle

    def move_down(self):
        '''Moves the paddle down on the screen.'''
        self.paddle.move_down()

    def move_up(self):
        '''Moves the paddle up on the screen.'''
        self.paddle.move_up()

    def score(self):
        '''Increses the players score.'''
        self.points += 1
