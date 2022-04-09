'''This file represents the game, the controller if you will.'''


import pygame

from pygame.image import load
from pathlib import Path

from .ball import Ball
from .net import Net
from .paddle import Paddle
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
        self.clock = None
        self.running = False
        self.screen = None
        self.sprites = None
        self.player1 = None
        self.player1_score = 0
        self.player2 = None
        self.player2_score = 0

        self._init_view()
        self._init_sprites()

    def _draw(self):
        self.screen.fill(BLACK)
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)

        pygame.display.flip()

    def _game_logic(self):
        self.sprites.update()

        if self.ball.rect.x <= 0:
            self.player1_score += 1
            self.ball.reset()
        if self.ball.rect.x >= self.screen.get_size()[0]-self.ball.image.get_width():
            self.player2_score += 1
            self.ball.reset()

        if pygame.sprite.collide_mask(self.ball, self.player1):
            self.ball.bounce()
        if pygame.sprite.collide_mask(self.ball, self.player2):
            self.ball.bounce()

    def _handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.VIDEORESIZE:
                self._resize_sprites(event.dict['size'])
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
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

    def _init_sprites(self):
        screen_size = self.screen.get_size()
        self.background = self._load_sprite("background")
        self.sprites.add(Net(WHITE, screen_size))

        self.ball = Ball(YELLOW, screen_size)
        self.sprites.add(self.ball)
        self.player1 = Paddle(WHITE, self.screen.get_size(), "LEFT")
        self.sprites.add(self.player1)
        self.player2 = Paddle(WHITE, self.screen.get_size(), "RIGHT")
        self.sprites.add(self.player2)

    def _init_view(self):
        self.screen = pygame.display.set_mode(INITIAL_SCREEN_SIZE, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.sprites = pygame.sprite.Group()

        pygame.init()
        pygame.display.set_caption(CAPTION)

    def _load_sprite(self, name):
        filename = Path(__file__).parent / Path("assets/sprites/" + name + ".png")
        sprite = load(filename.resolve())
        return sprite.convert()

    def _resize_sprites(self, screen_size):
        self.background = pygame.transform.scale(self.background, screen_size)
        for sprite in self.sprites:
            sprite.resize(screen_size)

    def run(self):
        '''Starts the game itself.'''
        if self.running:
            return

        self.running = True
        while self.running:
            self._handle_input()
            self._game_logic()
            self._draw()
            # This controlls the games rate in general.
            self.clock.tick(FPS)
