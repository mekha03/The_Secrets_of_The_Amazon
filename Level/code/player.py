import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('graphics/Explorer_Girl-right_64x115.png').convert_alpha()
        # self.image = pygame.Surface((32, 64))
        # self.image.fill('red')
        self.rect = self.image.get_rect(topleft= pos)
        # self.image = pygame.image.load('graphics/Explorer Girl-right.png').convert_alpha()

        # player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.image = pygame.image.load('graphics/Explorer_Girl-right_64x115.png').convert_alpha()
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.image = pygame.image.load('graphics/Explorer_Girl-left.png_64x115.png').convert_alpha()
            self.direction.x = -1
        else:
            self.direction.x = 0

        if keys[pygame.K_UP]:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed
    def update(self):
        self.get_input()