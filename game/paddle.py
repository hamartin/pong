'''This file represents a paddle in the game.'''


from .baserectangle import BaseRectangle


class Paddle(BaseRectangle):

    '''This class represents a paddle in the game.'''

    PERCENT_SIZE = (0.0125, 0.125)
    # 5 pixels when y == 600
    PERCENT_MOVE = 0.008333333333333333

    def __init__(self, color, screen_size):
        super().__init__(color)
        self.screen_size = screen_size

        # We calculate the height and width of the paddle.
        size_x = int(screen_size[0]*self.PERCENT_SIZE[0])
        size_y = int(screen_size[1]*self.PERCENT_SIZE[1])
        super().set_size((size_x, size_y))

        # The position of the paddle is calculated by the player object.

    def move_down(self):
        '''Moves the paddle down on the screen.'''
        self.rect.y += int(self.screen_size[1]*self.PERCENT_MOVE)
        if self.rect.y > self.screen_size[1]-self.get_size()[1]:
            self.rect.y = int(self.screen_size[1]-self.get_size()[1])

    def move_up(self):
        '''Moves the paddle up on the screen.'''
        self.rect.y -= int(self.screen_size[1]*self.PERCENT_MOVE)
        if self.rect.y < 0:
            self.rect.y = 0
