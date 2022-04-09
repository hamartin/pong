'''This file represents the paddles in the game.'''


from .baserectangle import BaseRectangle
from .statics import (
    PIXELMOVE
)


class PaddleError(Exception):
    pass


class Paddle(BaseRectangle):

    '''This class represents the net in the game.'''

    SIZE_RATIO = (0.0125, 0.125)
    SIDE = {"LEFT": (0, 0.01125, 0.5), "RIGHT": (1, 0.98875, 0.5)}

    def __init__(self, color, screen_size, side):
        self.screen_size = screen_size
        if side not in self.SIDE.keys():
            raise PaddleError("Side must be either \"LEFT\" or \"RIGHT\", not {0}.".format(side))
        self.side = side
        
        self.paddle_width = int(screen_size[0]*self.SIZE_RATIO[0])
        self.paddle_height = int(screen_size[1]*self.SIZE_RATIO[1])
        super().__init__(color)
        super().resize((self.paddle_width, self.paddle_height))

        pos_x = int(screen_size[0]*self.SIDE[self.side][1])
        if self.side == "RIGHT":
            pos_x = pos_x-self.paddle_width
        pos_y = int(screen_size[1]/2)-int(self.paddle_height/2)
        super().set_position((pos_x, pos_y))

    def move_down(self):
        '''Move the sprite in the positive y direction.'''
        self.rect.y += PIXELMOVE*self.screen_size[1]
        if self.rect.y > self.screen_size[1]-self.paddle_height:
            self.rect.y = self.screen_size[1]-self.paddle_height

    def move_up(self):
        '''Move the sprite in the negative y direction.'''
        self.rect.y -= PIXELMOVE*self.screen_size[1]
        if self.rect.y < 0:
            self.rect.y = 0

    def resize(self, screen_size):
        '''Resizes the sprite to match the current screen size.'''
        self.screen_size = screen_size

        # Figure out the new sprite size
        self.paddle_width = int(screen_size[0]*self.SIZE_RATIO[0])
        self.paddle_height = int(screen_size[1]*self.SIZE_RATIO[1])
        super().resize((self.paddle_width, self.paddle_height))

        pos_x = int(screen_size[0]*self.SIDE[self.side][1])
        if self.side == "RIGHT":
            pos_x = pos_x - self.paddle_width
        pos_y = int(screen_size[1]/2)-int(self.paddle_height/2)
        super().set_position((pos_x, pos_y))
