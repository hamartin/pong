'''This file represents the net in the game'''


from .baserectangle import BaseRectangle


class Net(BaseRectangle):

    '''This class represents the net in the game.'''


    PERCENT_SIZE = (0.0125, 0.9875)

    def __init__(self, color, screen_size):
        super().__init__(color)
        self.screen_size = screen_size

        # We calculate the height and width of the net.
        size_x = int(screen_size[0]*self.PERCENT_SIZE[0])
        size_y = int(screen_size[1]*self.PERCENT_SIZE[1])
        super().set_size((size_x, size_y))

        # We calculate the position of the net.
        pos_x = int((screen_size[0]/2.0)-(size_x/2.0))
        pos_y = int((screen_size[1]-size_y)/2)
        super().set_position((pos_x, pos_y))
