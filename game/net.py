'''This file represents the net in the game.'''


from .baserectangle import BaseRectangle


class Net(BaseRectangle):

    '''This class represents the net in the game.'''

    SIZE_RATIO = (0.0125, 0.9875)

    def __init__(self, color, screen_size):
        net_width = int(screen_size[0]*self.SIZE_RATIO[0])
        net_height = int(screen_size[1]*self.SIZE_RATIO[1])
        super().__init__(color)
        super().resize((net_width, net_height))

        pox_x = int(screen_size[0]/2) - int(net_width/2)
        pos_y = int((screen_size[1] - net_height)/2)
        super().set_position((pox_x, pos_y))

    def resize(self, screen_size):
        '''Resizes the sprite to match the current screen size.'''
        net_width = int(screen_size[0]*self.SIZE_RATIO[0])
        net_height = int(screen_size[1]*self.SIZE_RATIO[1])
        super().resize((net_width, net_height))

        pos_x = int(screen_size[0]/2) - int(net_width/2)
        pos_y = int((screen_size[1] - net_height)/2)
        super().set_position((pos_x, pos_y))
