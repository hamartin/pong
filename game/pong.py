'''This file represents the game, the controller if you will.'''


import pygame

from pygame.image import load
from pathlib import Path

from .ball import Ball
from .net import Net
from .player import Player
from .statics import (
    BLACK,
    CAPTION,
    FPS,
    INITIAL_SCREEN_SIZE,
    YELLOW,
    WHITE
)


class Pong:

    '''This class represents the game, the controller if you will.'''

    def __init__(self):
        self.background = None
        self.ball = None
        self.clock = None
        self.player1 = None
        self.player2 = None
        self.running = False
        self.screen = None
        self.sprites = None

        self._init_view() 
        self._init_sprites()

    def _init_sprites(self):
        self.sprites = pygame.sprite.Group()
        self.background = self._load_sprite("background")

        ss = self.screen.get_size()
        self.sprites.add(Net(WHITE, ss))
        self.ball = Ball(YELLOW, ss)
        self.sprites.add(self.ball)
        self.player1 = Player("LEFT", ss)
        self.sprites.add(self.player1.get_sprite())
        self.player2 = Player("RIGHT", ss)
        self.sprites.add(self.player2.get_sprite())

    def _init_view(self):
        self.screen = pygame.display.set_mode(INITIAL_SCREEN_SIZE)
        self.clock = pygame.time.Clock()

        pygame.init()
        pygame.display.set_caption(CAPTION)

    def _draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        score_font, size = self.player1.get_score()
        self.screen.blit(score_font, (10, 10))
        score_font, size = self.player2.get_score()
        self.screen.blit(score_font, (self.screen.get_size()[0]-size[0]-10, 10))
        self.sprites.draw(self.screen)
        pygame.display.flip()

    def _game_logic(self):
        self.sprites.update()

        ball_pos = self.ball.get_position()
        if ball_pos[0] <= 0:
            self.player2.score()
            self.ball.reset()
        if ball_pos[0] >= self.screen.get_size()[0]-self.ball.get_size()[0]:
            self.player1.score()
            self.ball.reset()

        if pygame.sprite.collide_mask(self.ball, self.player1.get_sprite()):
            self.ball.bounce()
        elif pygame.sprite.collide_mask(self.ball, self.player2.get_sprite()):
            self.ball.bounce()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_SPACE and self.ball.vel_x == 0 and self.ball.vel_y == 0:
                    self.ball.random_velocity()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player1.move_up()
        if keys[pygame.K_s]:
            self.player1.move_down()
        if keys[pygame.K_UP]:
            self.player2.move_up()
        if keys[pygame.K_DOWN]:
            self.player2.move_down()

    def _load_sprite(self, name):
        filename = Path(__file__).parent / Path("assets/sprites/" + name + ".png")
        sprite = load(filename.resolve())
        # Notie that this will ignore alpha channel.
        return sprite.convert()

    def run(self):
        '''Starts the game itself.'''
        if self.running:
            return

        self.running = True
        while self.running:
            self._handle_input()
            self._game_logic()
            self._draw()
            # This makes sure the game framerate and controlls go no faster than FPS times a second.
            self.clock.tick(FPS)
        pygame.quit()

